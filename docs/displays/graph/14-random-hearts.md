# Draw Random Hearts

This program uses the MicroPython ```urandom``` library to generate random X and Y positions on the display.  It then uses an array of binary values to draw a heart icon at that location.

```py
from machine import Pin, PWM, SPI
import urandom
import ssd1306
from utime import sleep
import random # random direction for new ball

WIDTH = 128
HEIGHT = 64
CS = machine.Pin(1)
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
DC = machine.Pin(4)
RES = machine.Pin(5)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

HEART = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

def draw_heart(xofs, yofs):
    for y, row in enumerate(HEART):
        for x, c in enumerate(row):
            oled.pixel(x + xofs, y + yofs, c)

def random_heart():
    xofs = urandom.getrandbits(7)
    yofs = urandom.getrandbits(6)
    print(xofs, yofs)
    draw_heart(xofs, yofs)


oled.fill(0)
for n in range(10):
    random_heart()

oled.show()
```