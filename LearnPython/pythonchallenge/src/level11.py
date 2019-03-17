# -*- coding:utf-8 -*-
# 2019/03/17 12:46:00

'''
url: http://www.pythonchallenge.com/pc/return/5808.html 查看图片这么模糊信息
应该隐藏在图片中，对图片进行处理

'''


from PIL import Image


if __name__ == '__main__':
    #url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
    im = Image.open('data/cave.jpg')
    w, h = im.size
    print(w, h)
    for i in range(w):
        for j in range(h):
            if (i + j) % 2 == 1:
                im.putpixel((i, j), 0)
    im.save('data/cave2.png')  # 查看图片信息 evil 右上角
