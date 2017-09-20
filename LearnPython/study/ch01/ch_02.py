#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 获取用户输入 input / raw_input

if __name__ == '__main__':
    name = input("Please input your name: ")
    # 如果直接输入 如 pemako 程序会报错，因为 input 会假设用户输入的是合法的
    # python 表达式，如果以字符串作为输入的名字，程序执行没有问题。
    print name 

    # raw_input 会把所有的输入当做原始数据，然后将其保存到字符串中，不会有上
    # 述的问题
    age = raw_input("Please input your age: ")
    print age
