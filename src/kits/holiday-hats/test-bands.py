from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
# This is the best number of pixels for most hats
# if you use 160 pixels/meter strips
NUMBER_PIXELS = 36
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255,0,0)
orange = (255,70,0)
yellow = (255,255,0)
green = (0, 255, 0)
green_med = (0,32, 0)
green_light = (0, 8, 0)
blue = (0,0,255)
off = (0, 0, 0)
orange = (140, 60, 0)
white = (255, 255, 255)
colors = (red, orange, yellow, green, blue)
color_count = len(colors)
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

def three_bands(c, spacing, c1, c2, c3, delay):
    band_length = spacing * 3
    bands = int((NUMBER_PIXELS/ (spacing*3)))
    # print('bands=', bands)
    for i in range(bands): 
        for j in range(spacing):
            index = (i*band_length + j + c) % NUMBER_PIXELS
            #print('red', i,j,c, index)
            if (index) < NUMBER_PIXELS:
                strip[index] = c1
        for j in range(spacing, spacing*2):
            index = (i*band_length + j + c) % NUMBER_PIXELS
            #print('green', i,j,c, index)
            if (index) < NUMBER_PIXELS:
                strip[index] = c2
        for j in range(spacing*2, spacing*3):
            index = (i*band_length + j + c) % NUMBER_PIXELS
            #print('blue', i,j,c, index)
            if (index) < NUMBER_PIXELS:
                strip[index] = c3
        strip.write()
        sleep(delay)

counter = 0
while True:
    three_bands(counter, 3, red, white, blue, 0.04)
    counter += 1
    if counter > NUMBER_PIXELS:
        counter = 0

