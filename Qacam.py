# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from QPolargraph import polargraph
from QSR830 import SR830
from QDS345 import DS345

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class Qacam(QMainWindow):
    def __init__(self):
        super(Qacam, self).__init__()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.ui = Ui_Qacam()
        self.ui.setupUi(self)
        self.configureUi()
        self.getDevices()
        self.connectSignals()
        self.initPlots()
        self.show()

    def getDevices(self):
        try:
            self.ui.lockin.device = SR830()
        except ValueError:
            logger.warn('No lockin detected')
        try:
            self.ui.functionGenerator.device = DS345()
        except ValueError:
            logger.warn('No function generator detected')
        try:
            self.ui.polargraph.device = polargraph()
        except ValueError:
            logger.warn('No polargraph detected')

    def configureUi(self):
        self.ui.polargraph.ui.frameBelt.hide()
        self.ui.functionGenerator.ui.offset.setDisabled(True)
        self.ui.lockin.ui.frameAuto.hide()
        self.ui.lockin.ui.frameReference.hide()

    def connectSignals(self):
        self.ui.scan.clicked.connect(self.ui.controlWidget.setEnabled)

    def initPlots(self):
        for plot in [self.ui.plot, self.ui.plotAmplitude, self.ui.plotPhase]:
            plot.setMouseEnabled(False, False)
            plot.setAspectLocked(ratio=1)
            plot.invertY(True)
            plot.showGrid(True, True, 0.2)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
