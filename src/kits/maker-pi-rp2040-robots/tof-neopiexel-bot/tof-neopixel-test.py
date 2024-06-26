# Test program for VL53L0X

from machine import Pin, I2C
import VL53L0X
from utime import sleep
from neopixel import NeoPixel

NEOPIXEL_PIN = 12
NUMBER_PIXELS = 8

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Grove Connector 4
I2C0_SDA_PIN = 26
I2C0_SCL_PIN = 27
i2c=machine.I2C(1,sda=machine.Pin(I2C0_SDA_PIN), scl=machine.Pin(I2C0_SCL_PIN), freq=400000)

tof = VL53L0X.VL53L0X(i2c)

# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def valmap(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

MIN_DIST = 30
MAX_DIST = 300
tof.start()
while True:
    dist = tof.read() - MIN_DIST
    if dist > MAX_DIST: 
        dist = 300
    index = valmap(dist, MIN_DIST, MAX_DIST, 0, NUMBER_PIXELS-1)
    print(dist, index)
    strip[index] = (255,0,0)
    strip.write()
    sleep(.05) # below this we get a flicker
    strip[index] = (0,0,0)
    strip.write()
