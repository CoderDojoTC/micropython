from rotary import Rotary
import utime as time
from machine import Pin

import ssd1306
# display setup
WIDTH = 128
HEIGHT = 64
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0, sck=clock, mosi=data)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

rotary = Rotary(16, 17, 22)
val = 0

def rotary_changed(change):
    global val
    oled.fill(0)
    oled.text('Rotery Encoder', 0, 0, 1)
    oled.text('Display Test', 0, 10, 1)
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
        oled.text(str(val), 0, 30, 1)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
        oled.text(str(val), 0, 30, 1)
    elif change == Rotary.SW_PRESS:
        print('PRESS')
        oled.text('B3 Press', 0, 50, 1) 
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')
        oled.text('B3 Release', 0, 50, 1)
    oled.show()
rotary.add_handler(rotary_changed)

oled.fill(0)
oled.text('Rotery Encoder', 0, 0, 1)
oled.text('Display Test', 0, 10, 1)
oled.show()

while True:
    time.sleep(0.1)