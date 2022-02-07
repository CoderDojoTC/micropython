# Test program for VL53L0X

from machine import Pin, I2C
import VL53L0X
from utime import sleep

# Grove Connector 1
sda=machine.Pin(0) # white Grove wire
scl=machine.Pin(1) # yellow Grove wire
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

tof = VL53L0X.VL53L0X(i2c)

tof.start()
while True:
    print(tof.read())
    sleep(.1)