# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from common.QSettingsWidget import QSettingsWidget
from Polargraph_UI import Ui_Polargraph


class QPolargraphSettings(QSettingsWidget):
    """Configuration for a polargraph"""

    def __init__(self, parent=None, device=None):
        super(QPolargraphSettings, self).__init__(parent=parent,
                                                  device=device,
                                                  ui=Ui_Polargraph())

    def configureUi(self):
        # validate edit fields
        notation = QtGui.QDoubleValidator.StandardNotation
        val = QtGui.QDoubleValidator(0.1, 5, 2, self.ui.L)
        val.setNotation(notation)
        self.ui.L.setValidator(val)
        val = QtGui.QDoubleValidator(0.01, 0.5, 3, self.ui.y0)
        val.setNotation(notation)
        self.ui.y0.setValidator(val)
        val = QtGui.QDoubleValidator(100, 1000, 0, self.ui.speed)
        val.setNotation(notation)
        self.ui.speed.setValidator(val)
        val = QtGui.QDoubleValidator(0.01, 5, 2, self.ui.width)
        val.setNotation(notation)
        self.ui.width.setValidator(val)
        val = QtGui.QDoubleValidator(0.01, 5, 2, self.ui.height)
        val.setNotation(notation)
        self.ui.height.setValidator(val)


if __name__ == "__main__":
    import sys
    from polargraph import polargraph

    app = QtGui.QApplication(sys.argv)
    try:
        device = polargraph()
    except ValueError:
        device = None
    wid = QPolargraphSettings(device=device)
    wid.show()
    sys.exit(app.exec_())
