from machine import I2C 
from time import sleep
import VL53L0X

sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=I2C(0, sda=sda, scl=scl)

# Create a VL53L0X object time of flight distance sensor object
tof = VL53L0X.VL53L0X(i2c)
MAX_RANGE = 1200

tof.start()
while True:
    tof_value = tof.read()
    if tof_value < MAX_RANGE  :
        dist = (tof_value - 30) * .5
        print('value =', tof_value, ' dist=', dist)
        sleep(.5)
    else:
        print(tof_value, ' out of range')
    
