from machine import Pin
from utime import sleep
import math
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)

WIDTH = 128
HEIGHT = 64
clock=Pin(2)
data=Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# x and y represent the center of the ellipse
# a represents the semi-major axis,
# and b represents the semi-minor axis.
# The fill_ellipse function checks for each pixel on the screen
# if it falls within the boundaries of the ellipse and
# sets the corresponding pixel on the screen to black if it does.
# The check is done by evaluating the equation of an
# ellipse ((x_pos - x) ** 2 / a ** 2 + (y_pos - y) ** 2 / b ** 2 <= 1).
def fill_circle(x, y, r, color):
    if r == 1:
        oled.pixel(x, y, color)
    else:
        # we adjust the distance to keep the small circles rounded
        r_squared = r ** 2 - 1.1
        x_min = max(0, int(x - r))
        x_max = min(128, int(x + r + 1))
        y_min = max(0, int(y - r))
        y_max = min(64, int(y + r + 1))

        for y_pos in range(y_min, y_max):
            for x_pos in range(x_min, x_max):
                if ((x_pos - x) ** 2 + (y_pos - y) ** 2 <= r_squared):
                    oled.pixel(x_pos, y_pos, color)


for r in range(1, 11):
    x = int(r * r + 1 * r)
    y = r
    fill_circle(x, y, r, 1)

for r in range(11, 16):
    x = int(r * r + 1 * r) - 120
    y = r * 2 + 10
    fill_circle(x, y, r, 1)

oled.show()
