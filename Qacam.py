# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, Qt
from Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from QPolargraph import Polargraph
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
            self.ui.polargraph.device = Polargraph()
            self.config.restore(self.ui.polargraph)
        except ValueError:
            logger.warn('No polargraph detected')
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

    def configureUi(self):
        self.ui.polargraph.ui.frameBelt.hide()
        self.ui.functionGenerator.ui.offset.setDisabled(True)
        self.ui.lockin.ui.frameAuto.hide()
        self.ui.lockin.ui.frameReference.hide()
        pen = pg.mkPen('r', style=Qt.DotLine)
        self.pathItem = pg.PlotDataItem(pen=pen)
        self.ui.plot.addItem(self.pathItem)
        pen = pg.mkPen('k', thick=3)
        brush = pg.mkBrush('y')
        self.beltItem = pg.PlotDataItem(pen=pen,
                                        symbol='o',
                                        symbolBrush=brush,
                                        symbolPen=pen)
        self.ui.plot.addItem(self.beltItem)

    def connectSignals(self):
        self.ui.scan.clicked.connect(self.ui.controlWidget.setEnabled)
        self.ui.scan.clicked.connect(self.scan)
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
            self.plotBelt()

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
        polargraph = self.ui.polargraph.ui
        height = polargraph.height.value()
        width = polargraph.width.value()
        dy = polargraph.dy.value()
        y0 = polargraph.y0.value()
        yright = np.arange(y0, y0+height, dy)
        yleft = yright + dy/2.
        npts = yright.size
        x0 = width/2.
        rright = zip([x0]*npts, yright)
        rleft = zip([-x0]*npts, yleft)
        coords = []
        for i in range(npts):
            coords.append(rright[i])
            coords.append(rleft[i])
        self.path = np.array(coords)

    def plotPath(self):
        if self.path is not None:
            self.pathItem.setData(self.path[:, 0], self.path[:, 1])

    def plotBelt(self, pos=None):
        ell = self.ui.polargraph.ui.ell.value()

        if pos is None:
            xp = 0.
            yp = self.ui.polargraph.ui.y0.value()
        else:
            xp, yp = pos
        print(xp, yp)
        x = [-ell/2, xp, ell/2]
        y = [0, yp, 0]
        self.beltItem.setData(x, y)

    @pyqtSlot()
    def scan(self):
        polargraph = self.ui.polargraph.device
        if polargraph is None:
            return
        nsteps = self.path[:, 0].size
        for n in range(2):
            polargraph.goto(self.path[n, 0], self.path[n, 1])
            while polargraph.running():
                pos = polargraph.position
                self.plotBelt(pos)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
