from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    for i in range(0, NUMBER_PIXELS):
        # red is 10 of 255
        strip[i] = (10,0,0)
        strip.write()
        sleep(.05)
        strip[i] = (0,0,0)
