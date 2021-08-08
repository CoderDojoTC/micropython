# rotary-encoder-display-plot-test.py
from rotary import Rotary
import utime as time
from machine import Pin

import ssd1306
# display setup
WIDTH = 128
HEIGHT = 64
HALF_HEIGHT = 32
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0, sck=clock, mosi=data)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

rotary = Rotary(16, 17, 22)
x = 0
val = 0

def rotary_changed(change):
    global val, x
    # oled.fill(0)
    oled.pixel(x % WIDTH, HALF_HEIGHT -val, 1)
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
    elif change == Rotary.SW_PRESS:
        print('Button pressed to clear screen')
        oled.fill(0)
        x = 0
        val = 0
        oled.pixel(0, HALF_HEIGHT, 1)
    oled.show()
    x += 1
    
rotary.add_handler(rotary_changed)

oled.fill(0)
oled.text('Rotery encoder', 0, 0, 1)
oled.text('Plot test', 0, 10, 1)
oled.text('Press to clear', 0, 20, 1)
oled.show()
time.sleep(2)
oled.fill(0)
oled.pixel(0, HALF_HEIGHT, 1)
oled.show()

while True:
    time.sleep(0.1)