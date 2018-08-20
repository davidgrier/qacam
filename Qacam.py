# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from QPolargraph import polargraph
from QSR830 import SR830
from QDS345 import DS345
from common.configure import configure

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
        self.config = configure(self)
        try:
            self.ui.lockin.device = SR830()
            self.config.restore(self.ui.lockin)
        except ValueError:
            logger.warn('No lockin detected')
        try:
            self.ui.functionGenerator.device = DS345()
            self.config.restore(self.ui.functionGenerator)
        except ValueError:
            logger.warn('No function generator detected')
        try:
            self.ui.polargraph.device = polargraph()
            self.config.restore(self.ui.polargraph)
        except ValueError:
            logger.warn('No polargraph detected')

    def configureUi(self):
        self.ui.polargraph.ui.frameBelt.hide()
        self.ui.functionGenerator.ui.offset.setDisabled(True)
        self.ui.lockin.ui.frameAuto.hide()
        self.ui.lockin.ui.frameReference.hide()

    def connectSignals(self):
        self.ui.scan.clicked.connect(self.ui.controlWidget.setEnabled)
        self.ui.actionSaveSettings.triggered.connect(self.saveConfiguration)

    def initPlots(self):
        for plot in [self.ui.plot, self.ui.plotAmplitude, self.ui.plotPhase]:
            plot.setMouseEnabled(False, False)
            plot.setAspectLocked(ratio=1)
            plot.invertY(True)
            plot.showGrid(True, True, 0.2)

    @pyqtSlot()
    def saveConfiguration(self):
        self.config.save(self.ui.lockin)
        self.config.save(self.ui.functionGenerator)
        self.config.save(self.ui.polargraph)
        logger.info('Configuration Saved')


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
