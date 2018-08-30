# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import (pyqtSlot, Qt, QThread)
from Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from QPolargraph import (Polargraph, QPolargraphScan)
from QSR830 import SR830
from QDS345 import DS345
from common.Configure import Configure

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
        self.initScanner()
        self.connectSignals()
        self.initPlots()
        self.show()

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

    def initScanner(self):
        self.scanner = QPolargraphScan(polargraph=self.ui.polargraph)
        self.thread = QThread()
        self.thread.start()
        self.scanner.moveToThread(self.thread)

    def connectSignals(self):
        self.ui.scan.clicked.connect(lambda v:
                                     self.ui.controlWidget.setEnabled(False))
        self.ui.scan.clicked.connect(self.scanner.runScan)
        self.ui.scan.clicked.connect(self.stopScan)
        self.scanner.newData.connect(self.plotBelt)
        self.scanner.motion.connect(self.plotBelt)
        self.scanner.finished.connect(self.scanFinished)

        ui = self.ui.polargraph.ui
        ui.ell.valueChanged.connect(self.plotPath)
        ui.y0.valueChanged.connect(self.plotPath)
        ui.height.valueChanged.connect(self.plotPath)
        ui.width.valueChanged.connect(self.plotPath)
        ui.dy.valueChanged.connect(self.plotPath)

        self.ui.actionSaveSettings.triggered.connect(self.saveConfiguration)

    def initPlots(self):
        for plot in [self.ui.plot, self.ui.plotAmplitude, self.ui.plotPhase]:
            plot.setMouseEnabled(False, False)
            plot.setAspectLocked(ratio=1)
            plot.invertY(True)
            plot.showGrid(True, True, 0.2)
            self.plotPath()
            self.plotBelt()

    @pyqtSlot()
    def stopScan(self):
        if self.scanner.scanning():
            self.scanner.abort()
            self.ui.scan.setText('Stopping')
            self.ui.scan.setEnabled(False)
            self.statusBar().showMessage('Aborting scan ...')
        else:
            self.statusBar().showMessage('Scanning ...')
            self.ui.scan.setText('Stop')

    @pyqtSlot()
    def scanFinished(self):
        self.ui.scan.setText('Scan')
        self.ui.scan.setEnabled(True)
        self.ui.controlWidget.setEnabled(True)
        self.statusBar().showMessage('Scan finished')

    @pyqtSlot()
    def plotPath(self):
        self.scanner.computePath()
        path = self.scanner.path
        self.pathItem.setData(path[:, 0], path[:, 1])

    @pyqtSlot(object)
    def plotBelt(self, data=None):
        ell = self.ui.polargraph.ui.ell.value()
        if data is None:
            xp = 0.
            yp = self.ui.polargraph.ui.y0.value()
        else:
            xp, yp = data[1]
        x = [-ell/2, xp, ell/2]
        y = [0, yp, 0]
        self.beltItem.setData(x, y)

    @pyqtSlot()
    def saveConfiguration(self):
        self.config.save(self.ui.lockin)
        self.config.save(self.ui.functionGenerator)
        self.config.save(self.ui.polargraph)
        self.statusBar().showMessage('Configuration saved')
        logger.info('Configuration Saved')

    def closeEvent(self, event):
        self.statusBar().showMessage('Shutting down ...')
        self.scanner.shutdown()
        self.thread.quit()
        self.thread.wait()
        event.accept()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
