from machine import Pin
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 2
NEOPIXEL_PIN = 18

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)


while True:
    
    # blink red
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (255,0,0)
    strip.write()
    sleep(.5)

    # blink green
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,255,0)
    strip.write()
    sleep(.5)

    # blink blue
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,255)
    strip.write()
    sleep(.5)
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()
    sleep(.5)