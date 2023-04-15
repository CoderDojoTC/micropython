from machine import Pin
from utime import sleep
from math import sqrt
import ssd1306

WIDTH = 128
HEIGHT = 64

# Do these calculations just once cause we have 264K RAM!
HALF_WIDTH = int(WIDTH/2)
QUARTER_WIDTH = int(WIDTH/4)
HALF_HEIGHT = int(HEIGHT/2)
QUARTER_HEIGHT = int(HEIGHT/4)



clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def fill_circle(cx, cy, r, color):
    diameter = r*2
    upper_left_x = cx - r
    upper_left_y = cy - r 
    # scan through all pixels and only turn on pixels within r of the center
    for i in range(upper_left_x, upper_left_x + diameter):
        for j in range(upper_left_y, upper_left_y + diameter):
            # distance of the current point (i, j) from the center (cx, cy)
            d = sqrt( (i - cx) ** 2 + (j - cy) ** 2 )
            if d < r:
                oled.pixel(i, j, color)

def fill_ellipse(x, y, a, b, color):
    x_min = max(0, int(x - a))
    x_max = min(128, int(x + a + 1))
    y_min = max(0, int(y - b))
    y_max = min(64, int(y + b + 1))

    for y_pos in range(y_min, y_max):
        for x_pos in range(x_min, x_max):
            if ((x_pos - x) ** 2 / a ** 2 + (y_pos - y) ** 2 / b ** 2 <= 1):
                oled.pixel(x_pos, y_pos, color)

# EYE PARAMETERS
EYE_WIDTH = int(WIDTH/5)
EYE_PLACEMENT_Y = int(HEIGHT/3)
EYE_HEIGHT = int(HEIGHT/6)
PUPLE_RADIUS = 5
def draw_eyes(look_offset):
    # outline
    LEFT_EYE_X = QUARTER_WIDTH
    RIGHT_EYE_X = QUARTER_WIDTH*3
    
    fill_ellipse(LEFT_EYE_X, EYE_PLACEMENT_Y, EYE_WIDTH, EYE_HEIGHT, 1)
    fill_ellipse(RIGHT_EYE_X, EYE_PLACEMENT_Y, EYE_WIDTH, EYE_HEIGHT, 1)
    # puples
    fill_circle(LEFT_EYE_X+look_offset, EYE_PLACEMENT_Y, PUPLE_RADIUS, 0)
    fill_circle(RIGHT_EYE_X+look_offset, EYE_PLACEMENT_Y, PUPLE_RADIUS, 0)

delay = .000
while True:
    for look_offset in range(-15, 15, 2):
        draw_eyes(look_offset)
        oled.show()
        sleep(delay)
    for look_offset in range(15, -15, -2):
        draw_eyes(look_offset)
        oled.show()
        sleep(delay)