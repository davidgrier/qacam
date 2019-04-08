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
        self.parent.scanner.finished.connect(self.handletask)

    def handletask(self):
        if self.parent.scanner.running():
            return
        if self.task is None:
            if len(self.queue) == 0:
                return
            self.task = self.queue.popleft().setup()
            self.parent.ui.scan.animateClick(100)
        else:
            self.task.finish()
            self.task = None
            self.handletask()

    def registertask(self, task, **kwargs):
        '''Place named task into the task queue
        '''
        if isinstance(task, str):
            try:
                taskmodule = importlib.import_module('tasks.' + task)
                taskclass = getattr(taskmodule, task)
                task = taskclass(parent=self.parent, **kwargs)
            except ImportError as err:
                msg = 'Could not import {}: {}'
                logger.error(msg.format(task, err))
                return
        self.queue.append(task)
        self.handletask()
