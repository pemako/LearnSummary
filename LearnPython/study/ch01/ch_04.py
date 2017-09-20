#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 原始字符串 在字符串的前面加上 r ,捕获把反斜线当做特殊字符串，在
# 原始字符串中输入的每个字符都会与书写的方式保持一致。不能在原始
# 字符串的末尾添加反斜线，不然 python 就不清楚何时应该结束字符串

# Unicode 字符串，在字符前面加上 u 在 python3中所有字符串均为unicode

if __name__ == '__main__':
    print r'C:\nowhere'
    print 'C:\nowhere'
    #print r'C:\nowhere\' # 错误写法

    print u'Hello, world!'
