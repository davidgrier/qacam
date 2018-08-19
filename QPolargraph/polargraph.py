# -*- coding: utf-8 -*-
from common.SerialDevice import SerialDevice
import numpy as np
from time import sleep

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class motors(SerialDevice):
    """Control the pair of stepper motors driving a polargraph"""

    def __init__(self):
        super(motors, self).__init__(eol='\n',
                                     manufacturer='Arduino',
                                     timeout=1)
        self._speed = 500.
        self.n1 = 0
        self.n2 = 0

    def identify(self):
        logger.info('Waiting for Arduino serial port')
        sleep(2)
        self.write('Q')
        acam = 'acam2' in self.readln()
        logger.info('Arduino running acam2: {}'.format(acam))
        return acam

    def goto(self, n1, n2):
        """Move to index (n1, n2)"""
        self.write('M:%d:%d' % (n1, n2))

    def release(self):
        """Stop and release motors"""
        self.write('S')

    def running(self):
        """Returns True if motors are running"""
        self.write('R')
        try:
            header, running = self.readln().split(':')
        except Exception as ex:
            logger.warn('Could not read running status: {}'.format(ex))
            running = 0
        return bool(int(running))

    def steps(self):
        """Returns current step numbers for motors"""
        self.write('P')
        try:
            header, n1, n2 = self.readln().split(':')
            self.n1 = int(n1)
            self.n2 = int(n2)
        except Exception as ex:
            logger.warn('Did not read position: {}'.format(ex))
            self.n1 = 0
            self.n2 = 0
        return self.n1, self.n2

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sends V:speed"""
        self._speed = float(speed)
        self.write('V%f' % self._speed)


class polargraph(motors):
    """Control a polargraph

    The polargraph consists of two stepper motors with GT2 gears
    that translate a GT2 timing belt.  The motors are controlled
    by an Arduino microcontroller that is connected to the host
    computer by USB.  This class communicates with the Arduino to
    obtain programmed motion from the motors.
    """

    def __init__(self,
                 L=1.,  # separation between motors [m]
                 y0=0.1,  # rest displacement from motors' centerline [m]
                 width=0.6,  # width of scan area [m]
                 height=0.6,  # height of scan area [m]
                 step=0.005,  # vertical displacement between scan lines [m]
                 ds=0.00025):  # distance traveled per motor step [m]

        super(polargraph, self).__init__()

        self.L = float(L)
        self.y0 = float(y0)
        self.width = float(width)
        self.height = float(height)
        self.step = float(step)
        self.ds = float(ds)
        # NOTE: GT2 timing belt has 2 mm between teeth.
        # Standard GT2 gears have 25 teeth per revolution,
        # for a total of 50 mm belt translation per revolution.
        # Standard NEMA 17 stepper motors have 200 steps/revolution.
        # This yields a step size of 0.25 mm/step.

        self.s0 = np.sqrt((self.L / 2.)**2 + (self.y0)**2)
        # distance (length of belt) from motor to payload

    def goto(self, x, y):
        """Move payload to position (x,y)"""
        s1 = np.sqrt((self.L / 2. - x)**2 + (y + self.y0)**2)
        s2 = np.sqrt((self.L / 2. + x)**2 + (y + self.y0)**2)
        n1 = np.rint((s1 - self.s0) / self.ds).astype(int)
        n2 = np.rint((self.s0 - s2) / self.ds).astype(int)
        super(polargraph, self).goto(n1, n2)

    def home(self):
        """Move payload to home position"""
        self.goto(0, 0)

    def position(self):
        """Current coordinates in meters"""
        n1, n2 = self.steps()
        s1 = self.s0 + n1*self.ds
        s2 = self.s0 - n2*self.ds
        x = (s2**2 - s1**2)/(2. * self.L)
        y = np.sqrt((s1**2 + s2**2)/2. - self.L**2/4. - x**2) - self.y0
        return x, y


def main():
    a = motors()
    print a.steps(), a.running()


if __name__ == '__main__':
    main()
