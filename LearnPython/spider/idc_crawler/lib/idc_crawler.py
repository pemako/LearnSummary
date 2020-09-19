# -*- coding: utf-8 -*-

import ConfigParser
import argparse
import logging.config
import os
import sys

from idc_crawler_service import IdcCrawlerService

exepath = os.path.realpath(os.path.dirname(__file__))
basepath = os.path.realpath(os.path.dirname(__file__) + '/../')
sys.path.append(exepath)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='idc_crawler service')
    ap.add_argument('-d', '--execute_dir', type=str,
                    help='idc_crawler service execute directory',
                    default=basepath)
    args = ap.parse_args()
    print 'Run idc_crawler service at %s' % args.execute_dir
    os.chdir(args.execute_dir)

    # 如果需要用到Django，取消以下注释，并在conf目录中增加Django相关的配置setting.py
    # sys.path.append('conf')
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings")

    print 'Load logging config...'
    logging.config.fileConfig(
        os.path.join(
            args.execute_dir,
            'conf/idc_crawler_logging.cfg'))
    print 'Load idc_crawler service config...'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(os.path.join(args.execute_dir, 'conf/idc_crawler_service.cfg'))

    IdcCrawlerService(cfg, args.execute_dir).run()
