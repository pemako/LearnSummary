#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字典的方法

# clear() 清空所有的信息
d = {'name':'pemako', 'age':20}
print d.clear() #None 
print d

# copy() 得到一个字典的复本
# 当在副本中替换值得时候，原始字典不受影响，但是，如果修改了么讴歌值（原地修改）
# 而不是替换，原始的字典也会改变，因为同样的值也存储在原字典中
# 避免这个问题的一种方法就是使用深复制（deep copy）,可以使用 copy 的 deepcopy模块
x = {'username':'admin', 'machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'pemako'
y['machines'].remove('bar')
print x, y

from copy import deepcopy
d = {}
d['name'] = ['pemako', 'lena']
c = d.copy()
dc = deepcopy(d)
d['name'].append('jeffery')

print '--' * 20
print d
print c
print dc

print '--'* 20
# fromkeys 方法使用给定的健建立新的字典，每个健都对应一个默认值 None
# 如果不想使用默认值 None 可以指定默认值
print {}.fromkeys(['name','age'])
print {}.fromkeys(('name','age'))
print {}.fromkeys({'name','age'})
print {}.fromkeys(['name','age'],'unknow')

# get 方法 如果查找一个不存在的健时，不报错默认返回 None，可以指定默认值
print {}.get('name')
print {}.get('name', 'pemako')


