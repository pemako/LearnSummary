# -*- coding:utf-8 -*-
# 2019/03/16 17:27:00

'''
url: http://www.pythonchallenge.com/pc/def/equality.html
根据提示“One small letter, surrounded by EXACTLY three big bodyguards
on each of its sides.”  除了这个没有任何信息，思考上一题查看页面源码
发现也是有一大段的注释内容。按照该思路进行解析 获取字符 linkedlist
'''


if __name__ == '__main__':
    import re
    import urllib.request
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    res = urllib.request.urlopen(url).read().decode('utf-8')
    r = ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', res))
    print(r)  # linkedlist
