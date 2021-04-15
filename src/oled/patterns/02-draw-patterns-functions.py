import machine
import ssd1306
from time import sleep

WIDTH = 128
HEIGHT = 64
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def eval_screen(function, x, y):
    if eval(function):
        oled.pixel(x, y, 0)
    else:
        oled.pixel(x, y, 1)

oled.fill(0)

for x in range(WIDTH):
    for y in range(HEIGHT):
        eval_screen('pow(x, y) % 2', x, y)
oled.show()