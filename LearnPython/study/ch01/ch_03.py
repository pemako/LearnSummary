#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 值转为字符串的两种机制，也可以通过下面两个函数来使用者两种机制
# 1、通过 str 函数，他会把值转为合理形式的字符串，便于用户理解
# 2、通过 repr 函数，他会创建一个字符串，以合法的 python 表达式
# 来表示

if __name__ == '__main__':
    print repr("Hello, world!")
    print repr(1000L)

    print str("Hello, world!")
    print str(1000L)
    
