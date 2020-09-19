#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import signal
import sys
import threading
import time
from multiprocessing import Condition, Manager, Process, Value

from loggingext.sockethandler import LogRecordSocketReceiver


class Multi_pService(object):
    """Multi_p Service"""

    def __init__(self, cfg, execute_dir):
        self.logger = logging.getLogger('multi_p')
        self.cfg = cfg
        self.execute_dir = execute_dir
        # worker
        self.worker_mum = self.cfg.getint('default', 'service.workers')
        self.workers = []
        self.is_running = Value('b', False)
        self.stop_condition = Condition()
        self.post_fork_callback = None
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
        SIGTERM = 15，可使用kill -15 pid发出"""

        signals = (signal.SIGTERM, signal.SIGINT)
        self.signal_handlers = {}
        for sig in signals:
            self.signal_handlers[sig] = signal.getsignal(sig)
            signal.signal(sig, self.handle_signal)

    def handle_signal(self, signal, frame):
        self.logger.info('Handle signal %d, stop service', signal)
        self.logger.info('Try to stop all workers.')
        self.stop()
        time.sleep(2)
        self.logger.info('Bye-bye.')
        sys.exit(0)

    def run_log_receiver_thread(self):
        """启动一个独立的线程，收集worker的日志"""
        tcpserver = LogRecordSocketReceiver(host='localhost',
                                            port=self.cfg.getint('default', 'service.logging.port'))
        tcpserver.logname = 'multi_p'
        t = threading.Thread(target=tcpserver.serve_until_stopped)
        t.daemon = True
        t.start()

    def reset_worker_log_config(self):
        """重置worker的logging config"""
        worker_logging_config = os.path.join(
            self.execute_dir, 'conf', 'multi_p_worker_logging.cfg')
        # print 'Reset worker logging config: %s' % (worker_logging_config)
        logging.config.fileConfig(worker_logging_config)

    def worker_process(self):
        if self.post_fork_callback:
            self.post_fork_callback()

        logger = logging.getLogger('worker')

        while self.is_running.value:
            logger.info("Worker process %s is working", os.getpid())
            time.sleep(1)

        logger.info("Worker process %s quits", os.getpid())

    def run(self):
        self.logger.info('Multi_p service starts to run.')
        self.init_signal_handler()
        self.run_log_receiver_thread()

        # 设置在worker进程启动时的callback，在worker进程重置logging config
        self.post_fork_callback = self.reset_worker_log_config

        self.logger.info('Start multi service')
        # this is a shared state that can tell the workers to exit when False
        self.is_running.value = True

        # fork the children
        for i in range(self.worker_mum):
            try:
                w = Process(target=self.worker_process)
                w.daemon = True
                w.start()
                self.workers.append(w)
            except Exception, x:
                logging.exception(x)

        for w in self.workers:
            w.join()

        # wait until the condition is set by stop()
        while True:
            self.stop_condition.acquire()
            try:
                self.stop_condition.wait()
                break
            except (SystemExit, KeyboardInterrupt):
                break
            except Exception, x:
                logging.exception(x)

        self.is_running.value = False

    def stop(self):
        self.logger.info('Multi_p service will stop.')
        self.is_running.value = False
        self.stop_condition.acquire()
        self.stop_condition.notify()
        self.stop_condition.release()
