from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    strip[0] = (25,0,0) # set first pixel to red
    strip[1] = (0,25,0) # set first pixel to green
    strip[2] = (0,0,25) # set first pixel to blue
    strip.write() # write to strip
    sleep(.5) # wait 1/10 second
    strip[0] = (0,0,0) # turn off first pixel
    strip[1] = (0,0,0)
    strip[2] = (0,0,0)
    strip.write()
    sleep(.5) # stay off 1 second
