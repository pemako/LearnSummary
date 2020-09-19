# -*- coding: utf-8 -*-

import logging
import signal
import sys
import threading
from collections import namedtuple

from idc_gm_spider import IdcGmSpider
from idc_mysql import MySql

GoodsCategory = namedtuple('GoodsCategory', ['id', 'url'])


class IdcCrawlerService(object):
    """IdcCrawler Service"""

    def __init__(self, cfg, execute_dir):

        self.logger = logging.getLogger('idc_crawler')
        self.cfg = cfg
        self.execute_dir = execute_dir
        self.running = False
        self.worker_mum = self.cfg.getint('default', 'service.workers')
        self.worker_goods_num = self.cfg.getint('default', 'service.workers.goods')
        self.init_signal_handler()

        self.mysql = MySql(host=cfg.get('db', 'host'),
                           port=cfg.getint('db', 'port'),
                           user=cfg.get('db', 'user'),
                           passwd=cfg.get('db', 'passwd'),
                           db=cfg.get('db', 'dbname'))
        self.gm_sql = cfg.get('gm', 'sql')
        self.worker_threads = []

        self.gm_spider = IdcGmSpider(self.mysql, self.logger)

    def gm_goods_urls(self):
        internal_config = self.mysql.fetchall(self.gm_sql)
        categorys = []
        for config in internal_config:
            categorys.append(GoodsCategory(*config[0:]))
        return categorys

    def init_signal_handler(self):
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

    def run(self):
        self.init_signal_handler()
        self.logger.info('MultiT service starts to run.')

        categorys = self.gm_goods_urls()

        # 开启20个线程，每个线程处理20个 goods
        for i in range(self.worker_mum):
            category = categorys[i * self.worker_goods_num:(i + 1) * self.worker_goods_num]
            t = threading.Thread(target=self.gm_spider.parse_goods, args=(category,))
            t.start()
            self.worker_threads.append(t)
            self.logger.info('Thread %d is created', t.ident)

        for t in self.worker_threads:
            t.join()

        while True:
            alive = False
            for t in self.worker_threads:
                alive = alive or t.isAlive()
            if not alive:
                break

    def stop(self):
        self.logger.info('IdcCrawler service will stop.')
        self.running = False
