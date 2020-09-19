#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import signal
import sys
import threading
import time


class Multi_tService(object):
    """MultiT Service"""

    def __init__(self, cfg, execute_dir):
        self.logger = logging.getLogger('multi_t')
        self.cfg = cfg
        self.execute_dir = execute_dir
        # worker
        self.running = False
        self.worker_mum = self.cfg.getint('default', 'service.workers')
        self.worker_threads = []

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
        self.logger.info('Init signal handler')

    def handle_signal(self, signal, frame):
        self.logger.info('Handle signal %d, stop service', signal)
        self.logger.info('Try to stop all workers.')
        self.stop()
        self.logger.info('Bye-bye.')
        sys.exit(0)

    def work_main(self):
        while self.running:
            self.logger.info('I\'m running')
            # do something as your wish
            time.sleep(1)
        self.logger.info('Thread %d exits', threading.current_thread().ident)

    def run(self):
        self.init_signal_handler()
        self.logger.info('MultiT service starts to run.')
        self.running = True

        for i in range(self.worker_mum):
            t = threading.Thread(target=self.work_main)
            t.start()
            self.worker_threads.append(t)
            self.logger.info('Thread %d is created', t.ident)

        while True:
            alive = False
            for t in self.worker_threads:
                alive = alive or t.isAlive()
            if not alive:
                break

    def stop(self):
        self.logger.info('MultiT service will stop.')
        self.running = False
