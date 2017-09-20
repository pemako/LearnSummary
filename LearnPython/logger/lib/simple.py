#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import signal
import logging
import logging.config
import argparse
import ConfigParser

class SimpleService(object):
	def __init__(self, cfg):
		self.logger = logging.getLogger('simple')

		self.running = False
		self.initSignalHandler()

		self.host = cfg.get('db', 'host')
		self.user = cfg.get('db', 'user')
		self.passwd = cfg.get('db', 'passwd')
		self.prot = cfg.getint('db', 'port')
		self.db = cfg.get('db', 'db_name')
		self.pool_size = cfg.get('db', 'pool_size')


	def initSignalHandler(self):
		"""
		删除不需要处理的信号，以及增加需要处理的信号,并且设置不同的处理方法
		里默认处理了SIGTERM和SIGINT，并且尝试停止service
		SIGINT = 2，可使用kill -2 pid 或 当CTRL+C终止程序时发出
		SIGTERM = 15，可使用kill -15 pid发出
		"""
		signals = (signal.SIGTERM, signal.SIGINT)
		self.signalHandlers = {}
		for sig in signals:
			self.signalHandlers[sig] = signal.getsignal(sig)
			signal.signal(sig, self.handleSignal)
	
	def handleSignal(self, signal, frame):
		self.logger.info('Handle signal %d, stop service', signal)
		self.logger.info('Try to stop all workers.')
		self.stop()
		self.logger.info('Bye-bye.')
		sys.exit(0)

	def run(self):
		self.logger.info('Simple service starts to run.')
		self.running = True
		while self.running:
			self.logger.debug('I\'m running')
			self.logger.info('I\'m running')
			self.logger.warn('I\'m running')
			self.logger.error('I\'m running')
			# do something as your wish
			time.sleep(1)
	
	def stop(self):
		self.logger.info('Simple service will stop.')
		self.running = False

basepath = os.path.realpath(os.path.dirname(__file__)) + "/../"

if __name__ == '__main__':
	# 命令行参数解析，默认解析'-d'，即指定该模块的运行时目录
	ap = argparse.ArgumentParser(description = 'simple service')
	ap.add_argument('-d', '--executeDir', type = str,
			help = 'simple service execute directory',
			default = basepath)

	args = ap.parse_args()
	print 'Run simple service at %s' % args.executeDir
	os.chdir(args.executeDir)

	# 如果需要用到Django，取消以下注释，并在conf目录中增加Django相关的配置setting.py
	# sys.path.append('conf')
	# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings")

	# 读取项目的配置，包括模块自身的基本配置，日志模块配置等
	print 'Load logging config...'
	logging.config.fileConfig(os.path.join(args.executeDir, 'conf/simple.logging.cfg'))
	# simple service config
	print 'Load simple service config...'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(os.path.join(args.executeDir, 'conf/service.cfg'))

	# Let's rock 'n roll!
	SimpleService(cfg).run()

# vim: set noexpandtab ts=4 sts=4 sw=4 :
