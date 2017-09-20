#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 循环遍历字典

d = {'x': 1, 'y':2, 'z':3}

for key in d:
    print key, 'corresponds to', d[key]

# 使用 d.items() 方法会将健值对作为元组返回
for key, value in d.items():
    print key, 'corresponds to', value
