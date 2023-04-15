# This code displays pi image & text on I2C OLED display, then repeats forever.
# Also print out the OLED's I2C address on serial at program start.
# ---
# Connection: SCL = GP1, SDA = GP0
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# 2. Grove OLED Display 0.96 inch (www.cytron.io/p-grove-oled-display-0p96-inch-ssd1315)
# ---
from machine import Pin, I2C
import framebuf
import utime
import ssd1306

WIDTH  = 128
HEIGHT = 64

# default is data on GP7 and clock on GP6

CS = machine.Pin(1)
SCL = machine.Pin(2)
SDA = machine.Pin(3)
DC = machine.Pin(4)
RES = machine.Pin(5)
spi=machine.SPI(0, sck=SCL, mosi=SDA)
# print(spi)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)                # Init oled display

# Raspberry Pi logo as 32x32 bytearray

my_bytearray = (b"\xFF\xFF\xFF\xBF\xDF\xEF\xF7\xFF\xFB\xFF\xFD\xFD\xFE\x0E\xE6\xF6\xF6\x06\xFC\xFD\xF9\xF1\xC3\x03\x07\x0F\x1F\x3F\x7F\xFF\xFF\xFF\x0F\xF9\xFE\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFC\xF9\xFB\xFB\xFC\x7F\x7F\x3F\x1F\x07\x00\x00\x00\x00\x00\x00\x00\x07\xFF\xF0\xDF\x7F\xFF\xFF\xFF\xFF\xFF\x1F\x07\x03\x01\x01\x00\x10\x10\xF0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xE0\xFF\xFF\xFF\xFF\xFD\xFB\xF7\xEF\xEF\xDC\xF0\xA0\x80\x80\x00\x08\x08\x0F\x08\x8E\x80\x80\xC0\xC0\xC0\xE0\xF0\xF8\xFC\xFE\xFF\xFF\xFF")

coderdojo_logo = bytearray(my_bytearray)
fb_len = len(coderdojo_logo)
inv_fb = []

for i in range(0, fb_len):
    inv_fb.append(255 - my_bytearray[i])

inv_fb = bytearray(inv_fb)

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
# Monochrome Horizontal least significant bit encoding is MONO_HLSB
# https://docs.micropython.org/en/latest/library/framebuf.html#framebuf.framebuf.MONO_VLSB
# fb = framebuf.FrameBuffer(pi_logo, 32, 32, framebuf.MONO_HLSB)
fbi = framebuf.FrameBuffer(inv_fb, 32, 32, framebuf.MONO_VLSB)

oled.fill(0)
oled.blit(fbi, 0, 1)
oled.show()

    