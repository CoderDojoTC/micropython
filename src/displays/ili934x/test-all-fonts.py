# test of printing multiple fonts to the ILI9341 on an M5Stack using H/W SP
# MIT License; Copyright (c) 2017 Jeffrey N. Magee

from ili934x import ILI9341, color565
from machine import Pin, SPI
import glcdfont
import tt14
import tt24
import tt32

# Use these PIN definitions.  SCK must be on 2 and data (SDL) on 3
SCK_PIN = const(2)
MISO_PIN = const(3) # labeled SDI(MOSI) on the back of the display
DC_PIN = const(4)
RESET_PIN = const(5)
CS_PIN = const(6)

# mosi=Pin(23)
# miso=Pin(MISO_PIN)
spi = SPI(0, baudrate=20000000, mosi=Pin(MISO_PIN),sck=Pin(SCK_PIN))
display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RESET_PIN), w=320, h=240, r=3)

fonts = [glcdfont,tt14,tt24,tt32]

text = 'Now is the time for all good men to come to the aid of the party.'

display.erase()
display.set_pos(0,0)
for ff in fonts:
    display.set_font(ff)
    display.print(text)

