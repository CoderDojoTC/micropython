from ili934x import ILI9341, color565
from machine import Pin, SPI
from utime import sleep
# use a very small 5x7 font
import glcdfont

SCK_PIN = 2
MISO_PIN = 3
DC_PIN = 4
RST_PIN = 5
CS_PIN = 6

# mosi=Pin(23)
# miso=Pin(MISO_PIN)
spi = SPI(0, baudrate=20000000, mosi=Pin(MISO_PIN),sck=Pin(SCK_PIN))
display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RST_PIN), w=320, h=240, r=3)
display.erase()
# use the largest 32-bit font
display.set_font(glcdfont)

# color defintions convered to 565 represnetations
black = color565(0, 0, 0)
white = color565(255, 255, 255)
red = color565(255, 0, 0)
green = color565(0, 255, 0)
blue = color565(0, 0, 255)

# the default is white on black
display.set_pos(0,0)
display.print('Hello World!')

display.set_color(red, black)
display.set_pos(0,40)
display.print('Hello World Red!')

display.set_color(green, black)
display.set_pos(0,80)
display.print('Hello World Green!')

display.set_color(blue, black)
display.set_pos(0,120)
display.print('Hello World Blue!')

display.set_color(red, white)
display.set_pos(0,160)
display.print('Red')

display.set_color(green, white)
display.set_pos(100,160)
display.print('Green')

display.set_color(blue, white)
display.set_pos(230,160)
display.print('Blue')