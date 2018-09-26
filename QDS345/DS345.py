# -*- coding: utf-8 -*-

from common.SerialDevice import SerialDevice
import numpy as np
import re
import serial
from parse import parse


class DS345(SerialDevice):

    def __init__(self):
        super(DS345, self).__init__(baudrate=9600,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_TWO)
        self._mute = False

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

    @property
    def mute(self):
        """Output muted"""
        return self._mute

    @mute.setter
    def mute(self, state):
        if state:
            if not self._mute:
                self._amplitude = self.amplitude
                self.amplitude = 0.
                self._mute = True
        else:
            if self._mute:
                self.amplitude = self._amplitude
                self._mute = False
                
    # Function output adjustable properties
    @property
    def amplitude(self):
        """Output amplitude [Vpp]"""
        if self.mute:
            return self._amplitude
        else:
            return float(parse('{}VP', self.command('AMPL?'))[0])

    @amplitude.setter
    def amplitude(self, value):
        if self.mute:
            self._amplitude = float(value)
        else:
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
        return int(self.command('FUNC?'))

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
