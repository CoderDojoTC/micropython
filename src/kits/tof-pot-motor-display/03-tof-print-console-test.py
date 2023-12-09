# Test program for VL53L0X
import time
from machine import Pin
from machine import I2C
import VL53L0X

sda=machine.Pin(0) # lower right pin
scl=machine.Pin(1) # one up from lower right pin
i2c=machine.I2C(0, sda=sda, scl=scl)
print('Device found at decimal address: ', i2c.scan()[0], 'Hex: ', hex(i2c.scan()[0]))
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)
tof.start()

while True:
    print(tof.read())
    time.sleep(0.1)
