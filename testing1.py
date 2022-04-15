import time

import serial
device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-4', baudrate=9600,timeout=5)
device_handler_3.flushInput()
device_handler_3.write(b'a')
val=device_handler_3.readline().decode().strip()
val=float(val)
if val < 0.25:
    val = 0
else:
    val= 1
print(val)
device_handler_3.close()
