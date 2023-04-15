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
def fill_ellipse(x, y, a, b, color):
    x_min = max(0, int(x - a))
    x_max = min(128, int(x + a + 1))
    y_min = max(0, int(y - b))
    y_max = min(64, int(y + b + 1))

    for y_pos in range(y_min, y_max):
        for x_pos in range(x_min, x_max):
            if ((x_pos - x) ** 2 / a ** 2 + (y_pos - y) ** 2 / b ** 2 <= 1):
                oled.pixel(x_pos, y_pos, color)

# oled.rect(50-6, 10-6, 12, 12, 1)
fill_ellipse(20, 20, 4, 8, 1)
fill_ellipse(40, 30, 15, 10, 1)
fill_ellipse(70, 40, 5, 8, 1)
fill_ellipse(100, 20, 15, 20, 1)
fill_ellipse(100, 20, 5, 3, 0)
oled.show()
