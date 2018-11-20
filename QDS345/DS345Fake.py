# -*- coding: utf-8 -*-


class DS345Fake(object):
    '''Abstraction for a placeholder function generator

    This model is useful when no real function generator is
    attached to the instrument.
    '''

    def __init__(self):
        self.identification = 'Fake DS345 Function Generator'
        self.amplitude = 1.
        self.frequency = 1.
        self.offset = 0.
        self.phase = 0.
        self.waveform = 0
        self.invert = 0
        self.mute = False

    def busy(self):
        return False
