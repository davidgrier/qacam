# -*- coding: utf-8 -*-
from common.SerialDevice import SerialDevice
import numpy as np
from time import sleep

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Motors(SerialDevice):
    """Control the pair of stepper motors driving a polargraph"""

    def __init__(self):
        super(Motors, self).__init__(eol='\n',
                                     manufacturer='Arduino',
                                     timeout=1)

    def identify(self):
        logger.info('Waiting for Arduino serial port')
        sleep(2)
        res = self.command('Q')
        acam = 'acam2' in res
        logger.info('Arduino running acam2: {}'.format(acam))
        return acam

    def goto(self, n1, n2):
        """Move to index (n1, n2)"""
        self.command('G:%d:%d' % (n1, n2))

    def home(self):
        """Move to home position"""
        self.goto(0, 0)

    def release(self):
        """Stop and release motors"""
        self.command('S')

    def running(self):
        """Returns True if motors are running"""
        try:
            res = self.command('R')
            header, running = res.split(':')
        except Exception as ex:
            logger.warn('Could not read running status: {}'.format(ex))
            running = 0
        return bool(int(running))

    @property
    def indexes(self):
        """Returns current step numbers for motors"""
        try:
            res = self.command('P')
            header, n1, n2 = res.split(':')
            n1 = int(n1)
            n2 = int(n2)
        except Exception as ex:
            logger.warn('Did not read position: {}'.format(ex))
            n1 = 0
            n2 = 0
        return n1, n2

    @indexes.setter
    def indexes(self, n1, n2):
        self.command('P:%d:%d' % (n1, n2))

    @property
    def motor_speed(self):
        """Maximum motor speed in steps/s"""
        try:
            res = self.command('V')
            header, speed = res.split(':')
        except Exception as ex:
            logger.warn('Could not read maximum speed: {}'.format(ex))
            speed = 0
        return float(speed)

    @motor_speed.setter
    def motor_speed(self, speed):
        res = self.command('V:%f' % speed)
        logger.debug('speed: {}'.format(res))


class Polargraph(Motors):
    """Control a polargraph

    The polargraph consists of two stepper motors with GT2 gears
    that translate a GT2 timing belt.  The motors are controlled
    by an Arduino microcontroller that is connected to the host
    computer by USB.  This class communicates with the Arduino to
    obtain programmed motion from the motors.
    """

    def __init__(self,
                 unit=2.,  # size of one timing belt tooth [mm]
                 circumference=25.,  # belt teeth per revolution
                 steps=200.,  # motor steps per revolution
                 ell=1.,  # separation between motors [m]
                 y0=0.1,  # rest displacement from motors' centerline [m]
                 y1=0.,  # vertical start of scan area [m]
                 width=0.6,  # width of scan area [m]
                 height=0.6,  # height of scan area [m]
                 dy=0.005):  # vertical displacement between scan lines [m]

        super(Polargraph, self).__init__()

        # Belt drive
        self.unit = float(unit)
        self.circumference = float(circumference)
        self.steps = float(steps)

        # Motor configuration
        self.ell = float(ell)
        self.y0 = float(y0)

        # Scan configuration
        self.y1 = float(y1)
        self.width = float(width)
        self.height = float(height)
        self.dy = float(dy)

        # distance traveled per step [m]
        self.ds = 1e-3 * self.unit * self.circumference / self.steps
        # distance (length of belt) from motor to payload at home position [m]
        self.s0 = np.sqrt((self.ell / 2.)**2 + (self.y0)**2)

    def goto(self, x, y):
        """Move payload to position (x,y)"""
        s1 = np.sqrt((self.ell / 2. - x)**2 + y**2)
        s2 = np.sqrt((self.ell / 2. + x)**2 + y**2)
        n1 = np.rint((s1 - self.s0) / self.ds).astype(int)
        n2 = np.rint((self.s0 - s2) / self.ds).astype(int)
        super(Polargraph, self).goto(n1, n2)

    @property
    def position(self):
        """Current coordinates in meters"""
        n1, n2 = self.indexes
        s1 = self.s0 + n1*self.ds
        s2 = self.s0 - n2*self.ds
        x = (s2**2 - s1**2)/(2. * self.ell)
        y = np.sqrt((s1**2 + s2**2)/2. - self.ell**2/4. - x**2)
        return x, y

    @property
    def speed(self):
        """Translation speed in mm/s"""
        return self.motor_speed * self.circumference * self.unit / self.steps

    @speed.setter
    def speed(self, value):
        self.motor_speed = value * (self.steps /
                                    (self.circumference * self.unit))
