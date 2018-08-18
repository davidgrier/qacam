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
