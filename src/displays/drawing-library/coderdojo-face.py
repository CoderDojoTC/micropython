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
    print('cx=', cx, ' cy=', cy, ' r=', r, sep='')
    diameter = r*2
    oled.pixel(cx, cy, 1)
    # outline the circile
    #oled.rect(cx-r, cy-r, r*2, r*2, 1)
    upper_left_x = cx - r
    upper_left_y = cy - r

    print('ul-x=', upper_left_x, ' ul-y=', upper_left_y, ' d=', diameter, sep='')
    
    # scan through all pixels and only turn on pixels within r of the center
    for i in range(upper_left_x, upper_left_x + diameter):
        for j in range(upper_left_y, upper_left_y + diameter):
            # distance of the current point (i, j) from the center (cx, cy)
            d = sqrt( (i - cx) ** 2 + (j - cy) ** 2 )
            fill = 0
            if d < r:
                oled.pixel(i, j, color)
                fill = 1
            # print(i, j, d, fill)

oled.text('CoderDojo Rocks!', 0, 0, 1)

# left eye
draw_circle(40, 30, 15, 1)
draw_circle(40, 30, 5, 0)
# right eye
draw_circle(80, 30, 15, 1)
draw_circle(80, 30, 5, 0)

oled.fill_rect(35, 50, 10, 5, 1)
oled.fill_rect(75, 50, 10, 5, 1)
oled.fill_rect(40, 55, 40, 5, 1)

oled.show()