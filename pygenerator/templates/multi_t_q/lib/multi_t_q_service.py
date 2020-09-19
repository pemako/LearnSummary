#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import pickle
import Queue
import signal
import threading
import time

from custom_tast.processor import TaskProcessor
from custom_tast.task import Task


class Multi_t_qService(object):
    """MultiTQ Service"""

    def __init__(self, cfg, execute_dir):
        self.logger = logging.getLogger('multi_t_q')
        self.cfg = cfg
        self.execute_dir = execute_dir
        # worker
        self.running = False
        self.worker_mum = self.cfg.getint('default', 'service.workers')
        self.worker_threads = []
        # task conf
        task_queue_max = self.cfg.getint('task', 'task.queue.max')
        self.retry_num = self.cfg.getint('task', 'task.retry.num')
        self.retry_interval = self.cfg.getint('task', 'task.retry.interval')
        self.task_queue = Queue.Queue(maxsize=task_queue_max)
        self.failed_queue = Queue.Queue()  # 失败任务追加到这个中
        self.task_processor = TaskProcessor()

    def __init_signal_handler(self):
        """删除不需要处理的信号，以及增加需要处理的信号,并且设置不同的处理方法
        这里默认处理了SIGTERM和SIGINT，并且尝试停止service
        SIGINT = 2，可使用kill -2 pid 或 当CTRL+C终止程序时发出
        SIGTERM = 15，可使用kill -15 pid发出
        """
        signals = (signal.SIGTERM, signal.SIGINT)
        self.signal_handlers = {}
        for sig in signals:
            self.signal_handlers[sig] = signal.getsignal(sig)
            signal.signal(sig, self.handle_signal)
        self.logger.info('Init signal handler')

    def handle_signal(self, signal, frame):
        self.logger.info('Handle signal %d, stop service', signal)
        self.logger.info('Try to stop all workers.')
        self.stop()
        self.logger.info('Bye-bye.')

    def work_main(self):
        while self.running:
            # Queue的get是同步的，queue里空的话会阻塞，需要get_nowait或get(False)，empty时会抛异常
            try:
                s = time.time()
                task = self.task_queue.get_nowait()
                # 这里要进行存储失败重试
                # 并且当达到重试上限时，将该记录加入失败列表并在“合适的”时机重试
                retry_time = 0
                while True:
                    if self.task_processor.process(task):
                        self.logger.info('Done processing task: %s', task)
                        break
                    else:
                        if retry_time >= self.retry_num:
                            self.failed_queue.put(task)
                            self.logger.error('Retry max time, save task into failed list')
                            break
                        retry_time += 1
                        time.sleep(self.retry_interval)
                        self.logger.debug('Retry process task: %s', task)
                self.logger.debug('Process cost: %f ms', (time.time() - s) * 1000)
            except Queue.Empty, empty:
                # 队列是空的，说明任务不繁重，让CPU休息一会儿吧
                # self.logger.debug('Task queue is empty')
                time.sleep(1)
                pass
            except Exception, e:
                self.logger.error('Unknown error: %s', e)
        self.logger.info('Thread %d exits', threading.current_thread().ident)

    def run(self):
        self.logger.info('MultiTQ service starts to run.')
        self.running = True
        self.__init_signal_handler()
        self.__create_workers()
        self.__main_thread_prepare()
        self.__main_thread_working()
        self.__wait_for_workers()
        self.__do_cleanup()

    def __create_workers(self):
        """创建工作线程"""
        for i in range(self.worker_mum):
            t = threading.Thread(target=self.work_main)
            t.start()
            self.worker_threads.append(t)
            self.logger.info('Thread %d is created', t.ident)

    def __main_thread_prepare(self):
        # 将本地已有的todo file load进来处理
        todo_list = self.__load_from_todo_file()
        self.logger.info('Load %d todo from file', len(todo_list))
        # 批量put到task queue，由于queue设置了上限，如果todo的比较多的话
        # 可能会阻塞在这里，直到todo都put完了，才能读标准输入处理新的
        for todo in todo_list:
            self.task_queue.put(item=todo, block=True)
        # 确保都put进去了之后，删掉dump的file
        try:
            os.remove(self.__get_todo_file_path())
        except Exception, e:
            self.logger.debug('Remove todo file error: %s', e)

    def __main_thread_working(self):
        while self.running:
            try:
                task = Task()
                # TODO
                # processTarget即需要被处理的实例
                # 例如通过logtailer读入thrift结构体，赋值给processTarget
                # 然后这个文件可以不用改了
                # 在custom_tast.processor.task_processor中实现具体的处理方法
                task.processTarget = int(time.time())

                time.sleep(1)  # 这个sleep是demo用，可去掉

            # 当使用logtailer做标准输入读取时，取消以下注释
            # except EOFError, eof:
            # 	self.logger.info('Read EOF, stop reading and exiting')
            # 	self.running = False
            # 	break
            except Exception, e:
                self.logger.error('Create task error: %s', e)
            else:
                # 这里如果queue满了，会阻塞
                self.task_queue.put(item=task, block=True)
                self.logger.debug('Put new task into queue')

    def __wait_for_workers(self):
        """该方法阻塞直到所有worker线程退出"""
        while True:
            alive = False
            for t in self.worker_threads:
                alive = alive or t.isAlive()
            if not alive:
                break

    def __do_cleanup(self):
        """做些进程结束前的清理工作"""
        self.logger.info("Cleanup...")
        # 此时queue中可能还会有一些待处理的
        # 同时还会有失败列表里的，需要合并成为todo list
        # 然后dump到本地，在下次启动时加载进task queue重新处理
        todo_list = []
        remain_task_list = list(self.task_queue.queue)
        failed_task_list = list(self.failed_queue.queue)
        todo_list.extend(remain_task_list)
        todo_list.extend(failed_task_list)
        self.logger.debug('Final todo task list: %s', todo_list)
        # 将所有此次生命周期没有完成的任务dump到本地，下次启动或直接手动处理
        self.__dump_todo_file(todo_list)

    def __dump_todo_file(self, todo):
        try:
            with open(self.__get_todo_file_path(), 'wb') as fd:
                pickle.dump(todo, fd)
        except Exception, e:
            self.logger.debug('Dump todo file error: %s', e)

    def __load_from_todo_file(self):
        todo = []
        try:
            with open(self.__get_todo_file_path(), 'rb') as fd:
                todo = pickle.load(fd)
        except Exception, e:
            self.logger.debug('Load todo file error: %s', e)
        return todo

    def __get_todo_file_path(self):
        todo_file = self.cfg.get('task', 'task.todo_file')
        path = os.path.join(self.execute_dir, 'data', todo_file)
        return path

    def stop(self):
        self.logger.info('MultiT service will stop.')
        self.running = False
