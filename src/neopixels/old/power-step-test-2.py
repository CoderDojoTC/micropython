import time
from neopixel import Neopixel

NUMBER_PIXELS = 144
PIXELS_IN_TEST = 20
strip = Neopixel(NUMBER_PIXELS, 0, 0, "GRB")
strip.brightness(1)

def off():
    global NUMBER_PIXELS
    for i in range(0, NUMBER_PIXELS - 1):
        strip.set_pixel(i, (0,0,0))
    strip.show()

while True:
    # turn everything off for a second
    off()
    time.sleep(1)
    for power_level in range(50, 0, -1):
        print('Power Level:', power_level)
        print('Current in milliamps:', power_level*2) # estimate at 2ma on 10% brightness
        for i in range(0, power_level - 1):
            strip.set_pixel(i, (255,0,0))
        strip.show()
        time.sleep(9)
        off()