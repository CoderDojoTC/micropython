from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

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

# The Change Rate is how quickly the colors change moving down the strip
def rainbow_slide(counter, change_rate, delay):
    for i in range(0, NUMBER_PIXELS):
        # the modulo make sure the color is in range of 0 to 255
        strip[i] = wheel((i*change_rate + counter) % 255)
        strip.write()
    sleep(delay)

def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()

# setup
counter = 0
clear()

# main loop
while True:
    rainbow_slide(counter, 3, .0001)
    counter += 1
    print(counter)
