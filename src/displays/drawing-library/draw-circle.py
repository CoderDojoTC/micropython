import machine
from utime import sleep
from math import sqrt
from ssd1306 import SSD1306_I2C
OLED_RESET = machine.Pin(15, machine.Pin.OUT)
OLED_RESET.low()
sleep(.1)
OLED_RESET.high()
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))

oled = SSD1306_I2C(128, 64, i2c)

def draw_circle(cx, cy, r, color):
    upper_left_x = cx - r
    upper_left_y = cy - r
    width = r+2
    height = r+2
    
    # scan through all pixels and only turn on pixels within r of the center
    for i in range(0, width):
        for j in range(0, height):
            # distance of the current point from the center (cx, cy)
            d = sqrt( (i - cx) ** 2 + (j - cy) ** 2 )
            if d < r:
                oled.pixel(cx + i, cj + j, color)


def draw_border(cx, cy, r, color):
    upper_left_x = cx - r
    upper_left_y = cy - r
    width = r+2
    height = r+2
    
    oled.rect(upper_left_x, upper_left_y, width, height, 1)
    oled.show()

# draw_circle(10, 20, 5, 1)
oled.rect(0, 0, 128, 64, 1)
oled.show()

draw_circle(50, 30, 8, 1)
oled.show()