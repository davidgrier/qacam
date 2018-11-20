# -*- coding: utf-8 -*-

from collections import deque
import importlib
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class TaskManager(object):

    def __init__(self, parent):
        self.parent = parent
        self.task = None
        self.queue = deque()

    def handletask(self):
        if self.task is None:
            try:
                self.task = self.queue.popleft().setup()
            except IndexError:
                self.parent.scanner.finished.disconnect(self.handletask)
                return
        self.task.setup(parent)

    def registertask(self, task):
        '''Place named task into the task queue
        '''
        if isinstance(task, str):
            try:
                taskmodule = importlib.import_module('tasks.' + task)
                taskclass = getattr(taskmodule, task)
                task = taskclass(parent=self.parent)
            except ImportError as err:
                msg = 'Could not import {}: {}'
                logger.error(msg.format(task, err))
                return
        self.queue.append(task)
        self.handletask()
