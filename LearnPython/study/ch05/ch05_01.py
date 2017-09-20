#!/usr/bin/env python
# -*- coding: utf-8 -*-

# is 同一性运算符 和 == 并不相同
# 使用==运算符来判定两个对象是否相等，使用 is 判定两者是否等同（同一个对象）

# in 成员资格运算符

# 短路逻辑和条件表达式
# 断言 assert

age = 10
assert 0 < age < 11

x = 1
while x <= 100:
    print x
    x += 1

name = ''
while not name or name.isspace():
    name = raw_input('Please enter your name:')
print "Hello, %s !" % name
