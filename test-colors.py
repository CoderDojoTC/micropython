from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

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

def solid_color(color, delay):
    for i in range(0, NUMBER_PIXELS-1):
        strip[i] = color;
    strip.write()
    sleep(delay)

while True:
    solid_color(red, 1)
    solid_color(white, 1)
    solid_color(blue, 1)

