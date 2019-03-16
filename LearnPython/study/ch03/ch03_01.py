#!/usr/bin/evn python
# -*- coding: utf-8 -*-

# string 串 find 查抄字符串中是否的子串的位置，返回找到的位置
# 如果没有找到 返回-1
import string
# translate 在使用的时候需要先指定一个转换表
# 转换表的关系是以某个字符替换为对应字符的关系
# 如需要把c->k ， s->z ，在 string 模块中使用
# maketrans 函数就行
# 转换表是包含替换 ASICC 字符集中256个字符的替
# 换字母的字符串
from string import maketrans

streg = "This is a example string"
print streg.find('a', 0, 2)
print string.find(streg, 'a')
print string.find(streg, 'e', 0, 20)
print string.find(streg, 'e', 0, 7)

# 错误，join 的序列必须是字符串
listreg = [1, 2, 3, 4]
sep = '+'
#print sep.join(listreg)

listreg = ['1','2','3','4']
print '+'.join(listreg)

print streg.lower()
# 每个单词的首字母大写
print string.capwords(streg)

# repace 第一个为 old字符串，第二个为需要替换成新的值，第三个为最大替换几个
# 默认我 -1 全部替换
print streg.replace("is", "pemako", 1)

# splict
print string.split(streg, ' ')
print streg.split(' ')

# strip 去除字符串两端的空格
print " this is  ".strip()

table = maketrans('cs', 'kz')
print len(table)
print table
print table[97:123]

# 创建这个表之后，可以将它作用 translate 方法的参数，进行字符串的替换
print "this is an incredible test".translate(table) # thiz iz an inkredible tezt
# translate 第二个参数是可选的，这个参数是指定需要删除的字符
print "this is an incredible test".translate(table, " ")
