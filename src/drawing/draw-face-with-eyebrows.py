'''
Test of the MicroPython framebuf poly drawing function

    from array import array
    
    my_array = array('h', [60,10, 50,60, 40,30])
    display.poly(0,0, my_array, ON, FILL)

'''

from machine import Pin
from utime import sleep, ticks_us
from array import array
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
eye_dist_from_top = 25
eyeWidth = 27
eyeWidth_half = int(eyeWidth/2)
eyeHeight = 7
mouth_vpos = 40
mouth_width = 40
pupil_width = 5

left_eyebrow  = array('h', [-eyeWidth_half,-1,      15,-5, eyeWidth_half+10,1,  15,-2])
right_eyebrow = array('h', [-eyeWidth_half-10, 1,  -15,-5, eyeWidth_half,0,    -15,-2])

def draw_eye(x):
    oled.ellipse(x, eye_dist_from_top, eyeWidth, eyeHeight, ON, FILL)
    # draw a black pupil on the white eye
    oled.ellipse(x, eye_dist_from_top, pupil_width, pupil_width, OFF, FILL)


def draw_face(eye_direction):
    
    # draw_face_grid()
    start = ticks_us()
    # left eye
    draw_eye(QUARTER_WIDTH)
    
    # eyebrow
    oled.poly(QUARTER_WIDTH,eye_dist_from_top-10, left_eyebrow, ON, FILL)
    
    # right eye
    draw_eye(QUARTER_WIDTH*3)
    oled.poly(QUARTER_WIDTH*3,eye_dist_from_top-10, right_eyebrow, ON, FILL)
    
    # draw mouth
    # draw bottom half by doing a bitwise and of 8 and 4
    oled.ellipse(HALF_WIDTH, mouth_vpos, mouth_width, 10, ON, NO_FILL, 12)
    end = ticks_us()
    drawTime = end - start
    # oled.text(str(drawTime), 0, bottom_row_text_vpos)
    oled.show()
    
# outline box

oled.fill(0)
oled.rect(0,0, WIDTH, HEIGHT, 1)
draw_face(0)


