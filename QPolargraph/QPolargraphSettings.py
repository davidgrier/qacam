# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Polargraph_UI import Ui_Polargraph
from polargraph import polargraph
import inspect
import numpy as np

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class QPolargraphSettings(QtGui.QWidget):

    def __init__(self, parent=None, device=None):
        super(QPolargraphSettings, self).__init__(parent)
        self.ui = Ui_Polargraph()
        self.ui.setupUi(self)
        self._properties = []
        self.device = device

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        if hasattr(self, 'device') and self.device is not None:
            self.disconnectSignals()
            self._properties = []
            logger.info('polargraph hardware disconnected')
        if isinstance(device, polargraph):
            self._device = device
            self.getProperties()
            self.updateUi()
            self.connectSignals()
            logger.info('polargraph hardware connected')
        else:
            self._device = None

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

    def updateUi(self):
        # validate edit fields
        val = QtGui.QDoubleValidator(0.1, 5, 2, self.ui.L)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.L.setValidator(val)
        val = QtGui.QDoubleValidator(0.01, 0.5, 3, self.ui.y0)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.y0.setValidator(val)
        val = QtGui.QDoubleValidator(100, 1000, 0, self.ui.speed)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.speed.setValidator(val)
        val = QtGui.QDoubleValidator(0.01, 5, 2, self.ui.width)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.width.setValidator(val)
        val = QtGui.QDoubleValidator(0.01, 5, 2, self.ui.height)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.height.setValidator(val)

        # Update widgets with current values from device
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            val = getattr(self.device, prop)
            wid.setText(str(val))

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
    def updateDevice(self):
        wid = self.sender()
        name = str(wid.objectName())
        min = wid.validator().bottom()
        max = wid.validator().top()
        value = np.clip(float(wid.text()), min, max)
        setattr(self.device, name, value)

    def connectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            wid.textChanged.connect(self.checkInput)
            wid.editingFinished.connect(self.updateDevice)

    def disconnectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            wid.textChanged.disconnect(self.checkInput)
            wid.editingFinished.disconnect(self.updateDevice)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    try:
        device = polargraph()
    except ValueError:
        device = None
    wid = QPolargraphSettings(device=device)
    wid.show()
    sys.exit(app.exec_())
