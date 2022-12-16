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


# draw_circle(10, 20, 5, 1)
oled.rect(0, 0, 128, 64, 1)
oled.show()

# oled.rect(50-6, 10-6, 12, 12, 1)
draw_circle(20, 20, 4, 1)
draw_circle(40, 30, 10, 1)
draw_circle(70, 40, 5, 1)
draw_circle(100, 20, 15, 1)
draw_circle(100, 20, 5, 0)
oled.show()