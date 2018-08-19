# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QWidget, QComboBox, QSpinBox, QDoubleSpinBox, QPushButton)
import inspect

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


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
            self.properties = []
            logger.info('device disconnected')
        self._device = device
        self.getProperties()
        self.configureUi()
        self.updateUi()
        self.connectSignals()
        self.setEnabled(True)
        logger.info('device connected')

    @property
    def properties(self):
        return self._properties

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
            if hasattr(self.device, name):
                setattr(self.device, name, values[name])
        self.updateUi()

    def getProperties(self):
        """valid properties appear in both the device and the ui"""
        dprops = [name for name, _ in inspect.getmembers(self.device)]
        uprops = [name for name, _ in inspect.getmembers(self.ui)]
        props = [name for name in dprops if name in uprops]
        self._properties = [name for name in props if '_' not in name]

    def configureUi(self):
        pass

    @QtCore.pyqtSlot()
    def updateUi(self):
        """Update widgets with current values from device"""
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            val = getattr(self.device, prop)
            if isinstance(wid, QDoubleSpinBox):
                wid.setValue(val)
            elif isinstance(wid, QSpinBox):
                wid.setValue(val)
            elif isinstance(wid, QComboBox):
                wid.setCurrentIndex(val)
            elif isinstance(wid, QPushButton):
                continue
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))

    @QtCore.pyqtSlot(object)
    def updateDevice(self, value):
        name = str(self.sender().objectName())
        setattr(self.device, name, value)

    @QtCore.pyqtSlot(bool)
    def autoUpdateDevice(self, flag):
        autosetproperty = self.sender.objectName()
        autosetmethod = getattr(self.device, autosetproperty)
        autosetmethod()
        QtCore.QTimer.singleShot(1000., self.updateUi)

    def connectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            if isinstance(wid, QDoubleSpinBox):
                wid.valueChanged[QtCore.double].connect(self.updateDevice)
            elif isinstance(wid, QSpinBox):
                wid.valueChanged[int].connect(self.updateDevice)
            elif isinstance(wid, QComboBox):
                wid.currentIndexChanged[int].connect(self.updateDevice)
            elif isinstance(wid, QPushButton):
                wid.clicked.connect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))

    def disconnectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            if isinstance(wid, QDoubleSpinBox):
                wid.valueChanged[QtCore.double].disconnect(self.updateDevice)
            elif isinstance(wid, QSpinBox):
                wid.valueChanged[int].disconnect(self.updateDevice)
            elif isinstance(wid, QComboBox):
                wid.currentIndexChanged[int].disconnect(
                    self.updateDevice)
            elif isinstance(wid, QPushButton):
                wid.clicked.disconnect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))
