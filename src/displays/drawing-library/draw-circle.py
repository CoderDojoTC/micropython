from machine import Pin
from utime import sleep
from math import sqrt
import ssd1306

WIDTH = 128
HEIGHT = 64
clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def circle(cx, cy, r, color):
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

HALF_WIDTH = int(WIDTH/2)
HALF_HEIGHT = int(HEIGHT/2)
while True:
    for rad in range(1,HALF_HEIGHT+2):
        circle(HALF_WIDTH, HALF_HEIGHT, rad, 1)
        oled.show()
        sleep(.1)
    sleep(3)
    oled.fill(1)
    for rad in range(1,HALF_HEIGHT+2):
        circle(HALF_WIDTH, HALF_HEIGHT, rad, 0)
        oled.show()
        sleep(.1)
    oled.fill(0)
    sleep(3)