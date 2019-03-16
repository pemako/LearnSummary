# -*- coding:utf-8 -*-
# 2018-01-22 10:52:27

# 你有一个除 __init__ 方法外只定义了一个方法的类。为了简化代码，可以把它转换为函数

from urllib.request import urlopen


class UrlTemplate(object):
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(name='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
