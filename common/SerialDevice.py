# -*- coding: utf-8 -*-

import serial
from serial.tools.list_ports import comports
import io
import fcntl
import atexit

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class SerialDevice(object):

    def __init__(self,
                 eol='\r',
                 manufacturer='Prolific',
                 baudrate=9600,
                 bytesize=serial.EIGHTBITS,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 timeout=0.1):
        self.eol = eol
        self.manufacturer = manufacturer
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        if not self.find():
            raise ValueError('Could not find serial device')

    def find(self):
        ports = list(comports())
        if len(ports) <= 0:
            logger.warning('No serial ports identified')
            return
        for port in ports:
            if port.manufacturer is None:
                continue
            if self.manufacturer not in port.manufacturer:
                continue
            try:
                self.ser = serial.Serial(port.device,
                                         baudrate=self.baudrate,
                                         bytesize=self.bytesize,
                                         parity=self.parity,
                                         stopbits=self.stopbits,
                                         timeout=self.timeout)
                if self.ser.isOpen():
                    try:
                        fcntl.flock(self.ser.fileno(),
                                    fcntl.LOCK_EX | fcntl.LOCK_NB)
                    except IOError:
                        logger.info('{} is busy'.format(self.ser.port))
                        self.ser.close()
                        continue
                else:
                    logger.warning('Could not open {}'.format(self.ser.port))
                    continue
            except serial.SerialException as ex:
                logger.warning('{} is unavailable: {}'.format(port, ex))
                continue
            buffer = io.BufferedRWPair(self.ser, self.ser, 1)
            self.sio = io.TextIOWrapper(buffer, newline=self.eol,
                                        line_buffering=True)
            if self.identify():
                atexit.register(self.close)
                return True
            self.ser.close()
        return False

    def identify(self):
        return False

    def close(self):
        self.ser.close()

    def write(self, str):
        logger.debug(str)
        self.sio.write((str + self.eol).encode())

    def readln(self):
        str = self.sio.readline().decode().strip()
        logger.debug(str)
        return(str)

    def available(self):
        return self.ser.in_waiting

    def command(self, cmd):
        """Send command to device and return response"""
        self.write(cmd)
        return self.readln()

    def busy(self):
        """Return True if device is executing a command

        A subclass can override this method.
        """
        return False

    def error(self):
        """Return True if device has an error condition

        A subclass can override this method.
        """
        return False
