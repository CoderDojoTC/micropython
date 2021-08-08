from rotary import Rotary
import utime as time
from machine import Pin

config_16 = Pin(16, Pin.IN, Pin.PULL_DOWN)
config_17 = Pin(17, Pin.IN, Pin.PULL_DOWN)

rotary = Rotary(16,17, 22)
val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
    elif change == Rotary.SW_PRESS:
        print('PRESS')
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')
        
rotary.add_handler(rotary_changed)

while True:
    time.sleep(0.1)