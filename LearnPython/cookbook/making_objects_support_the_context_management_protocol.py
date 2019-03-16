# -*- coding:utf-8 -*-
# 2018-01-24 12:47:46

# 让对象支持上线文管理协议(with语句)
# 需要实现 __enter__() 和 __exit__() 方法

from functools import partial
from socket import AF_INET, SOCK_STREAM, socket


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None



conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    # 当出现with语句的时候，对象的 __enter__()方法被触发，它返回的值(如果有的话)会被赋值给
    # as 声明的变量。然后，with语句块里面的代码开始执行，最后 __exit__()方法被触发清理工作
    print(s)
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    # conn.__exit__() executes: connection closed
