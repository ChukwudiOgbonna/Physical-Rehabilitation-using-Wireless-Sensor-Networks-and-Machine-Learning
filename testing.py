import time

import serial
device_handler_3 = serial.Serial(port='/dev/cu.HC-05-DevB-4', baudrate=9600,timeout=0)
device_handler_3.flushInput()
device_handler_3.flushOutput()
while True:                             # runs this loop forever
    time.sleep(.001)                    # delay of 1ms
    val = device_handler_3.readline()                # read complete line from serial output
    while not '\\n'in str(val):         # check if full data is received.
        # This loop is entered only if serial read value doesn't contain \n
        # which indicates end of a sentence.
        # str(val) - val is byte where string operation to check `\\n`
        # can't be performed
        time.sleep(.001)                # delay of 1ms
        temp = device_handler_3.readline()           # check for serial output.
        if not not temp.decode():       # if temp is not empty.
            val = (val.decode()+temp.decode()).encode()
            # requrired to decode, sum, then encode because
            # long values might require multiple passes
    val = val.decode()                  # decoding from bytes
    val = val.strip()
    val = float(val)
    val = abs(val)
    if val < 0.25:
        val = 0
    else:
        valo= 1
    print(right_leg)
    device_handler_3.close()
    # stripping leading and trailing spaces.
    print(val)
time.sleep(0.5)
device_handler_3.write(b'a')
time.sleep(0.5)
right_leg = device_handler_3.readline().decode().strip()
right_leg = float(right_leg)
right_leg=abs(right_leg)
print(right_leg)
if right_leg < 0.25:
    right_leg = 0
else:
    right_leg = 1
print(right_leg)
device_handler_3.close()