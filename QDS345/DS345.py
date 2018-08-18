# -*- coding: utf-8 -*-

from common.SerialDevice import SerialDevice
import numpy as np
import re


class DS345(SerialDevice):

    def __init__(self):
        super(DS345, self).__init__()

    def command(self, cmd):
        """Send cmd to function generator and return response"""
        self.write(cmd)
        return self.readln()

    def identify(self):
        """Check identity of instrument"""
        idn = self.identification
        return re.search('DS345', idn)

    # Properties
    @property
    def identification(self):
        """Read identification string from function generator"""
        return self.command('*IDN?')

    # Function output adjustable properties
    @property
    def amplitude(self):
        """Output amplitude [Vpp]"""
        return float(self.command('AMPL?'))

    @amplitude.setter
    def amplitude(self, value):
        self.write('AMPL %.2fVP' % float(value))

    @property
    def frequency(self):
        """Output frequency [Hz]"""
        return float(self.command('FREQ?'))

    @frequency.setter
    def frequency(self, value):
        self.write('FREQ %.4f' % float(value))

    @property
    def offset(self):
        """Output offset [V]"""
        return float(self.command('OFFS?'))

    @offset.setter
    def offset(self, value):
        self.write('OFFS %.2f' % float(value))

    @property
    def phase(self):
        """Output phase [degrees]"""
        return float(self.command('PHSE?'))

    @phase.setter
    def phase(self, value):
        self.write('PHSE %.2f' % float(value))

    @property
    def waveform(self):
        """Output waveform
           0: sine
           1: square
           2: triangle
           3: ramp
           4: noise
           5: arbitrary
        """
        return self.command('FUNC?')

    @waveform.setter
    def waveform(self, value):
        self.write('FUNC %d' % np.clip(int(value), 0, 5))

    @property
    def invert(self):
        return int(self.command('INVT?'))

    @invert.setter
    def invert(self, value):
        self.write('INVT %d', np.clip(int(value), 0, 1))

    def setECL(self):
        """Set ECL levels: 1Vpp, -1.3V offset"""
        self.write('AECL')

    def setTTL(self):
        """Set TTL levels: 5Vpp, 2.5V offset"""
        self.write('ATTL')

    def setPhaseZero(self):
        """Set waveform phase to zero"""
        self.write('PCLR')
