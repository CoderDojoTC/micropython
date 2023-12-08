from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 12
NUMBER_PIXELS = 28
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

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

def rainbow_cycle(wait):
    global NUMBER_PIXELS, strip
    for j in range(255):
        for i in range(NUMBER_PIXELS):
            rc_index = (i * 256 // NUMBER_PIXELS) + j
            # print(rc_index)
            strip[i] = wheel(rc_index & 255)
        strip.write()
    sleep(wait)

counter = 0
offset = 0
while True:
    print('Running cycle', counter)
    rainbow_cycle(.05)
    counter += 1