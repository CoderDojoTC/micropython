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

my_bytearray = (b'\x00\x00\x00@ \x10\x08\x00\x04\x00\x02\x02\x01\xf1\x19\t\t\xf9\x03\x02\x06\x0e<\xfc\xf8\xf0\xe0\xc0\x80\x00\x00\x00\xf0\x06\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x06\x04\x04\x03\x80\x80\xc0\xe0\xf8\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x0f \x80\x00\x00\x00\x00\x00\xe0\xf8\xfc\xfe\xfe\xff\xef\xef\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x7f\x1f\x00\x00\x00\x00\x02\x04\x08\x10\x10#\x0f_\x7f\x7f\xff\xf7\xf7\xf0\xf7q\x7f\x7f???\x1f\x0f\x07\x03\x01\x00\x00\x00')
coderdojo_logo = bytearray(my_bytearray)


# Load the raspberry pi logo into the framebuffer (the image is 32x32)
# Monochrome Horizontal least significant bit encoding is MONO_HLSB
# https://docs.micropython.org/en/latest/library/framebuf.html#framebuf.framebuf.MONO_VLSB
# fb = framebuf.FrameBuffer(pi_logo, 32, 32, framebuf.MONO_HLSB)
fbi = framebuf.FrameBuffer(coderdojo_logo, 32, 32, framebuf.MONO_VLSB)

oled.fill(0)
oled.blit(fbi, 0, 1)
oled.show()

    