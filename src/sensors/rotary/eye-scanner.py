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

# draw readability
ON = 1
OFF = 0
NO_FILL = 0
FILL = 1


clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)


# copy onto display

bottom_row_text_vpos = 57

def draw_face_grid():
    oled.vline(QUARTER_WIDTH, 0, HEIGHT, 1) # x, y, len, color
    oled.vline(QUARTER_WIDTH*3, 0, HEIGHT, 1)
    oled.hline(0, ONE_THIRD_HEIGHT, WIDTH, 1)

phm = 18 # puple horizontal movement
eye_dist_from_top = 21
eyeWidth = 27
eyeHeight = 10
mouth_vpos = 45
mouth_width = 40

def draw_face(eye_direction):
    oled.fill(0)
    # draw_face_grid()
    start = ticks_us()
    # left eye
    oled.ellipse(32, eye_dist_from_top, eyeWidth, eyeHeight, ON, FILL)
    oled.ellipse(32+i, eye_dist_from_top, 5, 5, OFF, FILL)
    # right eye
    oled.ellipse(94, eye_dist_from_top, eyeWidth, eyeHeight, ON, FILL)
    oled.ellipse(94+i, eye_dist_from_top, 5, 5, OFF, FILL)
    # draw mouth
    # draw bottom half by doing a bitwise and of 8 and 4
    oled.ellipse(HALF_WIDTH, mouth_vpos, mouth_width, 10, ON, NO_FILL, 12)
    end = ticks_us()
    drawTime = end - start
    oled.text(str(drawTime), 0, bottom_row_text_vpos)
    oled.show()
    
while True:
    for i in range(-phm, phm):
        draw_face(i)
        sleep(.005)
    for i in range(phm, -phm, -1):
        draw_face(i)
        sleep(.005)

