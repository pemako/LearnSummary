#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list 详解 为内置的模块
# 列表进行 分片 / 支持步长 / 序列相加 / 乘法 / In 判断成员资格 
# max min len 最大 最小 长度

# cmp(x, y) 比较两个值
# len(seq) 返回序列的长度
# list(seq) 把序列转换成列表
# max(args) 
# min(args)
# reversed(seq) # 对序列进行反向迭代
# sorted(seq) 
# tuple(seq) 

if __name__ == '__main__':
    name = ['pemako', 'lena', 'coolena']
    name.append('jeffery')
    print name

    name.reverse()
    print name

    name.sort()
    print name

    name.remove('lena')
    print name

    print name.pop()
    print name

    name.insert(1, 'fang')
    print name

    print name.index('jeffery')

    name.extend(['aaa', 'bbb', 'bbb'])
    print name

    print name.count('bbb')
