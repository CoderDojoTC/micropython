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

circle16 = bytearray(b'\x01\x80\x0f\xf0\x1f\xf8?\xfc\x7f\xfe\x7f\xfe\x7f\xfe\xff\xff\xff\xff\x7f\xfe\x7f\xfe\x7f\xfe?\xfc\x1f\xf8\x0f\xf0\x01\x80')

circle_buf_16 = framebuf.FrameBuffer(circle16, 16, 16, framebuf.MONO_HLSB)

eye_dist_from_top = 20
counter = 0
direction = 1
while True:
    oled.fill(0)
    start1 = ticks_us()
    oled.blit(circle_buf_16, 32+counter, eye_dist_from_top)
    oled.blit(circle_buf_16, 96+counter, eye_dist_from_top)
    end1 = ticks_us()
    start2 = ticks_us()
    oled.show()
    end2 = ticks_us()
    if counter > 16:
        direction = -1
    elif counter < -30:
        direction = 1
    counter = counter + direction
    sleep(.05)
    blit_time = end1 - start1
    show_time = end2 - start2
    print('blit time:', blit_time, 'show time:', show_time)
    print('blit to show ratio:', round(blit_time /  show_time, 2))


