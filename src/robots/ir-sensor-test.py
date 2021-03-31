from machine import Pin
from utime import sleep

left = Pin(8, Pin.IN, Pin.PULL_DOWN)
center = Pin(7, Pin.IN, Pin.PULL_DOWN)
right = Pin(6, Pin.IN, Pin.PULL_DOWN)

while True:
    print('Left:', left.value(), end='')
    print(' Center:', center.value(), end='')
    print(' Right:', right.value())
    sleep(.25)