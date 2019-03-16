#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @create 17/11/28 14:25:29
# @author pemakoa@gmail.com

import time
from random import random
from threading import Semaphore, Thread

sema = Semaphore(2)
threads = []

def foo(tid):
    with sema:
        print '{} acquire sema'.format(tid)
        wt = random() * 2
        time.sleep(wt)
    print '{} release sema'.format(tid)


for i in range(5):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
