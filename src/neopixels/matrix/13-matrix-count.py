import machine
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 256
PERCENT_COLOR_WHEEL = round(255/NUMBER_PIXELS)

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
delay = .05
brightness = 20
counter = 0
while True:
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (brightness, 0 ,0)
        if i > 0:
            strip[i-1] = (0, 0 ,0)
        strip.write()
        sleep(delay)
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0, brightness ,0)
        if i > 0:
            strip[i-1] = (0, 0 ,0)
        strip.write()
        sleep(delay)
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0, 0 ,brightness)
        if i > 0:
            strip[i-1] = (0, 0 ,0)
        strip.write()
        sleep(delay)

