# -*- coding: utf-8 -*-

import serial
from serial.tools.list_ports import comports
import fcntl
import atexit

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


class SerialDevice(object):
    '''
    Abstraction of an instrument connected to a serial port

    ...

    Attributes
    ----------
    eol : str, optional
        End-of-line character.
        Default: '\r' (carriage return)
    manufacturer : str, optional
        Identifier for the serial interface manufacturer.
        Default: 'Prolific'
    baudrate : int, optional
        Baud rate for serial communication.
        Default: 9600
    parity : int, optional
        One of the constants defined in the serial package
    stopbits : int, optional
        One of the constants defined in the serial package
    timeout : float
        Read timeout period [s].
        Default: 0.1

    Methods
    -------
    find() : bool
        Find the serial device that satisfies identify().
        Returns True if the device is found and correctly opened.
    identify() : bool
        Returns True if the device on the opened port correctly
        identifies itself.  Subclasses must override this method.
    close()
        Close serial device
    write(str)
        Write str to serial device and flush serial port.
    readln()
        Read data from the serial port until EOL character.
    available() : bool
        True if characters are available for reading.
    command(cmd) : string
        Send cmd to device and return response as string.
    busy() : bool
        Returns True if the device is executing a command.
        This method should be implemented by a subclass.
    error() : bool
        Returns True if the device has encountered an error.
        This method should be implemented by a subclass.
    '''

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
        '''
        Attempt to identify and open the serial port

        Returns
        -------
        find : bool
            True if port identified and successfully opened.
        '''
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
                logger.info('Trying {}'.format(port.device))
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
                    self.ser.flushInput()
                    self.ser.flushOutput()
                else:
                    logger.warning('Could not open {}'.format(self.ser.port))
                    continue
            except serial.SerialException as ex:
                logger.warning('{} is unavailable: {}'.format(port, ex))
                continue
            if self.identify():
                atexit.register(self.close)
                return True
            self.ser.close()
        return False

    def identify(self):
        '''
        Identify this device

        Subclasses must override this method

        Returns
        -------
        identify : bool
            True if attached device correctly identifies itself.
        '''
        return False

    def close(self):
        '''Close serial device'''
        self.ser.close()

    def write(self, str):
        '''
        Write string to serial device

        Parameters
        ----------
        str : string
            String to be transferred
        '''
        logger.debug('write: {}'.format(str))
        self.ser.write((str + self.eol).encode())
        self.ser.flush()

    def readln(self):
        '''
        Read one line from serial port

        Returns
        -------
        str : string
            Available data from serial port
        '''
        str = self.ser.read_until(terminator=self.eol)
        str = str.decode().strip()
        logger.debug('read: {}'.format(str))
        return str

    def available(self):
        '''
        Return True if serial characters are available
        '''
        return self.ser.in_waiting

    def command(self, cmd):
        '''
        Send command to device and return response

        Returns
        -------
        response : string
            Response from device
        '''
        self.write(cmd)
        return self.readln()

    def busy(self):
        '''
        Return True if device is executing a command

        A subclass can override this method.
        '''
        return False

    def error(self):
        '''
        Return True if device has an error condition

        A subclass can override this method.
        '''
        return False
