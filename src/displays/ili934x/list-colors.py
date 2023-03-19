from ili934x import ILI9341, color565
from machine import Pin, SPI
from utime import sleep
from random import randint
import tt32

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
spi = SPI(0, baudrate=20000000, mosi=Pin(MISO_PIN),sck=Pin(SCK_PIN))
display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RST_PIN), w=WIDTH, h=HEIGHT, r=ROTATION)
display.set_font(tt32)
display.erase()

# color defintions convered to 565 represnetations
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
color_names = ['white (255,255,255)', 'red (255,0,0)', 'green (0,255,0)', 'blue (0,0,255)', 'yellow (255,255,0)',
               'cyan (0,255,255)', 'magenta (255,0,255)',
              'gray (128,128,128)', 'light gray (192,192,192)', 'dark gray (64,64,64)',
               'brown (165,42,42)', 'orange (255,60,0)', 'pink (255,130,130)', 'purple (128,0,128)',
               'lavender (150,150,200)',
              'beige (200,200,150)', 'maroon (105,0,0)', 'olive (128,128,0)', 'turquoise (64,224,208)',
               'dark green (0,100,0)', 'black (0,0,0)']
color_num = len(color_list)

display.fill_rectangle(0, 0, WIDTH, HEIGHT, black)
while True:
    for i in range(0, color_num):
        display.fill_rectangle(0, 0, WIDTH, HEIGHT-33, color_list[i])
        # black behind the white text
        display.fill_rectangle(0, HEIGHT-32, WIDTH, 32, black)
        
        display.set_pos(0,HEIGHT-32)
        display.print(color_names[i])
        print(color_names[i])
        sleep(1)
