# print out "Hello World!" using the rotation=3 using 32-bit high font
# the default is white text on a black background
from ili934x import ILI9341
from machine import Pin, SPI
import tt32

# Use these PIN definitions.  SCK must be on 2 and data (SDL) on 3
SCK_PIN = 2
MOSI_PIN = 3 # labeled SDI(MOSI) on the back of the display
DC_PIN = 4
RESET_PIN = 5
CS_PIN = 6

# mosi=Pin(23)
# miso=Pin(MISO_PIN)
spi = SPI(0, baudrate=20000000, mosi=Pin(MOSI_PIN),sck=Pin(SCK_PIN))
display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RESET_PIN), w=320, h=240, r=3)
display.erase()
display.set_font(tt32)
display.set_pos(0,0)
display.print('Hello World!')
