from machine import Pin, I2C
import VL53L0X
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 12
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

sda=machine.Pin(16) # lower right pin
scl=machine.Pin(17) # one up from lower right pin
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)
tof.start()

while True:
    dist = round((tof.read() - 30) / 2)
    print(dist)
    index = round(dist / 20)
    if index < 0:
        index = 0
    if index > 11:
        index = 11
    strip[index] = (255,0,255)
    strip.write()
    sleep(0.1)
    strip[index] = (0,0,0)
