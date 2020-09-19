#! -*- coding:utf-8 -*-

"""
进行屏幕局部截取
"""

import os
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == "__main__":
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
    )
    driver = webdriver.PhantomJS(desired_capabilities=dcap, service_log_path=os.path.devnull)

    driver.get("http://www.baidu.com")
    driver.save_screenshot('./imgs/phantomjs_baidu.png')

    baidu = driver.find_element_by_id('logo')
    left = baidu.location['x']
    top = baidu.location['y']
    elementWidth = baidu.location['x'] + baidu.size['width']
    elementHeight = baidu.location['y'] + baidu.size['height']

    print "left:{}, top:{}, elementWidth:{}, elementHeight:{}".format(left, top, elementWidth, elementHeight)

    picture = Image.open('./imgs/phantomjs_baidu.png')
    picture = picture.crop((int(left), int(top), int(elementWidth), int(elementHeight)))

    picture.save('./imgs/phantomjs_baidu_logo.png')
    driver.quit()
