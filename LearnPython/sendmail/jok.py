#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys
import os
import time
import random
import base64
import requests
from sendmail import SmtpEmailTool


class BaseImg(object):
    def __init__(self, url):
        response = requests.get(url)
        self.uri = ("data:" + response.headers['Content-Type'] +
                    ";" + "base64," + base64.b64encode(response.content))

    def uri(self):
        return self.uri


class Jok(object):
    def __init__(self, time="2015-07-10", page=1, maxResult=20):
        self.base_url = "http://route.showapi.com/341-%s?showapi_appid=26265&showapi_sign=65fe84a00c16484d8e1988c3715eefc0&time=%s&page=%s&maxResult=%s"
        self.time = time
        self.page = page
        self.maxResult = maxResult
        self.con = {}

    def text_jok(self):
        text_con = []
        url = self.base_url % (1, self.time, self.page, self.maxResult)
        con = json.load(urllib2.urlopen(url))[
            'showapi_res_body']['contentlist']
        num = int(random.uniform(0, len(con)))
        return con[num]['text']

    def base_img(self, url):
        response = requests.get(url)
        basecon = ("data:" + response.headers['Content-Type'] +
                   ";" + "base64," + base64.b64encode(response.content))
        return basecon

    def img_jok(self):
        text_con = []
        url = self.base_url % (2, self.time, self.page, self.maxResult)
        con = json.load(urllib2.urlopen(url))[
            'showapi_res_body']['contentlist']
        num = int(random.uniform(0, len(con)))
        return self.base_img(con[num]['img'])

    def gif_jok(self):
        text_con = []
        url = self.base_url % (3, self.time, self.page, self.maxResult)
        con = json.load(urllib2.urlopen(url))[
            'showapi_res_body']['contentlist']
        num = int(random.uniform(0, len(con)))
        return self.base_img(con[num]['img'])

    def all(self):
        self.con['text'] = self.text_jok()
        self.con['img'] = self.img_jok()
        #self.con['gif'] = self.gif_jok()
        return self.con


if __name__ == "__main__":
    start = time.time()
    jok = Jok().all()
    # print jok['text']
    toAdd = ['731482121@qq.com', '']
    subject = u'每天一笑-20161027'
    #htmlText =u'<div><p><b>文字笑话</b></p>%(text)s</div><div><p><b>图片笑话</b></p><img src="%(img)s" /></div><div><p><b>动态图片</b></p><src="%(gif)s"></div>' % jok
    htmlText = u'<div><p><b>文字笑话</b></p>%(text)s</div><div><p><b>图片笑话</b></p><img src="%(img)s" /></div><div>' % jok

    emailTools = SmtpEmailTool(
        server='smtp.126.com',
        user='',
        password="")

    emailTools.sendEmail(toAdd, subject, htmlText)
    end = time.time()
    print end - start
