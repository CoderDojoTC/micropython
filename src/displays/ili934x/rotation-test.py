from ili934x import ILI9341, color565
from machine import Pin, SPI
from utime import sleep
import tt32

SCK_PIN = 2
MISO_PIN = 3
DC_PIN = 4
RST_PIN = 5
CS_PIN = 6

# mosi=Pin(23)
# miso=Pin(MISO_PIN)
spi = SPI(0, baudrate=20000000, mosi=Pin(MISO_PIN),sck=Pin(SCK_PIN))

while True:
    for r in range(0, 8):
        display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RST_PIN), w=320, h=240, r=r)
        display.erase()
        display.set_font(tt32)
        display.set_pos(0,0)
        display.print('Rotation ' + str(r))
        display.set_pos(0,40)
        display.print('LIL934x')
        sleep(3)
