from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    strip[0] = (25,0,0) # set first pixel to red
    strip.write() # write to strip
    sleep(.5) # wait 1/2 second
    strip[0] = (0,0,0) # turn off first pixel
    strip.write()
    
    strip[1] = (0,25,0) # set second pixel to green
    strip.write()
    sleep(.5)
    strip[1] = (0,0,0) # turn off second pixel
    strip.write()
    
    strip[2] = (0,0,25) # set first pixel to green
    strip.write()
    sleep(.5)
    strip[2] = (0,0,0) # turn off first pixel
    strip.write()
