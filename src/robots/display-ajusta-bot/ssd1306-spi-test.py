import machine
import ssd1306
from utime import sleep

WIDTH = 128
HEIGHT = 64
clock=machine.Pin(2)
data=machine.Pin(3)

spi=machine.SPI(0,sck=clock, mosi=data)

CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

i=0
while True:
    oled.fill(0)
    oled.text('Hello Dan', 0, 0, 1)
    oled.text(str(i), 0, 10, 1)
    oled.show()
    i += 1
    sleep(1)


    
    