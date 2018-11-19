# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (
    QWidget, QComboBox, QSpinBox, QDoubleSpinBox, QPushButton)
import inspect

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class QSettingsWidget(QWidget):
    """A glue class that connects a GUI with a device"""

    def __init__(self, parent=None, device=None, ui=None):
        super(QSettingsWidget, self).__init__(parent)
        self.ui = ui
        self.ui.setupUi(self)
        self._properties = []
        self.device = device

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        if device is None:
            self.setEnabled(False)
            self._device = None
            return
        if hasattr(self, 'device'):
            self.disconnectSignals()
        self._device = device
        self.getProperties()
        self.configureUi()
        self.updateUi()
        self.connectSignals()
        self.setEnabled(True)
        logger.info('device connected')

    def set(self, name, value):
        '''Set parameter on both device and UI

        Parameters
        ----------
        name : string
            Name of property
        value : scalar
            Value of property
        '''
        if name in self.properties:
            self.setDeviceProperty(name, value)
            self.setUiProperty(name, value)
        else:
            logger.warning('unknown property: {}'.format(name))

    def get(self, name):
        '''Return value from device (and UI)

        Parameters
        ----------
        name : string
            Name of property

        Returns
        -------
        value : scalar
            Value of property
        '''
        if name in self.properties:
            return getattr(self.device, name)
        else:
            logger.warning('unknown property: {}'.format(name))

    def setDeviceProperty(self, name, value):
        """Set device property and wait for operation to complete"""
        if hasattr(self.device, name):
            setattr(self.device, name, value)
            logger.info('Setting {}: {}'.format(name, value))
            while self.device.busy():
                if self.device.error:
                    logger.warn('device error')

    def setUiProperty(self, name, value):
        wid = getattr(self.ui, name)
        if isinstance(wid, QDoubleSpinBox):
            wid.setValue(value)
        elif isinstance(wid, QSpinBox):
            wid.setValue(value)
        elif isinstance(wid, QComboBox):
            wid.setCurrentIndex(value)
        elif isinstance(wid, QPushButton):
            pass
        else:
            logger.warn('Unknown property: {}: {}'.format(name, type(wid)))

    @property
    def settings(self):
        values = dict()
        for prop in self.properties:
            value = getattr(self.device, prop)
            if not inspect.ismethod(value):
                values[prop] = value
        return values

    @settings.setter
    def settings(self, values):
        for name in values:
            self.setDeviceProperty(name, values[name])
        self.updateUi()

    @property
    def properties(self):
        return self._properties

    def getProperties(self):
        """valid properties appear in both the device and the ui"""
        dprops = [name for name, _ in inspect.getmembers(self.device)]
        uprops = [name for name, _ in inspect.getmembers(self.ui)]
        props = [name for name in dprops if name in uprops]
        self._properties = [name for name in props if '_' not in name]
        logger.debug(self._properties)

    def configureUi(self):
        logger.debug('configureUi should be overridden')

    @pyqtSlot()
    def updateUi(self):
        """Update widgets with current values from device"""
        for prop in self.properties:
            val = getattr(self.device, prop)
            self.setUiProperty(prop, val)

    @pyqtSlot(int)
    @pyqtSlot(float)
    def updateDevice(self, value):
        name = str(self.sender().objectName())
        self.setDeviceProperty(name, value)

    @pyqtSlot(bool)
    def autoUpdateDevice(self, flag):
        autosetproperty = self.sender.objectName()
        autosetmethod = getattr(self.device, autosetproperty)
        autosetmethod()
        while self.device.busy():
            if self.device.error:
                logger.warn('device error')
        self.updateUi

    def connectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            if isinstance(wid, QDoubleSpinBox):
                wid.valueChanged.connect(self.updateDevice)
            elif isinstance(wid, QSpinBox):
                wid.valueChanged.connect(self.updateDevice)
            elif isinstance(wid, QComboBox):
                wid.currentIndexChanged.connect(self.updateDevice)
            elif isinstance(wid, QPushButton):
                wid.clicked.connect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))

    def disconnectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            if isinstance(wid, QDoubleSpinBox):
                wid.valueChanged.disconnect(self.updateDevice)
            elif isinstance(wid, QSpinBox):
                wid.valueChanged.disconnect(self.updateDevice)
            elif isinstance(wid, QComboBox):
                wid.currentIndexChanged.disconnect(self.updateDevice)
            elif isinstance(wid, QPushButton):
                wid.clicked.disconnect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))
