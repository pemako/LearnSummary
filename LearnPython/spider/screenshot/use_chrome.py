#! -*- coding:utf-8 -*-

"""
如果使用 chrome 浏览器的进行模拟手机样式，可以通过以下方法进行设置
1. 设置 device name 确定要模拟的手机样式
2. 指定分辨率以及 UA 标识

使用 chrome 的时候在进行屏幕定位截图图片的时候出现截取位置不对，目前测试发现可能的原因
1. 打开站点是 pc 站识别后重新加载为手机站，进行延迟定时不起作用
2. 页面顶部有可关闭的导航条，需先关闭在进行位置确定

下面两个测试截取到的图片位置均不对，还是 PhantomJS 效果比较好
"""

import os

from PIL import Image
from selenium import webdriver

CHROMEDRIVER_PATH = "/Users/lena/Desktop/bin/chromedriver"

def driver_set_device_name():
    mobileEmulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    return driver

def driver_set_ua():
    mobileEmulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, 
                              chrome_options=options, 
                              service_log_path=os.path.devnull)
    driver.set_window_size(360, 640) # 将浏览器窗口设置为相同大小
    return driver

def screenshot(driver):
    driver.get("https://www.baidu.com/")

    driver.save_screenshot('./imgs/chrome_baidu.png')

    baidu = driver.find_element_by_id('logo')
    left = baidu.location['x']
    top = baidu.location['y']
    elementWidth = baidu.location['x'] + baidu.size['width']
    elementHeight = baidu.location['y'] + baidu.size['height']
    picture = Image.open('./imgs/chrome_baidu.png')

    picture = picture.crop((int(left), int(top), int(elementWidth), int(elementHeight)))
    picture.save('./imgs/chrome_baidu_logo.png')

    driver.quit()


if __name__ == "__main__":
    screenshot(driver_set_device_name())
    #screenshot(driver_set_ua())
