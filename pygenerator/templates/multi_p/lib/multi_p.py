#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import ConfigParser
import logging.config
import os
import sys

from multi_p_service import Multi_pService

# 获取默认的运行时路径，并设置运行时需要加到sys.path的模块
exepath = os.path.realpath(os.path.dirname(__file__))
basepath = os.path.realpath(os.path.dirname(__file__) + '/../')
sys.path.append(exepath)

if __name__ == '__main__':
    # 命令行参数解析，默认解析'-d'，即指定该模块的运行时目录
    ap = argparse.ArgumentParser(description='multi_p service')
    ap.add_argument('-d', '--execute_dir', type=str,
                    help='multi_p service execute directory',
                    default=basepath)
    args = ap.parse_args()
    print 'Run multi_p service at %s' % args.execute_dir
    os.chdir(args.execute_dir)

    # 如果需要用到Django，取消以下注释，并在conf目录中增加Django相关的配置setting.py
    # sys.path.append('conf')
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings")

    # 读取项目的配置，包括模块自身的基本配置，日志模块配置等
    # logging config
    print 'Load logging config...'
    logging.config.fileConfig(os.path.join(args.execute_dir, 'conf/multi_p_logging.cfg'))
    # multi_p service config
    print 'Load multi_p service config...'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(os.path.join(args.execute_dir, 'conf/multi_p_service.cfg'))

    # Let's rock 'n roll!
    Multi_pService(cfg, args.execute_dir).run()
