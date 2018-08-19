# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from common.QSettingsWidget import QSettingsWidget
from Polargraph_UI import Ui_Polargraph


class QPolargraphSettings(QSettingsWidget):
    """Configuration for a polargraph"""

    def __init__(self, parent=None, device=None):
        super(QPolargraphSettings, self).__init__(parent=parent,
                                                  device=device,
                                                  ui=Ui_Polargraph())

    @QtCore.pyqtSlot(object)
    def limitRange(self, value):
        self.width.setMaximum(min(self.width.value(), 0.9*value))
        self.height.setMaximum(min(self.height.value(), 0.9*value))

    def ConfigureUi(self):
        self.L.valueChanged[QtCore.double].connect(self.limitRange)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    from polargraph import polargraph

    app = QApplication(sys.argv)
    try:
        device = polargraph()
    except ValueError:
        device = None
    wid = QPolargraphSettings(device=device)
    wid.show()
    sys.exit(app.exec_())
