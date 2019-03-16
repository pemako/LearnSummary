# -*- coding:utf-8 -*-
# 2018-01-25 11:31:57

"""你想定义某些在属性赋值上面有限制的数据结构"""

__author__ = "pemakoa@gmail.com"


class Descriptor:
    """Base class. Uses a descriptor to set a value"""

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    """Descriptor for enforcing types"""
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    """Descriptor for enforcing values"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected > 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be <' + str(self.size))
        super().__set__(instance, value)
