import sqlite3
import time

import serial

import DatabaseManager

class BluetoothHandler:
    # LEFT HAND
    def calibrateLeftHandForce(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-4', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'a')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 0.5:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()


    def calibrateLeftHandFlex(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-4', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'c')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 35:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()

    def calibrateLeftHandAcceleration(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-4', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'b')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 0.25:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()

    # RIGHT HAND
    def calibrateRightHandForce(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-5', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'a')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 10:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()


    def calibrateRightHandFlex(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-5', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'c')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 35:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()

    def calibrateRightHandAcceleration(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-5', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'b')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 0.25:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()
    # RIGHT LEG

    def calibrateRightLegForce(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'a')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 10:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()

    def calibrateRightLegAcceleration(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'b')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 0.25:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()

    # LEFT LEG

    def calibrateLeftLegForce(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-6', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'a')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 10:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()
    def calibrateLeftLegAcceleration(self):
        device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-6', baudrate=9600, timeout=5)
        device_handler_3.flushInput()
        device_handler_3.write(b'b')
        val = device_handler_3.readline().decode().strip()
        val = float(val)
        if val < 0.25:
            val = 0
        else:
            val = 1
        return val
        device_handler_3.close()

    def exerciseforLeftHandFlex(self):
        self.device_handler_1.open()
        time.sleep(1)
        self.device_handler_1.write(b'd')
        time.sleep(40)
        value=self.device_handler_1.readline().decode().strip()
        return value

    def exerciseforRightHandFlex(self):
        self.device_handler_2.open()
        time.sleep(1)
        self.device_handler_1.write(b'd')
        time.sleep(40)
        value=self.device_handler_1.readline().decode().strip()
        return value

    def exerciseforLeftElbow(self):
        self.device_handler_1.open()
        time.sleep(1)
        self.device_handler_1.write(b'e')
        time.sleep(40)
        value=self.device_handler_1.readline().decode().strip()
        return value

    def exerciseforRightElbow(self):
        self.device_handler_2.open()
        time.sleep(1)
        self.device_handler_1.write(b'e')
        time.sleep(40)
        value=self.device_handler_1.readline().decode().strip()
        return value
    def exerciseForLeftKnee(self):
        self.device_handler_3.open()
        time.sleep(1)
        self.device_handler_3.write(b'f')
        time.sleep(40)
        value= self.device_handler_3.readline().decode().strip()
        return value
    def exerciseForRightKnee(self):
        self.device_handler_4.open()
        time.sleep(1)
        self.device_handler_3.write(b'f')
        time.sleep(40)
        value= self.device_handler_3.readline().decode().strip()
        return value

    def exerciseForLeftSole(self):
        self.device_handler_3.open()
        time.sleep(1)
        self.device_handler_3.write(b'a')
        time.sleep(40)
        value= self.device_handler_3.readline().decode().strip()
        return value
    def exerciseForRightSole(self):
        self.device_handler_4.open()
        time.sleep(1)
        self.device_handler_4.write(b'a')
        time.sleep(40)
        value= self.device_handler_4.readline().decode().strip()
        return value

    def exerciseForRightHandForce(self):
        self.device_handler_2.open()
        time.sleep(1)
        self.device_handler_2.write(b'a')
        time.sleep(40)
        value= self.device_handler_2.readline().decode().strip()
        return value

    def exerciseForLeftHandForce(self):
        self.device_handler_1.open()
        time.sleep(1)
        self.device_handler_1.write(b'a')
        time.sleep(40)
        value= self.device_handler_1.readline().decode().strip()
        return value


import concurrent.futures


def foo(bar):
    print('hello {}'.format(bar))
    return 'foo'


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(foo, 'world!')
    return_value = future.result()
    print(return_value)
