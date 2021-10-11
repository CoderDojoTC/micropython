"""
hello.py
    Writes "Hello!" in random colors at random locations on a
    ST7789 display connected to a Raspberry Pi Pico.
    Pico Pin   Display
    =========  =======
    14 (GP10)  BL
    15 (GP11)  RST
    16 (GP12)  DC
    17 (GP13)  CS
    18 (GND)   GND
    19 (GP14)  CLK
    20 (GP15)  DIN
"""
import random
from machine import Pin, SPI
import st7789

import vga1_bold_16x32 as font

spi = SPI(1, baudrate=31250000, sck=Pin(14), mosi=Pin(15))
tft = st7789.ST7789(spi, 240, 320,
    reset=Pin(11, Pin.OUT),
    cs=Pin(13, Pin.OUT),
    dc=Pin(12, Pin.OUT),
    backlight=Pin(10, Pin.OUT),
    rotation=3)

tft.init()
tft.text(font, "Hello World!",10, 0, st7789.color565(255,255,255), st7789.color565(0,0,0))
tft.text(font, "Hello World!",10, 50, st7789.color565(255,0,0), st7789.color565(0,0,0))
tft.text(font, "Hello World!",10, 100, st7789.color565(0,255,0), st7789.color565(0,0,0))
tft.text(font, "Hello World!",10, 150, st7789.color565(0,0,255), st7789.color565(0,0,0))
