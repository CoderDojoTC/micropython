import time
from machine import Pin
from machine import I2C
import VL53L0X

sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)
tof.start() # startup the sensor
while True:
# Start ranging
    dist = tof.read()
    print(dist)
    time.sleep(.1)






    #q = tof.set_signal_rate_limit(0.1)
    #
    # time.sleep(0.1)
