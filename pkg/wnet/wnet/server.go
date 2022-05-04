package wnet

import (
	"C"
	"fmt"
	"net"
)

//定义服务接口
type INetServer interface {
	Start()
	Stop()
	Serve()
	Packet()  		IMsgPack
	GetConnMgr() 	IConnManager
}

type NetServer struct {
	Name          string
	IP            string
	Port          int
	IPVersion     string
	MsgHandler    IMsgHandle
	ConnMgr       IConnManager
	Pack          IMsgPack
	netPyAddr string
	PeerID        uint32
}

func NewNetServer() *NetServer {
	s := &NetServer{
		Name:       "NetServer",
		IP:         "127.0.0.1",
		Port:       60000,
		IPVersion:  "tcp4",
		MsgHandler: NewMsgHandle(),
		ConnMgr:    NewConnManager(),
		Pack: 		NewMsgPack(),
		PeerID:		PeerIDStart,
	}
	s.MsgHandler.SetServer(s)
	return s
}

//export StartNetThread
func StartNetThread(netPyAddr *C.char, ip *C.char, port int)  {
	s := NewNetServer()
	s.netPyAddr = C.GoString(netPyAddr)
	s.IP = C.GoString(ip)
	s.Port = port
	s.Start()
}

func (s *NetServer) Start() {
	go s.PyNetStart()
	go s.TcpStart()
	go s.MsgHandler.StartNetWorker()
}

func (s *NetServer) PyNetStart() {
	conn, err := net.Dial("tcp", s.netPyAddr)
	if err != nil {
		fmt.Println("client start err, exit!", err)
		return
	}
	pyConn := NewConnection(s, conn, PyConnId, s.MsgHandler,true)
	// 初始化python和go的交互
	for {
		err = pyConn.SendPyMsg(uint32(CmdInit), 0, 0, []byte("hello"))
		if err != nil {
			fmt.Println("write error err ", err)
			continue
		}
		pymsg := pyConn.ReadFromPy()
		if pymsg != nil && ServerCmdEnum(pymsg.GetCmdID()) == CmdInit {
			fmt.Println("PyNetStart finish")
			break
		}
	}
	go pyConn.Start()
}

func (s *NetServer) TcpStart() {
	addr, err := net.ResolveTCPAddr(s.IPVersion, fmt.Sprintf("%s:%d", s.IP, s.Port))
	if err != nil {
		fmt.Println("resolve tcp addr err: ", err)
		return
	}
	listener, err := net.ListenTCP(s.IPVersion, addr)
	if err != nil {
		panic(err)
	}
	fmt.Println("start Wnet server  ", s.Name, " succ, now listenning...")
	for {
		conn, err := listener.AcceptTCP()
		if err != nil {
			fmt.Println("Accept err ", err)
			continue
		}
		fmt.Println("Get conn remote addr = ", conn.RemoteAddr().String())
		if s.ConnMgr.Len() >= MaxConn {
			_ = conn.Close()
			continue
		}
		dealConn := NewConnection(s, conn, s.PeerID, s.MsgHandler, false)
		s.PeerID++
		go dealConn.Start()
	}
}


func (s *NetServer) Stop() {
	fmt.Println("[STOP] Wnet server , name ", s.Name)
	s.ConnMgr.ClearConn()
}

func (s *NetServer) Serve() {
	s.Start()
	select {}
}

func (s *NetServer) Packet() IMsgPack {
	return s.Pack
}

func (s *NetServer) GetConnMgr() IConnManager {
	return s.ConnMgr
}
