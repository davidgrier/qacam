# -*- coding: utf-8 -*-

from qacam.common.SerialDevice import SerialDevice
import numpy as np
import re


class SR830(SerialDevice):
    '''Abstraction of Stanford Research SR830 Lockin Amplifier

    ...

    Attributes
    ----------
    phase : float
        Phase offset relative to reference [degrees]
    source : int
        Reference source
    frequency : float
        Reference frequency [Hz]
    trigger : int
        Trigger mode for external reference
    harmonic : int
        Detection harmonic
    amplitude : float
        Amplitude of internal reference output [V]
    input : int
        Input configuration
    grounding : int
        Input shield grounding
    coupling : int
        Input coupling
    filter : int
        Input line filter mode
    sensitivity : int
        Input sensitivity mode
    reserve : int
        Dynamic reserve mode
    timeConstant : int
        Time constant mode
    slope : int
        Low-pass filter slope mode
    synchronous : int
        Synchronous filter status
    identification : str
        Identification string returned by instrument

    Methods
    -------
    identify() : bool
        Returns True if attached instrument is a SR830
    busy() : bool
        Returns True if the instrument is busy

    '''

    def __init__(self, baudrate=9600, timeout=1):
        super(SR830, self).__init__(baudrate=baudrate,
                                    timeout=timeout)

    def identify(self):
        '''Check identity of instrument

        Returns
        -------
        identify : bool
            True if attached instrument is a SR830
        '''
        idn = self.identification
        return re.search('SR830', idn)

    def busy(self):
        '''Check if instrument is busy

        Returns
        -------
        busy : bool
            True if instrument is executing a command or has
            an error condition.
        '''
        status = self.status()
        executing = not bool(status & 0b11)
        error = bool(status & 0b100)
        return executing or error

    # Properties

    @property
    def identification(self):
        '''Identification string returned by instrument'''
        self.write('*IDN?')
        return self.readln()

    # Reference and phase commands

    @property
    def phase(self):
        '''Phase offset relative to reference [degrees]'''
        return np.float(self.command('PHAS?'))

    @phase.setter
    def phase(self, value):
        self.write('PHAS %.2f' % np.clip(float(value), -360., 729.99))

    @property
    def source(self):
        '''Reference source:
           0: external
           1: internal
        '''
        return int(self.command('FMOD?'))

    @source.setter
    def source(self, value):
        self.write('FMOD %d' % np.clip(int(value), 0, 1))

    @property
    def frequency(self):
        '''Reference frequency [Hz]'''
        return float(self.command('FREQ?'))

    @frequency.setter
    def frequency(self, value):
        self.write('FREQ %f' % np.clip(float(value), 0.001, 102000.))

    @property
    def trigger(self):
        '''Reference trigger mode for external reference
           0: Sine zero crossing
           1: TTL rising edge
           2: TTL falling edge
        '''
        return int(self.command('RSLP?'))

    @trigger.setter
    def trigger(self, value):
        self.write('RSLP %d' % np.clip(int(value), 0, 2))

    @property
    def harmonic(self):
        '''Detection harmonic'''
        return int(self.command('HARM?'))

    @harmonic.setter
    def harmonic(self, value):
        self.write('HARM %d' % np.clip(int(value), 1, 19999))

    @property
    def amplitude(self):
        '''Amplitude of sine output [V]'''
        return float(self.command('SLVL?'))

    @amplitude.setter
    def amplitude(self, value):
        self.write('SLVL %.3f' % np.clip(float(value), 0.004, 5.))

    # Input and filter commands
    @property
    def input(self):
        '''Input configuration:
           0: Input A
           1: A-B
           2: I (1 MOhm)
           3: I (100 MOhm)
        '''
        return int(self.command('ISRC?'))

    @input.setter
    def input(self, value):
        self.write('ISRC %d' % np.clip(int(value), 0, 3))

    @property
    def grounding(self):
        '''Input shield grounding mode
           0: shield is floating
           1: shield is grounded
        '''
        return int(self.command('IGND?'))

    @grounding.setter
    def grounding(self, value):
        self.write('IGND %d' % np.clip(int(value), 0, 1))

    @property
    def coupling(self):
        '''Input coupling mode
           0: AC coupling
           1: DC coupling
        '''
        return int(self.command('ICPL?'))

    @coupling.setter
    def coupling(self, value):
        self.write('ICPL %d' % np.clip(int(value), 0, 1))

    @property
    def filter(self):
        '''Input line filter mode
           0: No filters
           1: Line frequency notch filter
           2: 2x line frequency filter
           3: Both notch filters
        '''
        return int(self.command('ILIN?'))

    @filter.setter
    def filter(self, value):
        self.write('ILIN %d' % np.clip(int(value), 0, 3))

    # Gain and time constant commands
    @property
    def sensitivity(self):
        '''Input sensitivity mode
           0 : 2 nV/fA    13: 50 µV/pA
           1 : 5 nV/fA    14: 100 µV/pA
           2 : 10 nV/fA   15: 200 µV/pA
           3 : 20 nV/fA   16: 500 µV/pA
           4 : 50 nV/fA   17: 1 mV/nA
           5 : 100 nV/fA  18: 2 mV/nA
           6 : 200 nV/fA  19: 5 mV/nA
           7 : 500 nV/fA  20: 10 mV/nA
           8 : 1 µV/pA    21: 20 mV/nA
           9 : 2 µV/pA    22: 50 mV/nA
           10: 5 µV/pA    23: 100 mV/nA
           11: 10 µV/pA   24: 200 mV/nA
           12: 20 µV/pA   25: 500 mV/nA
                          26: 1 V/µA
        '''
        return int(self.command('SENS?'))

    @sensitivity.setter
    def sensitivity(self, value):
        self.write('SENS %d' % np.clip(int(value), 0, 26))

    @property
    def reserve(self):
        '''Dynamic reserve mode
           0: High reserve
           1: Normal
           2: Low noise (minimum)
        '''
        return int(self.command('RMOD?'))

    @reserve.setter
    def reserve(self, value):
        self.write('RMOD %d' % np.clip(int(value), 0, 2))

    @property
    def timeConstant(self):
        '''Time constant mode
           0: 10 µs   10: 1 s
           1: 30 µs   11: 3 s
           2: 100 µs  12: 10 s
           3: 300 µs  13: 30 s
           4: 1 ms    14: 100 s
           5: 3 ms    15: 300 s
           6: 10 ms   16: 1 ks
           7: 30 ms   17: 3 ks
           8: 100 ms  18: 10 ks
           9: 300 ms  19: 30 ks
        '''
        return int(self.command('OFLT?'))

    @timeConstant.setter
    def timeConstant(self, value):
        self.write('OFLT %d' % np.clip(int(value), 0, 19))

    @property
    def slope(self):
        '''Low pass filter slope mode
           0: 6 dB/oct
           1: 12 dB/oct
           2: 18 dB/oct
           3: 24 dB/oct
        '''
        return int(self.command('OFSL?'))

    @slope.setter
    def slope(self, value):
        self.write('OFSL %d' % np.clip(int(value), 0, 3))

    @property
    def synchronous(self):
        '''Synchronous filter mode
           Used if detection frequency is less than 200 Hz
           0: Off
           1: On
        '''
        return int(self.command('SYNC?'))

    @synchronous.setter
    def synchronous(self, value):
        self.write('SYNC %d' % np.clip(int(value), 0, 1))

    # Display and output commands

    # Setup commands

    # Auto functions
    def autoGain(self):
        self.write('AGAN')

    def autoReserve(self):
        self.write('ARSV')

    def autoPhase(self):
        self.write('APHS')

    def autoOffset(self, channel):
        c = np.clip(int(channel), 1, 3)
        self.write('AOFF %d' % c)

    # Data storage commmands

    # Data transfer commands
    def x(self):
        return float(self.command('OUTP?1'))

    def y(self):
        return float(self.command('OUTP?2'))

    def r(self):
        return float(self.command('OUTP?3'))

    def theta(self):
        return float(self.command('OUTP?4'))

    def channel1(self):
        return float(self.command('OUTR?1'))

    def channel2(self):
        return float(self.command('OUTR?2'))

    def snap(self, a, b):
        """Return multiple readings simultaneously:
           1: X
           2: Y
           3: R
           4: theta
           5: Aux In 1
           6: Aux In 2
           7: Aux In 3
           8: Aux In 4
           9: Reference frequency
           10: Channel 1 display
           11: Channel 2 display
        NOTE: can obtain up to 6 readings
        """
        res = self.command('SNAP?%d,%d' %
                           (np.clip(int(a), 1, 11),
                            np.clip(int(b), 1, 11)))
        va, vb = res.split(',')
        return float(va), float(vb)

    @property
    def data(self):
        return self.snap(3, 4)

    # Status reporting commands
    def clearStatusRegisters(self):
        '''Clear status regiesters except status enable registers'''
        self.write('*CLS')

    def status(self):
        '''Read status byte'''
        res = self.command('*STB?')
        return np.uint8(res)

    def error(self):
        '''Read error status byte'''
        res = self.command('ERRS?')
        return np.uint8(res)
