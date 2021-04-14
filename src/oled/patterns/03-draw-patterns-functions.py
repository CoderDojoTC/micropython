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

equations = ['(x ** y) & 64']
save = ['(x * y) & 24', '(x * y) & 47']
             
# '((x * y) ** 4) % 7' grid
def eval_screen(function):
    if eval(function):
        oled.pixel(x, y, 0)
    else:
        oled.pixel(x, y, 1)

oled.fill(0)
for x in range(WIDTH):
    for y in range(HEIGHT):
        eval_screen('(y + x) & 10')
oled.show()
print('done')