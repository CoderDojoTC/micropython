# VL53L0X Display Test

import time
from machine import Pin
from machine import I2C
import VL53L0X
import sh1106

sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.rotate(1)


# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

#tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)

#tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)

while True:
# Start ranging
    tof.start()
    display.fill(0)
    display.text('Distance:', 0, 0, 1)
    display.text(str(tof.read()), 20, 20, 1)
    display.show()
    tof.stop()
    






    #q = tof.set_signal_rate_limit(0.1)
    #
    # time.sleep(0.1)
