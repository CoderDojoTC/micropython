import time
from neopixel import Neopixel

numpix = 72
strip = Neopixel(numpix, 0, 0, "GRB")

red = (255, 0, 0)
orange = (255, 150, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
colors = (red, orange, yellow, green, blue, indigo, violet)

strip.brightness(255)

def color_wipe():
    for color in colors:
        for i in range(numpix):
            strip.set_pixel(i, color)
            strip.show()
            time.sleep(0.01)

def color_wipe_2():
    for color in colors:
        for i in range(12):
            strip.set_pixel(i, color)
            strip.set_pixel(i+12, color)
            strip.set_pixel(i+24, color)
            strip.set_pixel(i+36, color)
            strip.set_pixel(i+48, color)
            strip.set_pixel(i+60, color)
            strip.show()
            time.sleep(0.01)

def color_wipe_3():
    for color in colors:
        for i in range(12):
            strip.set_pixel(i, color)
            strip.set_pixel(23-i, color)
            strip.set_pixel(i+24, color)
            strip.set_pixel(47-i, color)
            strip.set_pixel(48+i, color)
            strip.set_pixel(71-i, color)
            strip.show()
            time.sleep(0.3)

# offset is the color to start (0 to 6)
# dir is 1 for forward and -1 for reverse
def color_wipe_4(offset, dir):
    for i in range(12):
        if dir == 1:
            this_color = colors[ ((i-offset) %7 )]
        else:
            this_color = colors[ ((i+offset) %7 )]
        strip.set_pixel(i, this_color)
        strip.set_pixel(23-i, this_color)
        strip.set_pixel(i+24, this_color)
        strip.set_pixel(47-i, this_color)
        strip.set_pixel(48+i, this_color)
        strip.set_pixel(71-i, this_color)
        strip.show()
        # time.sleep(0.01)
            
while True:
    for counter in range(100):
        color_wipe_4(counter %7, 1)
    for counter in range(100):
        color_wipe_4(counter%7, -1)  