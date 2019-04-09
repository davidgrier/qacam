# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QObject, pyqtSignal, pyqtSlot)
import numpy as np


class QacamScan(QObject):

    '''Scan object ready for threading

    Compute the path for the polargraph to scan, and then
    perform the scan while reading values from the polargraph
    and lockin amplifier.

    ...

    Attributes
    ----------
    polagraph : QPolargraph
       Polargraph object
    source : QDS345
       Function generator
    lockin : QSR830
       Lockin amplifier

    Methods
    -------
    scanning() : bool
        Return true if the motors are moving
    reset():
        Cancel scan
    computePath()
        Obtain scan parameters from polargraph and determine
        vertices of serpentine scan path

    Signals
    -------
    newData(object)
        Emitted for every data data point.
        Value is a list of polargraph indexes,
        polargraph position and lockin data.
    motion(object)
        Emitted when polargraph is moving but not recording data
        Value is list of polargraph indexes
        and polargraph position.
    finished()
        Emitted when scan completes

    Slots
    -----
    runScan()
        Perform serpentine scan with data acquisition.
        Then return to home position and release motors.
    '''

    newData = pyqtSignal(object)
    motion = pyqtSignal(object)
    finished = pyqtSignal()

    def __init__(self, parent=None,
                 polargraph=None,
                 source=None,
                 lockin=None):
        super(QacamScan, self).__init__(parent)
        self.polargraph = polargraph
        self.source = source
        self.lockin = lockin
        self.computePath()
        self._scanning = False
        self._reset = False

    def computePath(self):
        polargraph = self.polargraph.ui
        height = polargraph.height.value()
        width = polargraph.width.value()
        xstart = polargraph.x1.value() - width / 2.
        xstop = xstart + width
        y0 = polargraph.y0.value()
        ystart = y0 + polargraph.y1.value()
        ystop = ystart + height
        dy = polargraph.dy.value()
        yright = np.arange(ystart, ystop, dy)
        yleft = yright + dy / 2.
        npts = yright.size
        rright = list(zip([xstart] * npts, yright))
        rleft = list(zip([xstop] * npts, yleft))
        coords = [(0, y0), (polargraph.x1.value(), ystart)]
        for i in range(npts):
            coords.append(rright[i])
            coords.append(rleft[i])
        self.path = np.array(coords)
        self.xstart = xstart
        self.xstop = xstop
        self.ystart = ystart
        self.ystop = ystop

    @pyqtSlot()
    def runScan(self):
        if self._scanning or self._reset:
            self._reset = False
            return
        self._scanning = True
        polargraph = self.polargraph.device
        lockin = self.lockin.device
        source = self.source.device
        source.mute = False
        npts = len(self.path[:, 0])
        for n in range(npts):
            polargraph.goto(self.path[n, 0], self.path[n, 1])
            while polargraph.running() and not self._reset:
                self.newData.emit([polargraph.indexes,
                                   polargraph.position,
                                   lockin.data])
            if self._reset:
                break
        source.mute = True
        polargraph.goto(self.path[0, 0], self.path[0, 1])
        while polargraph.running():
            self.motion.emit([polargraph.indexes, polargraph.position])
        polargraph.release()
        self._scanning = False
        self.finished.emit()

    def scanning(self):
        return self._scanning

    def reset(self):
        self._reset = True
