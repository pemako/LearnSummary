#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 可以通过 dict 函数，通过其他映射（比如其他字典）或者
# （键值对）的系列建立字典

# 在地点中检查健的成员资格比在列表中检查值得成员资格更
# 高效，数据结构的规模越大，两者的效率差距越明显

items = [('name', 'pemako'), ('age', 20)]
d = dict(items)
print d

people = {
    'Alice': {
        'phone': '1234',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Name: ')
# 查找电话号码还是地址？
request = raw_input('Phone(p) or Address(a) ?')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# 如果名字是字典中的有效健才打印信息
if name in people: 
    print "%s's %s's is %s" % (name, labels[key], people[name][key])
