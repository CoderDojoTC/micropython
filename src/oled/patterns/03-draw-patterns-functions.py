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

equations = ['(x * y) & 64', '(x * y) & 24', '(x * y) & 47']
# 'pow(x, y) < 77', 'pow(x, y) < 214', 'pow(x, y) < 120',
'(x * 2) % (y+1)', '(x * 64) % (y+1)', '(x * 31) % (y+1)'
((x-128) * 64) % (y-128)

((x * y) ** 4) % 7
((x * y) ** 5) % 99
((x * y) ** 9) % 3
(x % y) % 4
(y % x) % 20

             
# '((x * y) ** 4) % 7' grid
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