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
# bit shifting only works when the numbers are a power of 2
HALF_WIDTH = WIDTH >> 1
QUARTER_WIDTH = HALF_WIDTH >> 1
HEIGHT = 64
HALF_HEIGHT = HEIGHT >> 1
QUARTER_HEIGHT = HALF_HEIGHT >> 1
ONE_THIRD_HEIGHT = int(HEIGHT/3)

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# make an fb for an eye
eye = bytearray(QUARTER_WIDTH * 24)
eyeBuf = framebuf.FrameBuffer(eye, 51, 31, framebuf.MONO_HLSB)
fill = 1 # 0 is no fill center
x = 25
y = 15
width = 25
height = 15
eyeBuf.ellipse(x, y, width, height, 1, fill)
eyeBuf.ellipse(x, y, 5, 5, 0, fill)

eye_dist_from_top = 7
# copy onto display

bottom_row_text_vpos = 57

def draw_face_grid():
    oled.vline(QUARTER_WIDTH, 0, HEIGHT, 1) # x, y, len, color
    oled.vline(QUARTER_WIDTH*3, 0, HEIGHT, 1)
    oled.hline(0, ONE_THIRD_HEIGHT, WIDTH, 1)

# while True:
for i in range(0, 1):
    for i in range(0, 1):
        oled.fill(0)
        draw_face_grid()
        start = ticks_us()
        # left eye
        oled.blit(eyeBuf, 7, eye_dist_from_top)
        # right eye
        oled.blit(eyeBuf, 70+i, eye_dist_from_top)
        end = ticks_us()
        drawTime = end - start
        oled.text(str(drawTime), 0, bottom_row_text_vpos)
        oled.show()
        sleep(.1)
#     for i in range(0, 1):
#         oled.fill(0)
#         draw_face_grid()
#         start = ticks_us()
#         # left eye
#         oled.blit(eyeBuf, 32+i, eye_dist_from_top)
#         # right eye
#         oled.blit(eyeBuf, 96+i, eye_dist_from_top)
#         end = ticks_us()
#         drawTime = end - start
#         oled.text(str(drawTime), 0, bottom_row_text_vpos)
#         oled.show()
#         sleep(.1)     
