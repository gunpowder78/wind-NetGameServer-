import uuid
import asyncio
import logging
from engine.logger.LogModule import init_log
import sys
from engine.utils.Utils import init_asyncio_loop_policy

# python 3.9.12


class Engine:
    def __init__(self, name: str, process_pool: int = None) -> None:
        self.exiting = False
        self.server_id: str = uuid.uuid4().hex
        self.sid: bytes = self.server_id.encode()
        self.name: str = name

        self.ip = "127.0.0.1"
        self.port = 0

        self.request_que = asyncio.Queue()
        self.cmd_map = {}
        init_asyncio_loop_policy()
        self.loop = asyncio.get_event_loop()

        # 以下为各个插件
        init_log(self)

    async def init(self):
        logging.info("SrvEngine Init")
        argv_len = len(sys.argv)
        if argv_len < 2:
            raise ValueError("没有传递可用窗口")
        else:
            self.port = int(sys.argv[1])

    async def register(self):
        pass

    async def start(self):
        pass

    async def exit(self):
        pass

    async def launch(self):
        # 配置参数
        await self.init()
        # 注册rpc处理函数
        await self.register()
        # 启动前最后做一些逻辑操作等
        await self.start()
        logging.critical(f"################ 服务 {self.name} 启动完毕 ##############")
        logging.info("服务端口号:{}".format(self.port))

    def serve(self):
        logging.getLogger().setLevel(logging.INFO)
        self.loop.run_until_complete(asyncio.ensure_future(self.launch()))
        try:
            self.loop.run_forever()
        except SystemExit:
            logging.info("SYSTEM EXIT 0")
        finally:
            self.loop.close()
            logging.info("loop closed!!")

    def register_cmd(self, cmd_dct):
        self.cmd_map.update(cmd_dct)

    def get_cmd(self, name):
        logging.info(f"name:{name}, cmd_map:{self.cmd_map}")
        return self.cmd_map.get(name)

    async def on_client_request(self, client, cmd, request):
        func = self.get_cmd(cmd)
        if func:
            if asyncio.iscoroutinefunction(func):
                await func(client=client, request=request)
            else:
                func(client=client, request=request)
        else:
            logging.error(f"no rpc func:{cmd}")


# engine 实例
srv_inst: Engine = None
