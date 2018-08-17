# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from QPolargraph import polargraph
from QSR830 import SR830

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class Qacam(QtGui.QMainWindow):
    def __init__(self):
        super(Qacam, self).__init__()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.ui = Ui_Qacam()
        self.ui.setupUi(self)
        self.getDevices()
        self.connectSignals()
        self.initPlots()
        self.show()

    def getDevices(self):
        try:
            self.ui.lockin.device = SR830()
        except Exception:
            self.ui.lockin.setEnabled(False)
        try:
            self.ui.polargraph.device = polargraph()
        except Exception:
            self.ui.polargraph.setEnabled(False)

    def connectSignals(self):
        self.ui.scan.clicked.connect(self.ui.controlWidget.setEnabled)

    def initPlots(self):
        for plot in [self.ui.plot, self.ui.plotAmplitude, self.ui.plotPhase]:
            plot.setMouseEnabled(False, False)
            plot.setAspectLocked(ratio=1)
            plot.invertY(True)
            plot.showGrid(True, True, 0.2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
