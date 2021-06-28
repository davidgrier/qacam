# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtProperty
from qacam.common.QSerialDevice import QSerialDevice
import numpy as np
from parse import parse

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DS345(QSerialDevice):
    '''Abstraction of a Stanford Research DS345 Function Generator

    Attributes
    ----------
    amplitude : float
       Output amplitude [Vpp]
    frequency : float
       Output frequency [Hz]
    offset : float
       Offset voltage [V]
    phase : float
       Output phase relative to reference [degrees]
    waveform : 0 .. 5
       Index of output waveform selection
    invert : bool
       If True, invert output signal
    mute : bool
       If True, set amplitude to 0 V.
       Else, set amplitude to last value.
    identification : str
       Identification string returned by instrument

    Methods
    -------
    identify() : bool
        Returns True if serial device is connected to a DS345
    '''

    def __init__(self):
        super(DS345, self).__init__(baudrate=QSerialDevice.Baud9600,
                                    databits=QSerialDevice.Data8,
                                    parity=QSerialDevice.NoParity,
                                    stopbits=QSerialDevice.TwoStop)
        self._mute = False
        self.amplitude = 0.

    def identify(self):
        '''Check identity of instrument

        Returns
        -------
        identify : bool
            True if attached instrument identifies itself as a DS345
        '''
        res = self.handshake('*IDN?')
        logger.debug(' Received: {}'.format(res))
        found = 'DS345' in res
        logger.info(' DS345: {}'.format(found))
        return found

    def busy(self):
        return False

    # Properties
    @pyqtProperty(bool)
    def mute(self):
        '''Output muted'''
        return self._mute

    @mute.setter
    def mute(self, set_mute):
        if set_mute:
            self.send('AMPL 0.00VP')
            self._mute = True
        elif self._mute:
            self._mute = False
            self.amplitude = self._amplitude

    # Function output adjustable properties
    @pyqtProperty(float)
    def amplitude(self):
        '''Output amplitude [Vpp]'''
        if self.mute:
            return self._amplitude
        else:
            return float(parse('{}VP', self.handshake('AMPL?'))[0])

    @amplitude.setter
    def amplitude(self, value):
        self._amplitude = float(value)
        if not self._mute:
            self.send('AMPL {:.2f}VP'.format(self._amplitude))

    @pyqtProperty(float)
    def frequency(self):
        '''Output frequency [Hz]'''
        return float(self.handshake('FREQ?'))

    @frequency.setter
    def frequency(self, value):
        self.send('FREQ {:.4f}'.format(float(value)))

    @pyqtProperty(float)
    def offset(self):
        '''Output offset [V]'''
        return float(self.handshake('OFFS?'))

    @offset.setter
    def offset(self, value):
        self.send('OFFS {:.2f}'.format(float(value)))

    @pyqtProperty(float)
    def phase(self):
        '''Output phase [degrees]'''
        return float(self.handshake('PHSE?'))

    @phase.setter
    def phase(self, value):
        self.send('PHSE {:.2f}'.format(float(value)))

    @pyqtProperty(int)
    def waveform(self):
        '''Output waveform
           0: sine
           1: square
           2: triangle
           3: ramp
           4: noise
           5: arbitrary
        '''
        return int(self.handshake('FUNC?'))

    @waveform.setter
    def waveform(self, value):
        self.send('FUNC {}'.format(np.clip(int(value), 0, 5)))

    @pyqtProperty(int)
    def invert(self):
        return int(self.handshake('INVT?'))

    @invert.setter
    def invert(self, value):
        self.send('INVT {}'.format(np.clip(int(value), 0, 1)))

    def setECL(self):
        '''Set ECL levels: 1Vpp, -1.3V offset'''
        self.send('AECL')

    def setTTL(self):
        '''Set TTL levels: 5Vpp, 2.5V offset'''
        self.send('ATTL')

    def setPhaseZero(self):
        '''Set waveform phase to zero'''
        self.send('PCLR')
