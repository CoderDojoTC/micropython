'''

FrameBuffer.ellipse(x, y, xr, yr, c)

FrameBuffer.ellipse(x, y, xr, yr, c[, f, m])¶
Draw an ellipse at the given location. Radii xr and yr define the geometry; equal values cause 
a circle to be drawn. The c parameter defines the color.

The optional f parameter can be set to True to fill the ellipse. Otherwise just a one 
pixel outline is drawn.

The optional m parameter enables drawing to be restricted to certain quadrants of the ellipse. 
The LS four bits determine which quadrants are to be drawn, with bit 0 specifying Q1, b1 Q2, b2 Q3 
and b3 Q4. 
Quadrants are numbered counterclockwise with Q1 being top right.
'''

from machine import Pin
from utime import sleep, ticks_us
from math import sqrt
import framebuf
import ssd1306

WIDTH = 128
HALF_WIDTH = WIDTH >> 1
QUEATER_WIDTH = HALF_WIDTH >> 1
HEIGHT = 64

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# make an fb for an eye
eye = bytearray(QUEATER_WIDTH * 24)
eyeBuf = framebuf.FrameBuffer(eye, 32, 24, framebuf.MONO_HLSB)
fill = 1
x = 16
y = 12
width = 10
height = 8
eyeBuf.ellipse(x, y, width, height, 1, fill)

eye_dist_from_top = 20
# copy onto display

for i in range(0, 1):
    oled.fill(0)
    start = ticks_us()
    # left eye
    oled.blit(eyeBuf, 32, eye_dist_from_top)
    # right eye
    oled.blit(eyeBuf, 96, eye_dist_from_top)
    end = ticks_us()
    drawTime = end - start
    oled.text(str(drawTime), i, 54)
    oled.show()
    
