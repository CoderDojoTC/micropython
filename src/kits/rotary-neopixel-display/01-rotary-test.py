from machine import Pin
from rotary import Rotary
from time import sleep

# GPIO Pins 16 and 17 are for the encoder pins. 18 is the button press switch.
ENCODER_A = 15
ENCODER_B = 14
SWITCH = 17
rotary = Rotary(ENCODER_A, ENCODER_B, SWITCH)
val = 0

# this function is called whenever the rotory is changed
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
    sleep(0.1)