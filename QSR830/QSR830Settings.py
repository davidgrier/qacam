# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from common.QSettingsWidget import QSettingsWidget
from SR830Settings_UI import Ui_SR830Settings


class QSR830Settings(QSettingsWidget):
    """Configuration for a Stanford Research Systems SR830 lockin amplifier"""

    def __init__(self, parent=None, device=None):
        super(QSR830Settings, self).__init__(parent=parent,
                                             device=device,
                                             ui=Ui_SR830Settings())

    def configureUi(self):
        # validate edit fields
        notation = QtGui.QDoubleValidator.StandardNotation
        val = QtGui.QDoubleValidator(0.001, 102000., 3, self.ui.frequency)
        val.setNotation(notation)
        self.ui.frequency.setValidator(val)
        val = QtGui.QDoubleValidator(0.004, 5, 3, self.ui.amplitude)
        val.setNotation(notation)
        self.ui.amplitude.setValidator(val)
        val = QtGui.QDoubleValidator(-360., 729.99, 2, self.ui.phase)
        val.setNotation(notation)
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


if __name__ == "__main__":
    import sys
    from SR830 import SR830

    app = QtGui.QApplication(sys.argv)
    try:
        device = SR830()
    except ValueError:
        device = None
    wid = QSR830Settings(device=device)
    wid.show()
    sys.exit(app.exec_())
