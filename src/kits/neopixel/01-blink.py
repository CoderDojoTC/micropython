from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # brightness is a number from 0 of 255
    strip[0] = (25,0,0) # set first pixel to red
    strip.write() # write to strip
    sleep(.5) # wait 1/5 second
    strip[0] = (0,0,0) # turn off first pixel
    strip.write()
    sleep(.5) # stay off 1/2 second
