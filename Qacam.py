# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QMainWindow, QFileDialog)
from PyQt5.QtCore import (pyqtSlot, Qt, QThread)
from qacam.Qacam_UI import Ui_Qacam
import pyqtgraph as pg
from qacam.QPolargraph.Polargraph import Polargraph
from qacam.QSR830.SR830 import SR830
from qacam.QDS345.DS345 import DS345
from qacam.QPolargraph.PolargraphFake import PolargraphFake
from qacam.QSR830.SR830Fake import SR830Fake
from qacam.QDS345.DS345Fake import DS345Fake

from QacamScan import QacamScan
from qacam.common.Configure import Configure
import numpy as np
from scipy.interpolate import griddata
import csv

import logging
logging.basicConfig()
logger = logging.getLogger('Qacam')


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
        # hide unnecessary functionality
        self.ui.polargraph.ui.frameBelt.hide()
        self.ui.functionGenerator.ui.offset.setDisabled(True)
        self.ui.lockin.ui.frameAuto.hide()
        self.ui.lockin.ui.frameReference.hide()

    def getDevices(self):
        self.config = Configure(self)
        try:
            self.ui.polargraph.device = Polargraph()
            self.config.restore(self.ui.polargraph)
        except ValueError:
            logger.warn('No polargraph detected ... using fake')
            self.ui.polargraph.device = PolargraphFake()
        try:
            self.ui.lockin.device = SR830()
        except ValueError:
            logger.warn('No lockin detected ... using fake')
            self.ui.lockin.device = SR830Fake()
        self.config.restore(self.ui.lockin)
        try:
            self.ui.functionGenerator.device = DS345()
            self.ui.functionGenerator.device.mute = True
            self.config.restore(self.ui.functionGenerator)
        except ValueError:
            logger.warn('No function generator detected ... using fake')
            self.ui.functionGenerator.device = DS345Fake()

    def initScanner(self):
        self.scanner = QacamScan(polargraph=self.ui.polargraph,
                                 source=self.ui.functionGenerator,
                                 lockin=self.ui.lockin)
        self.thread = QThread()
        self.thread.start()
        self.scanner.moveToThread(self.thread)

    def connectSignals(self):
        self.ui.scan.clicked.connect(lambda v:
                                     self.ui.controlWidget.setEnabled(False))
        self.ui.scan.clicked.connect(self.scanner.runScan)
        self.ui.scan.clicked.connect(self.toggleScan)
        self.scanner.newData.connect(self.plotBelt)
        self.scanner.newData.connect(self.recordScan)
        self.scanner.motion.connect(self.plotBelt)
        self.scanner.finished.connect(self.scanFinished)

        ui = self.ui.polargraph.ui
        ui.ell.valueChanged.connect(self.plotPath)
        ui.y0.valueChanged.connect(self.plotPath)
        ui.height.valueChanged.connect(self.plotPath)
        ui.width.valueChanged.connect(self.plotPath)
        ui.dy.valueChanged.connect(self.plotPath)

        self.ui.actionSaveSettings.triggered.connect(self.saveConfiguration)
        self.ui.actionSaveRawData.triggered.connect(self.saveRawData)

    def initPlots(self):
        for plot in [self.ui.plot, self.ui.plotAmplitude, self.ui.plotPhase]:
            plot.setMouseEnabled(False, False)
            plot.setAspectLocked(ratio=1)
            plot.invertY(True)
            plot.showGrid(True, True, 0.2)
        # graphical representation of planned scan path
        pen = pg.mkPen('r', style=Qt.DotLine)
        self.pathItem = pg.PlotDataItem(pen=pen)
        self.ui.plot.addItem(self.pathItem)
        self.plotPath()
        # graphical representation of current data
        pen = pg.mkPen('k')
        self.traceItem = pg.ScatterPlotItem(pen=pen)
        self.ui.plot.addItem(self.traceItem)
        # graphical representation of polargraph belt
        pen = pg.mkPen('k', thick=3)
        brush = pg.mkBrush('y')
        self.beltItem = pg.PlotDataItem(pen=pen,
                                        symbol='o',
                                        symbolBrush=brush,
                                        symbolPen=pen)
        self.plotBelt()
        # image representations of amplitude and phase
        self.ui.plot.addItem(self.beltItem)
        self.amplitudeItem = pg.ImageItem()
        self.ui.plotAmplitude.addItem(self.amplitudeItem)
        self.phaseItem = pg.ImageItem()
        self.ui.plotPhase.addItem(self.phaseItem)

    @pyqtSlot()
    def toggleScan(self):
        if self.scanner.scanning():
            self.scanner.reset()
            self.ui.scan.setText('Stopping')
            self.ui.scan.setEnabled(False)
            self.statusBar().showMessage('Aborting scan ...')
        else:
            self.data = []
            self.traceItem.clear()
            self.statusBar().showMessage('Scanning ...')
            self.ui.scan.setText('Stop')

    @pyqtSlot()
    def scanFinished(self):
        self.ui.scan.setText('Scan')
        self.ui.scan.setEnabled(True)
        self.ui.controlWidget.setEnabled(True)
        d = np.array(self.data)
        x0 = self.scanner.x0
        x1 = self.scanner.x1
        y0 = self.scanner.y0
        y1 = self.scanner.y1
        grid_x, grid_y = np.mgrid[x0:x1:128j, y0:y1:128j]
        self.amplitude = griddata(d[:, 2:4], d[:, 4],
                                  (grid_x, grid_y), method='cubic')
        self.amplitudeItem.setImage(self.amplitude)
        self.phase = griddata(d[:, 2:4], d[:, 5],
                              (grid_x, grid_y), method='cubic')
        self.phaseItem.setImage(self.phase)
        self.statusBar().showMessage('Scan finished')

    @pyqtSlot()
    def plotPath(self):
        self.scanner.computePath()
        path = self.scanner.path
        self.pathItem.setData(path[:, 0], path[:, 1])

    @pyqtSlot(object)
    def recordScan(self, data):
        self.data.append([val for tup in data for val in tup])
        x, y = data[1]
        amp, phi = data[2]
        hue = (phi/360. + 1.) % 1.
        brush = pg.mkBrush(color=pg.hsvColor(hue))
        self.traceItem.addPoints([x], [y], brush=brush)

    @pyqtSlot(object)
    def plotBelt(self, data=None):
        ell = self.ui.polargraph.ui.ell.value()
        if data is None:
            n1 = 0
            n2 = 0
            xp = 0.
            yp = self.ui.polargraph.ui.y0.value()
        else:
            n1, n2 = data[0]
            xp, yp = data[1]
        self.ui.n1.display(n1)
        self.ui.n2.display(n2)
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

    @pyqtSlot()
    def saveRawData(self, name=None):
        if name is None:
            default = self.config.filename(suffix='.csv')
            name, _ = QFileDialog.getSaveFileName(self,
                                                  'Save Raw Data',
                                                  default,
                                                  'Raw Data (*.csv)')
        try:
            with open(name, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(self.data)
            self.statusBar().showMessage('Raw data saved to {}'.format(name))
        except AttributeError:
            self.statusBar().showMessage('Save aborted')

    def closeEvent(self, event):
        self.statusBar().showMessage('Shutting down ...')
        self.ui.functionGenerator.device.mute = True
        self.scanner.reset()
        self.thread.quit()
        self.thread.wait()
        event.accept()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    instrument = Qacam()
    sys.exit(app.exec_())
