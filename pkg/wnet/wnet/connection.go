package wnet

import (
	"context"
	"errors"
	"fmt"
	"io"
	"net"
	"sync"
)

type IConnection interface {
	Start()
	Stop()
	Context() context.Context

	GetTCPConnection() net.Conn
	GetPeerID() uint32
	GetIsPyConn() bool
	RemoteAddr() net.Addr
	SendMsg(msgID uint32, data []byte) error
	SendPyMsg(cmdID uint32,peerId uint32, msgID uint32, data []byte) error
	ReadFromPy() IMessage
}


type Connection struct {
	Server      INetServer
	Conn        net.Conn
	PeerID      uint32
	MsgHandler  IMsgHandle
	IsPyConn    bool
	ctx         context.Context
	cancel      context.CancelFunc
	msgBuffChan chan []byte

	sync.RWMutex
	propertyLock sync.Mutex
	isClosed bool
}

func NewConnection(server INetServer, conn net.Conn, peerID uint32, msgHandler IMsgHandle, isPyConn bool) IConnection {
	//初始化Conn属性
	c := &Connection{
		Server:      server,
		Conn:        conn,
		PeerID:      peerID,
		isClosed:    false,
		MsgHandler:  msgHandler,
		msgBuffChan: make(chan []byte, 1024),
		IsPyConn:    isPyConn,
	}
	c.Server.GetConnMgr().Add(c)
	return c
}

func (c *Connection) StartReader() {
	fmt.Println("[Reader Goroutine is running]")
	defer fmt.Println(c.RemoteAddr().String(), "[conn Reader exit!]")
	defer c.Stop()

	for {
		select {
		case <-c.ctx.Done():
			return
		default:
			headData := make([]byte, c.Server.Packet().GetHeadLen())
			if _, err := io.ReadFull(c.Conn, headData); err != nil {
				fmt.Println("read msg head error ", err)
				return
			}
			msg, err := c.Server.Packet().Unpack(headData)
			if err != nil {
				fmt.Println("unpack error ", err)
				return
			}
			var data []byte
			if msg.GetDataLen() > 0 {
				data = make([]byte, msg.GetDataLen())
				if _, err := io.ReadFull(c.Conn, data); err != nil {
					fmt.Println("read msg data error ", err)
					return
				}
			}
			msg.SetData(data)
			req := Request{
				conn: c,
				msg:  msg,
			}
			c.MsgHandler.SendMsgToTaskQueue(&req)
		}
	}
}

func (c *Connection) StartPyReader() {
	fmt.Println("[PyReader Goroutine is running]")
	defer fmt.Println(c.RemoteAddr().String(), "[conn PyReader exit!]")
	defer c.Stop()

	for {
		select {
		case <-c.ctx.Done():
			return
		default:
			headData := make([]byte, c.Server.Packet().GetPyHeadLen())
			if _, err := io.ReadFull(c.Conn, headData); err != nil {
				fmt.Println("read msg head error ", err)
				return
			}
			msg, err := c.Server.Packet().UnpackPy(headData)
			if err != nil {
				fmt.Println("unpack error ", err)
				return
			}
			var data []byte
			if msg.GetDataLen() > 0 {
				data = make([]byte, msg.GetDataLen())
				if _, err := io.ReadFull(c.Conn, data); err != nil {
					fmt.Println("read msg data error ", err)
					return
				}
			}
			msg.SetData(data)
			req := Request{
				conn: c,
				msg:  msg,
			}
			c.MsgHandler.SendMsgToTaskQueue(&req)
		}
	}
}

func (c *Connection) SendMsg(msgID uint32, data []byte) error {
	c.RLock()
	defer c.RUnlock()
	if c.isClosed == true {
		return errors.New("connection closed when send msg")
	}

	dp := c.Server.Packet()
	msg, err := dp.Pack(NewMessage(uint32(CmdPacket), msgID, data))
	if err != nil {
		fmt.Println("Pack error msg MsgID = ", msgID)
		return errors.New("Pack error msg ")
	}
	_, err = c.Conn.Write(msg)
	return err
}

func (c *Connection) SendPyMsg(cmdID uint32, PeerId uint32, msgID uint32, data []byte) error {
	c.RLock()
	defer c.RUnlock()
	if c.isClosed == true {
		return errors.New("connection closed when send msg")
	}

	dp := c.Server.Packet()
	msg, err := dp.PackPy(NewPyMessage(cmdID, PeerId, msgID, data))
	if err != nil {
		fmt.Println("Pack error msg MsgID = ", msgID)
		return errors.New("Pack error msg ")
	}
	_, err = c.Conn.Write(msg)
	return err
}

func (c *Connection) ReadFromPy() IMessage {
	headData := make([]byte, c.Server.Packet().GetPyHeadLen())
	if _, err := io.ReadFull(c.Conn, headData); err != nil {
		fmt.Println("read msg head error ", err)
		return nil
	}
	msg, err := c.Server.Packet().UnpackPy(headData)
	if err != nil {
		fmt.Println("unpack error ", err)
		return nil
	}
	var data []byte
	if msg.GetDataLen() > 0 {
		data = make([]byte, msg.GetDataLen())
		if _, err := io.ReadFull(c.Conn, data); err != nil {
			fmt.Println("read msg data error ", err)
			return nil
		}
	}
	msg.SetData(data)
	return msg
}

func (c *Connection) Start() {
	c.ctx, c.cancel = context.WithCancel(context.Background())
	if c.IsPyConn {
		go c.StartPyReader()
	} else{
		go c.StartReader()
		c.SendConnectToPy()
	}
	select {
	case <-c.ctx.Done():
		c.finalizer()
		return
	}
}

func (c *Connection) SendConnectToPy() {
	msg:= NewMessage(uint32(CmdConnect),0,[]byte(""))
	req := Request{
		conn: c,
		msg:  msg,
	}
	c.MsgHandler.SendMsgToTaskQueue(&req)
}

func (c *Connection) SendDisconnectToPy() {
	msg:= NewMessage(uint32(CmdDisconnect),0,[]byte(""))
	req := Request{
		conn: c,
		msg:  msg,
	}
	c.MsgHandler.SendMsgToTaskQueue(&req)
}


func (c *Connection) Stop() {
	c.SendDisconnectToPy()
	c.cancel()
}

func (c *Connection) GetTCPConnection() net.Conn {
	return c.Conn
}

func (c *Connection) GetPeerID() uint32 {
	return c.PeerID
}

func (c *Connection) GetIsPyConn() bool {
	return c.IsPyConn
}

func (c *Connection) RemoteAddr() net.Addr {
	return c.Conn.RemoteAddr()
}

func (c *Connection) Context() context.Context {
	return c.ctx
}

func (c *Connection) finalizer() {
	c.Lock()
	defer c.Unlock()
	if c.isClosed == true {
		return
	}
	fmt.Println("Conn Stop()...PeerID = ", c.PeerID)
	_ = c.Conn.Close()
	c.Server.GetConnMgr().Remove(c)
	close(c.msgBuffChan)
	//设置标志位
	c.isClosed = true
}