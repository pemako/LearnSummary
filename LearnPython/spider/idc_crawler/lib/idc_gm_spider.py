# -*- coding: utf-8 -*-

import httplib
import os
import threading
import time
import traceback
from collections import namedtuple
from urllib2 import HTTPError
from urllib2 import URLError

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

Product = namedtuple('Product', ['gid', 'pid', 'url'])

BASE_URL = 'https://m.gome.com.cn'
SLEEP_ONE_SECOND = 1
SLEEP_HALF_SECOND = 0.5
CRAWLER_NUM = 3 # 第几次抓取

XPATH = {
    'goods_list': '//li[@class="gd_list"]',
    'goods_href': './/a[@onclick="urlClick(this)"]',
    'goods_params': './/a[@onclick="urlClick(this)"]',
    'warpper_imgs': '//ul[@class="swiper-wrapper see_details"]/li/a/img',
    'price': '//span[@v="all_0"]',
    'addesc': '//p[@i="stock_adDescIndex"]',
    'title': '//div[@class="title"]/div/h1',
    'evaluate': '//span[@v="allNum"]',
    'groupon_price': '//span[@v="price_0"]',
    'good_comment': '//span[@v="goodNum"]',
    'click_evaluate': '//ul[@class="nav_list"]/li[3]',
    'evaluate_item_img': '//ul[@class="evaluate_nav_list flex1"]/li[5]',
    'evaluate_imgs': '//div[@class="evaluate_list_item"]/div[2]/ul/li/img',
    'gm_self_support': '//p[@class="tag"]',
}


def phantomjs_driver():
    global driver
    UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (UA)
    SERVICE_ARGS = ['--disk-cache=true', '--load-images=false']
    driver = webdriver.PhantomJS(service_args=SERVICE_ARGS, desired_capabilities=dcap, service_log_path=os.path.devnull)

    return driver


class IdcGmSpider(threading.Thread):
    def __init__(self, mysql, logger):
        super(IdcGmSpider, self).__init__()
        self.logger = logger
        self.mysql = mysql
        self.running = True

    def parse_goods(self, categorys):
        while self.running:
            self.logger.info('I\'m running')
            time.sleep(SLEEP_ONE_SECOND)
            self.logger.info("this categorys: %s", categorys)
            driver = phantomjs_driver()
            products_url = []
            for category in categorys:
                goods_url = ''.join([BASE_URL, category.url])
                driver.get(goods_url)
                goods_list = driver.find_elements_by_xpath(XPATH['goods_list'])
                for goods in goods_list:
                    _href = goods.find_element_by_xpath(XPATH['goods_href']).get_attribute('href')
                    _pid = _href.split('product-')[1].split('-')[0]
                    _params = goods.find_element_by_xpath(XPATH['goods_params']).get_attribute('params')
                    _product_url = '?'.join([_href, _params])
                    products_url.append(Product(category.id, _pid, _product_url))

            self.parse_product(products_url)
            driver.quit()
            self.logger.info('Thread %d exits', threading.current_thread().ident)

            self.running = False

    def __cureent_time(self):
        return int(time.time())

    def parse_product(self, products):
        driver = phantomjs_driver()

        def check_gm_self_support(xpath):
            """判断是否是京东自营"""
            try:
                driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return False
            return True

        def get_imgs_from_evaluate():
            """获取评论区有图的图片信息"""
            driver.find_element_by_xpath(XPATH['click_evaluate']).click()
            time.sleep(SLEEP_ONE_SECOND+SLEEP_HALF_SECOND)
            _have_imgs = driver.find_element_by_xpath(XPATH['evaluate_item_img']).text
            evaluate_img = []
            if "(0)" not in _have_imgs.encode('utf-8').strip():
                driver.find_element_by_xpath(XPATH['evaluate_item_img']).click()
                time.sleep(SLEEP_HALF_SECOND)
                driver.execute_script("document.body.scrollTo=3000")
                __evaluate_imgs = driver.find_elements_by_xpath(XPATH['evaluate_imgs'])
                for __evaluate_img in __evaluate_imgs:
                    evaluate_img.append(__evaluate_img.get_attribute('src'))
            return ','.join(evaluate_img)

        for product in products:
            try:
                self.logger.info("===> %s", product)
                __warpper_imgs = []
                driver.get(product.url)
                driver.execute_script("document.body.scrollTo=3000")

                groupon_price = driver.find_element_by_xpath(XPATH['groupon_price']).text
                imgs = driver.find_elements_by_xpath(XPATH['warpper_imgs'])
                for img in imgs:
                    __warpper_imgs.append(img.get_attribute('src'))

                price = driver.find_element_by_xpath(XPATH['price']).text
                addesc = driver.find_element_by_xpath(XPATH['addesc']).text
                title = driver.find_element_by_xpath(XPATH['title']).text
                evaluate = driver.find_element_by_xpath(XPATH['evaluate']).text
                good_comment = driver.find_element_by_xpath(XPATH['good_comment']).text

                gm_self_support = 0
                if check_gm_self_support(XPATH['gm_self_support']):
                    gm_self_support = 1

                product_info = {'gid': product.gid, 'pid': product.pid, 'img': ','.join(__warpper_imgs), 'title': title,
                                'addesc': addesc, 'price': price, 'evaluate': evaluate, 'groupon_price': groupon_price,
                                'good_comment': good_comment, 'create_time': self.__cureent_time(),
                                'last_update': self.__cureent_time(),
                                'cnum': CRAWLER_NUM, 'purl': product.url, 'evaluate_img': get_imgs_from_evaluate(),
                                'gm_self_support': gm_self_support}

                self.__insert(product_info)

            except httplib.BadStatusLine, e:
                self.logger.info('Error===> httplib.BadStatusLine err: %s', e)
                traceback.print_exc()
                continue
            except URLError, e:
                self.logger.info('Error===>urllib2.URLError err: %s', e)
                driver.quit()
                driver = phantomjs_driver()
                traceback.print_exc()
                continue
            except HTTPError, e:
                self.logger.info('Error===>HTTPError err: %s', e)
                traceback.print_exc()
                continue
            except Exception, e:
                self.logger.info('Error===>parse_product err: %s', e)
                traceback.print_exc()
                time.sleep(SLEEP_ONE_SECOND)
                continue
            except:
                traceback.print_exc()
                time.sleep(SLEEP_ONE_SECOND)
                pass

    def __insert(self, product_info):
        base = """
            INSERT INTO
                gm_goods_product (gid, pid, img, title, addesc, price, evaluate, groupon_price, good_comment, create_time, last_update, cnum, purl, evaluate_img, gm_self_support)
            VALUES
                (%(gid)s, "%(pid)s", "%(img)s", "%(title)s", "%(addesc)s", "%(price)s", "%(evaluate)s", "%(groupon_price)s", "%(good_comment)s", "%(create_time)s", "%(last_update)s", %(cnum)s, "%(purl)s", "%(evaluate_img)s", %(gm_self_support)s) """
        try:
            sql = base % product_info
            self.logger.info(sql)
            self.mysql.execute(sql)
        except Exception as e:
            raise e