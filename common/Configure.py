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

    Methods
    -------
    timestamp() : str
        Returns a string representation of the current time.
    filename([prefix], [suffix]) : str
        Returns a string intended for use as a filename.
    configname(object) : str
        Returns the filename for a configuration file.
    save(object) :
        Save the configuration of a specified object.
    restore(object) :
        Read configuration and set properties of object.
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
        '''Returns string representing the current date and time'''
        return datetime.now().strftime('_%Y%b%d_%H%M%S')

    def filename(self, prefix='qacam', suffix=None):
        '''Returns a file name, including timestamp

        Arguments
        ---------
        prefix : str, optional
            String prefix for the filename.
            Default: qacam
        suffix : str, optional
            String suffix to append to filename.
            Default: None
        '''
        return os.path.join(self.datadir,
                            prefix + self.timestamp() + suffix)

    def configname(self, object):
        '''Returns name of configuration file based on class of objects

        Parameters
        ----------
        object : object
            Configuration file is named based on class name of objects

        Returns
        -------
        configname : str
            File name for configuration file

        '''
        classname = object.__class__.__name__
        return os.path.join(self.configdir, classname + '.json')

    def save(self, object):
        '''Save configuration of object as json file

        Parameters
        ----------
        object : object
            Object must have settings property, which provides
            a dictionary of parameters to be saved.
        '''
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
        '''Restore object configuration from json file

        Parameters
        ----------
        object : object
            Reads configuration for object from a configuration file
            based on the object class name
        '''
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
