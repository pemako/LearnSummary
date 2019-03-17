# -*- coding:utf-8 -*-
# 2019/03/17 01:01:00

'''
url: http://www.pythonchallenge.com/pc/def/oxygen.html 查看该页面图片上有
一行信息被添加上了水印，目标去除水印 也许就可以获取需要的信息

'''

import urllib.request
from PIL import Image

if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    request = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    image = Image.open(response)
    w, h = image.size  # 629 95
    # (115, 115, 115, 255) 如果图是一个多层图像返回的是一个元祖
    print(image.getpixel((0, h / 2)))
    # print(w, h, image.__dict__)

    s = ''.join(chr(image.getpixel((i, h / 2))[0]) for i in range(0, w, 8))
    # smartguy, yo made i. the nxt leve is [10, 110, 16, 101 103, 14, 105,116,
    # 12]reb
    print(s)
    s = ''.join(chr(image.getpixel((i, h / 2))[0]) for i in range(0, w, 7))
    # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114,
    # 105, 116, 121]pe_
    print(s)

    print(''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])))
    # integrity
