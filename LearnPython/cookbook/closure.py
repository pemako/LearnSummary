# -*- coding:utf-8 -*-
# 2018-01-23 18:29:24

import sys
from timeit import timeit


class ClosureInstance(object):
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # update instance dictionray with callables
        self.__dict__.update((key, value) for key, value in locals.items())

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    """this is docting"""
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


class Stack2(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


s = Stack()
timeit('s.push(1);s.pop()', 'from __main__ import s')

s = Stack2()
timeit('s.push(1);s.pop()', 'from __main__ import s')
