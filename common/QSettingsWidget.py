# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import inspect
import numpy as np

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class QSettingsWidget(QtGui.QWidget):
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
            if isinstance(wid, QtGui.QLineEdit):
                wid.setText(str(val))
            elif isinstance(wid, QtGui.QSpinBox):
                wid.setValue(val)
            elif isinstance(wid, QtGui.QComboBox):
                wid.setCurrentIndex(val)
            elif isinstance(wid, QtGui.QPushButton):
                continue
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))

    @QtCore.pyqtSlot()
    def checkInput(self):
        wid = self.sender()
        state = wid.validator().validate(wid.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#ffffff'  # white
        elif state == QtGui.QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        wid.setStyleSheet('QLineEdit {background-color: %s}' % color)

    @QtCore.pyqtSlot()
    def updateDevice_edit(self):
        wid = self.sender()
        name = str(wid.objectName())
        if isinstance(wid, QtGui.QLineEdit):
            min = wid.validator().bottom()
            max = wid.validator().top()
            value = np.clip(float(wid.text()), min, max)
        setattr(self.device, name, value)

    @QtCore.pyqtSlot(int)
    def updateDevice_select(self, value):
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
            if isinstance(wid, QtGui.QLineEdit):
                wid.textChanged.connect(self.checkInput)
                wid.editingFinished.connect(self.updateDevice_edit)
            elif isinstance(wid, QtGui.QSpinBox):
                wid.valueChanged[int].connect(self.updateDevice_select)
            elif isinstance(wid, QtGui.QComboBox):
                wid.currentIndexChanged[int].connect(
                    self.updateDevice_select)
            elif isinstance(wid, QtGui.QPushButton):
                wid.clicked.connect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))

    def disconnectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            if isinstance(wid, QtGui.QLineEdit):
                wid.textChanged.disconnect(self.checkInput)
                wid.editingFinished.disconnect(self.updateDevice_edit)
            elif isinstance(wid, QtGui.QSpinBox):
                wid.valueChanged[int].disconnect(self.updateDevice_select)
            elif isinstance(wid, QtGui.QComboBox):
                wid.currentIndexChanged[int].disconnect(
                    self.updateDevice_select)
            elif isinstance(wid, QtGui.QPushButton):
                wid.clicked.disconnect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))
