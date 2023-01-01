from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 10

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # red is 10 of 255
    strip[NUMBER_PIXELS-1] = (255,0,0)

    # turn on for 1/2 second
    strip.write()
    sleep(.25)

    # turn off for 1/2 second
    strip[NUMBER_PIXELS-1] = (0,0,0)
    strip.write()
    sleep(.25)