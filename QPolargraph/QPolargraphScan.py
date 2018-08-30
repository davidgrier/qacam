# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QObject, pyqtSignal, pyqtSlot)
import numpy as np


class QPolargraphScan(QObject):
    """Scan object ready for threading"""

    newData = pyqtSignal(object)
    motion = pyqtSignal(object)
    finished = pyqtSignal()

    def __init__(self, parent=None,
                 polargraph=None,
                 lockin=None):
        super(QPolargraphScan, self).__init__(parent)
        self.polargraph = polargraph
        self.lockin = lockin
        self.computePath()
        self.scanning = False
        self.abort = False

    def computePath(self):
        polargraph = self.polargraph.ui
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
        coords = [(0, y0)]
        for i in range(npts):
            coords.append(rright[i])
            coords.append(rleft[i])
        self.path = np.array(coords)

    @pyqtSlot()
    def runScan(self):
        if self.scanning or self.abort:
            self.abort = False
            return
        self.scanning = True
        polargraph = self.polargraph.device
        npts = len(self.path[:, 0])
        for n in range(npts):
            polargraph.goto(self.path[n, 0], self.path[n, 1])
            while polargraph.running() and not self.abort:
                self.newData.emit([polargraph.indexes,
                                   polargraph.position])
            if self.abort:
                break
        polargraph.goto(self.path[0, 0], self.path[0, 1])
        while polargraph.running():
            self.motion.emit([polargraph.indexes, polargraph.position])
        self.scanning = False
        self.finished.emit()
