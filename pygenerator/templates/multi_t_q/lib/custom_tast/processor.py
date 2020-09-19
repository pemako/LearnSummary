#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


class TaskProcessor(object):
    def __init__(self):
        self.logger = logging.getLogger('multi_t_q')

    def process(self, task):
        '''Process task and return False if the processing is failed and another retry is needed.
        Otherwise return True.'''
        data_object = task.process_target

        # TODO process the task in your own way
        self.logger.debug("Hey look! I'm processing this one: {}".format(data_object))

        return True
