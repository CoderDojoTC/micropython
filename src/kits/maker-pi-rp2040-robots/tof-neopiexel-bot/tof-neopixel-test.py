# Test program for VL53L0X

from machine import Pin, I2C
import VL53L0X
from utime import sleep
from neopixel import Neopixel

NUMBER_PIXELS = 20
STATE_MACHINE = 0
LED_PIN = 16
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

# Grove Connector 1
sda=machine.Pin(0) # white Grove wire
scl=machine.Pin(1) # yellow Grove wire
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

tof = VL53L0X.VL53L0X(i2c)

# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def valmap(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

MIN_DIST = 50
max_dist = 0
tof.start()
while True:
    dist = tof.read()
    if dist < 8000: # values over 8000 are no signal
        if dist > max_dist:
            max_dist = dist
        index = valmap(dist, 50, max_dist, 0, 19)
        print(dist, index)
        strip.set_pixel(index, (255,0,0))
        strip.show()
        sleep(.05) # below this we get a flicker
        strip.set_pixel(index, (0,0,0))
        strip.show()
