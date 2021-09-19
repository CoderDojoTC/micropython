# Rotary Encoder Display Test
# I am getting ocassional errors
# Traceback (most recent call last):
#  File "rotary.py", line 35, in rotary_change
# RuntimeError: schedule queue full

from rotary import Rotary
from utime import sleep
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
mode = 0
button_state = 0

def rotary_changed(change):
    global mode, button_state
    if change == Rotary.ROT_CW:
        mode += 1
    elif change == Rotary.ROT_CCW:
        mode -=  1
    # note these are reversed since we have the middle pin on 3.3v
    elif change == Rotary.SW_PRESS:
        button_state = 0
    elif change == Rotary.SW_RELEASE:
        button_state = 1

rotary.add_handler(rotary_changed)

def update_display():
    global mode
    oled.fill(0)
    oled.text('Rotery Encoder', 0, 0, 1)
    oled.text('Display Test', 0, 10, 1)
    oled.text('Mode:', 0, 30, 1)
    oled.text(str(mode), 50, 30, 1)
    oled.text('Button State:', 0, 40, 1)
    oled.text(str(button_state), 110, 40, 1)
    oled.text('Counter: ', 0, 50, 1)
    oled.text(str(counter), 70, 50, 1)
    oled.show()

print('Rotary Encoder Display Test')

current_mode = mode
current_button = button_state
print('mode:', mode)
print('button:', button_state)
counter = 0
while True:
    update_display()
    # only print on change
    if current_mode != mode:
        print('mode:', mode)
        current_mode = mode
    if current_button != button_state:
        print('button:', button_state)
        current_button = button_state
    sleep(0.1)
    counter += 1