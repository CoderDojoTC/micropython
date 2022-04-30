from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # brightness is a number from 0 of 255
    strip[0] = (25,0,0) # set first pixel to red
    strip.write() # write to strip
    sleep(.1) # wait 1/10 second
    strip[0] = (0,0,0) # turn off first pixel
    strip.write()
    sleep(1) # stay off 1 second
