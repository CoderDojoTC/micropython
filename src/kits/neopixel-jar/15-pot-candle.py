from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
# https://docs.micropython.org/en/latest/library/random.html
pot = ADC(26)

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def candle(brightness, delay):
    for i in range(0, NUMBER_PIXELS):
        # we can't get any dimmer than this
        if brightness < 4:
            red = 1 
            green = 0
            blue = 0
        # one step from the lowest setting
        elif brightness < 8:
            red = 2 + randint(0,2)
            green = 1
            blue = 0
        # white hot candle on full bright mode
        elif brightness >= 254:
            red = 255
            green = 255
            blue = 255
        # somewhere in the middle with red being 4/5 of the color
        else:
             red = int(brightness * .9) + randint(0,int(brightness/5))
             # keep red from going over max of 255
             if red > 255: red = 255
             green = int(brightness/5) + randint(0,int(brightness/10))
             blue = 0
        print(brightness, red, green, blue)
        strip[randint(0,NUMBER_PIXELS - 1)] = (red, green, blue)
        strip.write()
        sleep(delay)

while True:
    val = pot.read_u16() >> 8
    candle(val, .001)