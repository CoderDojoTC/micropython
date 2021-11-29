# Test program for VL53L0X
import time
from machine import Pin
from machine import I2C
import VL53L0X

sda=machine.Pin(2) # lower right pin
scl=machine.Pin(3) # one up from lower right pin
i2c=machine.I2C(1, sda=sda, scl=scl, freq=400000)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

while True:
    tof.start()
    tof.read()
    print(tof.read())
    tof.stop()
    time.sleep(0.1)