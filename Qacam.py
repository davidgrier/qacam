# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, Qt
from Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from QPolargraph import polargraph
from QSR830 import SR830
from QDS345 import DS345
from common.Configure import Configure
import numpy as np

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
        self.computePath()
        self.initPlots()
        self.show()

    def getDevices(self):
        self.config = Configure(self)
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
        pen = pg.mkPen('r', style=Qt.DotLine)
        self.pathItem = pg.PlotDataItem(pen=pen)
        self.ui.plot.addItem(self.pathItem)

    def connectSignals(self):
        self.ui.scan.clicked.connect(self.ui.controlWidget.setEnabled)
        self.ui.actionSaveSettings.triggered.connect(self.saveConfiguration)
        ui = self.ui.polargraph.ui
        ui.height.valueChanged.connect(self.updatePath)
        ui.width.valueChanged.connect(self.updatePath)
        ui.dy.valueChanged.connect(self.updatePath)

    def initPlots(self):
        for plot in [self.ui.plot, self.ui.plotAmplitude, self.ui.plotPhase]:
            plot.setMouseEnabled(False, False)
            plot.setAspectLocked(ratio=1)
            plot.invertY(True)
            plot.showGrid(True, True, 0.2)
            self.computePath()
            self.plotPath()

    @pyqtSlot()
    def saveConfiguration(self):
        self.config.save(self.ui.lockin)
        self.config.save(self.ui.functionGenerator)
        self.config.save(self.ui.polargraph)
        logger.info('Configuration Saved')

    @pyqtSlot()
    def updatePath(self):
        self.computePath()
        self.plotPath()

    def computePath(self):
        polargraph = self.ui.polargraph.device
        y0 = np.arange(0., polargraph.height, polargraph.dy)
        y0 += polargraph.dy
        y1 = y0 + polargraph.dy/2.
        x0 = polargraph.width/2.
        r0 = zip([x0]*y0.size, y0)
        r1 = zip([-x0]*y1.size, y1)
        coords = []
        for i in range(y0.size):
            coords.append(r0[i])
            coords.append(r1[i])
        self.path = np.array(coords)

    def plotPath(self):
        self.pathItem.setData(self.path[:, 0], self.path[:, 1])


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
