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
CIRCLE8 = [
    [ 0, 0, 0, 1, 1, 0, 0, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 0, 1, 1, 0, 0, 0],
]

CIRCLE16 = [
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]
]

# convert the bit array into a byte array
cba8 = bytearray()
for row in CIRCLE8:
    byte = 0
    for bit in row:
        byte = (byte << 1) | bit
    cba8.append(byte)

circle_buf_8 = framebuf.FrameBuffer(cba8, 8, 8, framebuf.MONO_HLSB)

cba16 = bytearray()
row_count = len(CIRCLE16)
col_count = int(len(CIRCLE16[0]) / 8) # eight bits in a byte
print('rows:', row_count, ' 8-byte columns:', col_count, sep='')
for row in range(0, row_count):
    for col in range(0, col_count):
        print('at (', row, ',', col, ') ', sep='', end='')
        byte = 0
        for bit in range(8):
            print(CIRCLE16[row][col*8+bit], end='')
            byte = (byte << 1) | CIRCLE16[row][col*8+bit]
        cba16.append(byte)
        print('')

print("length of CIRCLE8:", len(CIRCLE8))
print("length of cba8:", len(cba8))
print(cba8)
print("length of CIRCLE16:", len(CIRCLE16))
print("length of cba16 should be 32 bytes:", len(cba16))
print(cba16)

circle_buf_16 = framebuf.FrameBuffer(cba16, 16, 16, framebuf.MONO_HLSB)

oled.fill(0)
start = ticks_us()
oled.blit(circle_buf_8, 10, 10)
oled.blit(circle_buf_8, 20, 10)
oled.blit(circle_buf_8, 30, 10)
oled.blit(circle_buf_16, 64, 30)
oled.blit(circle_buf_16, 100, 45)
end1 = ticks_us()
oled.show()
end2 = ticks_us()
print('Blit time:', end1 - start)
print('Show time:', end2 - start)

