import time
from neopixel import Neopixel

numpix = 12
strip = Neopixel(numpix, 0, 0, "GRB")

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
colors = (red, orange, yellow, green, blue, indigo, violet)

strip.brightness(255)

while True:
    for color in colors:
        for i in range(numpix):
            strip.set_pixel(i, color)
            strip.show()
            time.sleep(0.1)
            