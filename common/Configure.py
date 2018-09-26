# -*- coding: utf-8 -*-

import json
import os
import io
import platform
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Configure(object):
    """Save and restore configuration of objects

    The configuration object also includes utility functions for
    standard timestamps and standard file names
    """

    def __init__(self, parent):
        self.parent = parent
        self.datadir = os.path.expanduser('~/data/')
        self.configdir = os.path.expanduser('~/.acam/')
        if not os.path.exists(self.datadir):
            logger.info('Creating data directory: {}'.format(self.datadir))
            os.makedirs(self.datadir)
        if not os.path.exists(self.configdir):
            logger.info(
                'Creating configuration directory: {}'.format(self.configdir))
            os.makedirs(self.configdir)

    def timestamp(self):
        return datetime.now().strftime('_%Y%b%d_%H%M%S')

    def filename(self, prefix='pyfab', suffix=None):
        return os.path.join(self.datadir,
                            prefix + self.timestamp() + suffix)

    def configname(self, object):
        """Configuration file is named for the class of the object."""
        classname = object.__class__.__name__
        return os.path.join(self.configdir, classname + '.json')

    def save(self, object):
        """Save configuration of object as json file"""
        settings = object.settings
        if len(settings) == 0:
            return
        configuration = json.dumps(settings,
                                   indent=2,
                                   separators=(',', ': '),
                                   ensure_ascii=False)
        filename = self.configname(object)
        with io.open(filename, 'w', encoding='utf8') as configfile:
            if platform.python_version().startswith('3.'):
                configfile.write(str(configuration))
            else:
                configfile.write(unicode(configuration))

    def restore(self, object):
        """Restore object's configuration from json file"""
        try:
            filename = self.configname(object)
            logger.info('Configuring {}'.format(filename))
            configuration = json.load(io.open(filename))
            object.settings = configuration
        except IOError as ex:
            msg = ('Could not read configuration file:\n\t' +
                   str(ex) +
                   '\n\tUsing default configuration.')
            logger.warning(msg)

    def query_save(self, object):
        query = 'Save current configuration?'
        reply = QMessageBox.question(self.parent,
                                     'Confirmation',
                                     query,
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save(object)
        else:
            pass
