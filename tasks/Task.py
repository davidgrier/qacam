# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Task(object):

    def __init__(self,
                 parent=None):
        self.parent = parent
        self._done = False

    def setup(self):
        '''Set up before scan starts'''
        return self

    def finish(self):
        '''Perform tasks after scan is complete'''
        pass
