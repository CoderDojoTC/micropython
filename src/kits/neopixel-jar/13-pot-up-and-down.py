from machine import ADC, Pin
from utime import sleep
from neopixel import NeoPixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

pot = ADC(26) 
while True:
    # shift the reading 8 bits to the right to be 0 to 255
    val = pot.read_u16() >> 8
    pixel = round(NUMBER_PIXELS * (val/255))
    print(val, pixel)
    for i in range(0, pixel):
        strip[i] = (80, 25, 0)
    for i in range(pixel, NUMBER_PIXELS):
        strip[i] = (0, 0, 50)
    strip.write()
