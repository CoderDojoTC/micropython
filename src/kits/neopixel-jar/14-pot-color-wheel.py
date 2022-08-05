from machine import ADC, Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

pot = ADC(26)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)        

while True:
    val = pot.read_u16() >> 8
    for i in range(0, NUMBER_PIXELS):
        color = wheel(val)
        print(color)
        strip[i] = color
        strip.write()

