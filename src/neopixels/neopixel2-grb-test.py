# this is the same as the standard NeoPixel library but with the order of the red and green bytes reversed.
# class NeoPixel2:
# G R B W
# ORDER = (0, 1, 2, 3)
from neopixelgrb import NeoPixel2
from utime import sleep

NEOPIXEL_PIN = 0
# guess the number here
NUMBER_PIXELS = 50

strip = NeoPixel2(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

 
print('Turning the last pixel red:', NUMBER_PIXELS-1)
print('Drawing orange, yellow, green, blue, indigo and violet')

strip[NUMBER_PIXELS-1] = (255,0,0) # red
strip[NUMBER_PIXELS-2] = (128,50,0) # orange
strip[NUMBER_PIXELS-3] = (128,128,0) # yellow
strip[NUMBER_PIXELS-4] = (0,255,0) # green
strip[NUMBER_PIXELS-5] = (0,0,255) # blue
strip[NUMBER_PIXELS-6] = (75,0,130) # indigo or pink
strip[NUMBER_PIXELS-7] = (255,0,255) # violet or purple
strip.write()

        
