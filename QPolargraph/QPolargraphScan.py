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
                 source=None,
                 lockin=None):
        super(QPolargraphScan, self).__init__(parent)
        self.polargraph = polargraph
        self.source = source
        self.lockin = lockin
        self.computePath()
        self._scanning = False
        self._abort = False
        self._shutdown = False

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
        self.x0 = -x0
        self.x1 = x0
        self.y0 = y0
        self.y1 = y0 + height

    @pyqtSlot()
    def runScan(self):
        if self._scanning or self._abort:
            self._abort = False
            return
        self._scanning = True
        polargraph = self.polargraph.device
        lockin = self.lockin.device
        source = self.source.device
        # source.mute = False
        npts = len(self.path[:, 0])
        for n in range(npts):
            polargraph.goto(self.path[n, 0], self.path[n, 1])
            while polargraph.running() and not self._abort:
                self.newData.emit([polargraph.indexes,
                                   polargraph.position,
                                   lockin.data])
            if self._shutdown:
                self.finished.emit()
                return
            if self._abort:
                break
        # source.mute = True
        polargraph.goto(self.path[0, 0], self.path[0, 1])
        while polargraph.running():
            self.motion.emit([polargraph.indexes, polargraph.position])
        polargraph.release()
        self._scanning = False
        self.finished.emit()

    def scanning(self):
        return self._scanning

    def abort(self):
        self._abort = True

    def shutdown(self):
        self._shutdown = True
