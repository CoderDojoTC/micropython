from machine import Pin
from utime import sleep, ticks_us
from math import sqrt
import framebuf
import ssd1306
import urandom

WIDTH = 128
HEIGHT = 64

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# create an 8X8 array of bits for drawing a circle
CIRCLE = [
    [ 0, 0, 0, 1, 1, 0, 0, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 0, 1, 1, 0, 0, 0],
]

# convert the bit array into a byte array
circle_bytearray = bytearray()
for row in CIRCLE:
    byte = 0
    for bit in row:
        byte = (byte << 1) | bit
    circle_bytearray.append(byte)

circle_buf = framebuf.FrameBuffer(circle_bytearray, 8, 8, framebuf.MONO_HLSB)

oled.fill(0)
start = ticks_us()
oled.blit(circle_buf, 64, 32)
end1 = ticks_us()
oled.show()
end2 = ticks_us()
# Blit time: 168
# Show time: 2692
print('Blit time:', end1 - start)
print('Show time:', end2 - start)

