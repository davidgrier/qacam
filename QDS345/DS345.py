# -*- coding: utf-8 -*-

from qacam.common.SerialDevice import SerialDevice
import numpy as np
import re
import serial
from parse import parse


class DS345(SerialDevice):
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
    command(cmd) : str
        Sends command to DS345 and returns response
    identify() : bool
        Returns True if serial device is connected to a DS345
    '''

    def __init__(self):
        super(DS345, self).__init__(baudrate=9600,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_TWO)
        self._mute = False

    def command(self, cmd):
        '''Send cmd to function generator and return response

        Parameters
        ----------
        cmd : str
            String with command for DS345

        Returns
        -------
        result : str
            String returned by DS345
        '''
        self.write(cmd)
        return self.readln()

    def identify(self):
        '''Check identity of instrument

        Returns
        -------
        identify : bool
            True if attached instrument identifies itself as a DS345
        '''
        idn = self.identification
        return re.search('DS345', idn)

    # Properties
    @property
    def identification(self):
        '''Identification string from function generator'''
        return self.command('*IDN?')

    @property
    def mute(self):
        '''Output muted'''
        return self._mute

    @mute.setter
    def mute(self, set_mute):
        if set_mute:
            self.write('AMPL 0.00VP')
            self._mute = True
        elif self._mute:
            self._mute = False
            self.amplitude = self._amplitude

    # Function output adjustable properties
    @property
    def amplitude(self):
        '''Output amplitude [Vpp]'''
        if self.mute:
            return self._amplitude
        else:
            return float(parse('{}VP', self.command('AMPL?'))[0])

    @amplitude.setter
    def amplitude(self, value):
        self._amplitude = float(value)
        if not self._mute:
            self.write('AMPL %.2fVP' % self._amplitude)

    @property
    def frequency(self):
        '''Output frequency [Hz]'''
        return float(self.command('FREQ?'))

    @frequency.setter
    def frequency(self, value):
        self.write('FREQ %.4f' % float(value))

    @property
    def offset(self):
        '''Output offset [V]'''
        return float(self.command('OFFS?'))

    @offset.setter
    def offset(self, value):
        self.write('OFFS %.2f' % float(value))

    @property
    def phase(self):
        '''Output phase [degrees]'''
        return float(self.command('PHSE?'))

    @phase.setter
    def phase(self, value):
        self.write('PHSE %.2f' % float(value))

    @property
    def waveform(self):
        '''Output waveform
           0: sine
           1: square
           2: triangle
           3: ramp
           4: noise
           5: arbitrary
        '''
        return int(self.command('FUNC?'))

    @waveform.setter
    def waveform(self, value):
        self.write('FUNC %d' % np.clip(int(value), 0, 5))

    @property
    def invert(self):
        return int(self.command('INVT?'))

    @invert.setter
    def invert(self, value):
        self.write('INVT %d' % np.clip(int(value), 0, 1))

    def setECL(self):
        """Set ECL levels: 1Vpp, -1.3V offset"""
        self.write('AECL')

    def setTTL(self):
        """Set TTL levels: 5Vpp, 2.5V offset"""
        self.write('ATTL')

    def setPhaseZero(self):
        """Set waveform phase to zero"""
        self.write('PCLR')
