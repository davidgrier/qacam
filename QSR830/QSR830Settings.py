from PyQt4 import QtGui, QtCore
from SR830Settings_UI import Ui_SR830Settings
from SR830 import SR830
import inspect
import numpy as np

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class QSR830Settings(QtGui.QWidget):

    def __init__(self, parent=None, device=None):
        super(QSR830Settings, self).__init__(parent)
        self.ui = Ui_SR830Settings()
        self.ui.setupUi(self)
        self._properties = []
        self.device = device

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        if hasattr(self, 'device'):
            self.diconnectSignals()
            self.properties = []
            logger.info('lockin amplifier disconnected')
        if isinstance(device, SR830):
            self._device = device
            self.getProperties()
            self.updateUi()
            self.connectSignals()
        else:
            logger.error('device is not an SR830...no lockin connected')
            self._device = None

    @property
    def properties(self):
        return self._properties

    def getProperties(self):
        """valid properties appear in both the device and the ui"""
        dprops = [name for name, _ in inspect.getmembers(self.device)]
        uprops = [name for name, _ in inspect.getmembers(self.ui)]
        props = [name for name in dprops if name in uprops]
        self._properties = [name for name in props if '_' not in name]

    def configureUi(self):
        # validate edit fields
        val = QtGui.QDoubleValidator(0.001, 102000., 3, self.ui.frequency)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.frequency.setValidator(val)
        val = QtGui.QDoubleValidator(0.004, 5, 3, self.ui.amplitude)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.amplitude.setValidator(val)
        val = QtGui.QDoubleValidator(-360., 729.99, 2, self.ui.phase)
        val.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.phase.setValidator(val)

        # Choice of source determines activity of widgets
        self.ui.source.currentIndexChanged[int].connect(
            lambda v: self.ui.frequency.setEnabled(bool(v)))
        self.ui.source.currentIndexChanged[int].connect(
            lambda v: self.ui.amplitude.setEnabled(bool(v)))
        self.ui.source.currentIndexChanged[int].connect(
            lambda v: self.ui.trigger.setDisabled(bool(v)))
        self.ui.frequency.setEnabled(bool(self.ui.source.currentIndex()))
        self.ui.amplitude.setEnabled(bool(self.ui.source.currentIndex()))
        self.ui.trigger.setDisabled(bool(self.ui.source.currentIndex()))

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

    @QtCore.pyqtSlot(name='updateDevice')
    def updateDevice_qlineedit(self):
        wid = self.sender()
        name = wid.objectName()
        if isinstance(wid, QtGui.QLineEdit):
            min = wid.validator().bottom()
            max = wid.validator().top()
            value = np.clip(float(wid.text()), min, max)
        setattr(self.device, name, value)

    @QtCore.pyqtSlot(int, name='updateDevice')
    def updateDevice_selection(self, value):
        name = self.sender().objectName()
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
                wid.textEdited.connect(self.updateDevice)
            elif isinstance(wid, QtGui.QSpinBox):
                wid.valueChanged[int].connect(self.updateDevice)
            elif isinstance(wid, QtGui.QComboBox):
                wid.currentIndexChanged[int].connect(self.updateDevice)
            elif isinstance(wid, QtGui.QPushButton):
                wid.clicked.connect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))

    def disconnectSignals(self):
        for prop in self.properties:
            wid = getattr(self.ui, prop)
            if isinstance(wid, QtGui.QLineEdit):
                wid.textEdited.disconnect(self.updateDevice)
            elif isinstance(wid, QtGui.QSpinBox):
                wid.valueChanged[int].disconnect(self.updateDevice)
            elif isinstance(wid, QtGui.QComboBox):
                wid.currentIndexChanged[int].disconnect(self.updateDevice)
            elif isinstance(wid, QtGui.QPushButton):
                wid.clicked.disconnect(self.autoUpdateDevice)
            else:
                logger.warn('Unknown property: {}: {}'.format(prop, type(wid)))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    try:
        device = SR830()
    except ValueError:
        device = None
    wid = QSR830Settings(device=device)
    wid.show()
    sys.exit(app.exec_())
