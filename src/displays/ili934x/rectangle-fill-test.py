from ili934x import ILI9341, color565
from machine import Pin, SPI
from utime import sleep
from random import randint

WIDTH = 320
HALF_WIDTH = int(WIDTH/2)
HEIGHT = 240
HALF_HEIGHT = int(HEIGHT/2)
ROTATION = 3 # landscape with 0,0 in upper left and pins on left

SCK_PIN = 2
MISO_PIN = 3
DC_PIN = 4
RST_PIN = 5
CS_PIN = 6

# mosi=Pin(23)
# miso=Pin(MISO_PIN)
spi = SPI(0, baudrate=20000000, mosi=Pin(MISO_PIN), sck=Pin(SCK_PIN))
display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RST_PIN), w=WIDTH, h=HEIGHT, r=ROTATION)
display.erase()

# color defintions converted to 565 represnetations
black = color565(0, 0, 0)
white = color565(255, 255, 255)
red = color565(255, 0, 0)
green = color565(0, 255, 0)
blue = color565(0, 0, 255)
yellow = color565(255, 255, 0)
cyan = color565(0, 255, 255)
magenta = color565(255, 0, 255)
gray = color565(128, 128, 128)
light_gray = color565(192, 192, 192)
dark_gray = color565(64, 64, 64)
brown = color565(165, 42, 42)
orange = color565(255, 60, 0)
# 150 for the green and blue wash out the colors
pink = color565(255, 130, 130)
purple = color565(128, 0, 128)
lavender = color565(150, 150, 200)
beige = color565(200, 200, 150)
# by definition, maroon is 50% of the red on, but 128 is way too bright
maroon = color565(105, 0, 0)
olive = color565(128, 128, 0)
turquoise = color565(64, 224, 208)
dark_green = color565(0,100,0)
color_list = [white, red, green, blue, yellow, cyan, magenta,
              gray, light_gray, dark_gray, brown, orange, pink, purple, lavender,
              beige, maroon, olive, turquoise, dark_green, black]
color_num = len(color_list)

# Draw forever
while True:
    # rect_fill(x, y, width, height, color)
    x = randint(0, HALF_WIDTH)
    y = randint(0, HALF_HEIGHT)
    width = randint(0, HALF_WIDTH)
    height = randint(0, HALF_HEIGHT)
    color = color_list[randint(0, color_num-1)]
    print('fill_rectangle(', x, y, width, height, color)
    display.fill_rectangle(x, y, width, height, color)