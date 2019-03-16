# -*- coding:utf-8 -*-
# 2018-01-24 17:50:34

# 你想定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法
# 使用 abc 模块可以很轻松的定义抽象基类

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

# 抽象类不能直接实例化
# 抽象类的目的就是让别的类继承它并实现特定的抽象方法


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

# 抽象类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass
