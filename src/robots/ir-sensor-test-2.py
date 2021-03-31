from machine import Pin
from utime import sleep

left = Pin(8, Pin.IN, Pin.PULL_DOWN)
center = Pin(7, Pin.IN, Pin.PULL_DOWN)
right = Pin(6, Pin.IN, Pin.PULL_DOWN)

while True:
    if left.value()==0:
        print('Left')
    if center.value()==0:
        print('Center')
    if right.value()==0:
        print('Right')
    # if (left.value()==1) and (center.value()==1) and (right.value()==1):
    if left.value() and center.value() and right.value():
        print('Go forward!')
    sleep(.25)