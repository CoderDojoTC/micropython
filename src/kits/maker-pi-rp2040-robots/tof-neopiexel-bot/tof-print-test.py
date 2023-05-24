from machine import I2C 
from time import sleep
import VL53L0X

# Grove connector 4
sda=machine.Pin(26)
scl=machine.Pin(27)
i2c=I2C(1, sda=sda, scl=scl)

print(i2c)

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
    
