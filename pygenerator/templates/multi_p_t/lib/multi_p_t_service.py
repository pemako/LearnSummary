#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import signal
import sys
import threading
from multiprocessing import Manager

from thrift.protocol import TBinaryProtocol
from thrift.server import TProcessPoolServer
from thrift.transport import TSocket, TTransport

from loggingext.sockethandler import LogRecordSocketReceiver


class Multi_p_tService(object):
    """Multi_p_t Service"""

    def __init__(self, cfg, execute_dir):
        self.logger = logging.getLogger('multi_p_t')
        self.cfg = cfg
        self.execute_dir = execute_dir
        self.port = cfg.getint('default', 'service.port')
        self.server = None
        self.init_signal_handler()
        # 初始化多进程间共享的容器
        manager = Manager()
        # 存放缓存的dict，约定key需要一个特定类型的prefix，即[type_value]
        # 例如媒体信息：'media_12306'，offer信息：'creative_10086'
        # 对这个dict的读写是进程安全的
        self.cache_dict = manager.dict()

    def init_signal_handler(self):
        """删除不需要处理的信号，以及增加需要处理的信号,并且设置不同的处理方法
        这里默认处理了SIGTERM和SIGINT，并且尝试停止service
        SIGINT = 2，可使用kill -2 pid 或 当CTRL+C终止程序时发出
        SIGTERM = 15，可使用kill -15 pid发出
        """
        signals = (signal.SIGTERM, signal.SIGINT)
        self.signal_handlers = {}
        for sig in signals:
            self.signal_handlers[sig] = signal.getsignal(sig)
            signal.signal(sig, self.handle_signal)

    def handle_signal(self, signal, frame):
        self.logger.info('Handle signal %d, stop service', signal)
        self.logger.info('Try to stop all workers.')
        self.stop()
        self.logger.info('Bye-bye.')
        sys.exit(0)

    def run_log_receiver_thread(self):
        """启动一个独立的线程，收集worker的日志"""
        tcpserver = LogRecordSocketReceiver(host='localhost',
                                            port=self.cfg.getint('default', 'service.logging.port'))
        t = threading.Thread(target=tcpserver.serve_until_stopped)
        t.daemon = True
        t.start()

    def run(self):
        self.logger.info('Multi_p_t service starts to run.')
        self.run_log_receiver_thread()

        handler = SomeHandler(self.cfg, self.cache_dict)
        processor = SomeServer.Processor(handler)
        transport = TSocket.TServerSocket(port=self.port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolAcceleratedFactory()
        workerNum = self.cfg.getint('default', 'server.workers')

        self.server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
        # 设置在worker进程启动时的callback，在worker进程重置logging config
        self.server.setPostForkCallback(self.resetWorkerLogConfig)
        self.server.setNumWorkers(workerNum)

        try:
            self.logger.info('Start multi service')
            self.server.serve()
        except Exception, why:
            self.logger.fatal('Serve failed, %s', why)
            self.server.stop()
            sys.exit(1)
        print 'done.'

    def stop(self):
        self.logger.info('Multi_p_t service will stop.')
        self.server.stop()
