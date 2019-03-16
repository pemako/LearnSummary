# -*- coding:utf-8 -*-
# 2018-01-24 12:26:52

# 改变对象的字符串显示，可以从新定义它的 __str__() 和 __repr__() 方法


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(repr(p))
print(p)
