# This program will print a sequence of numbers in the shell if a button is pressed
# Each momentary button must be connected to the 3.3 volt power rail
# The rotory encoder will only display A or B values
from machine import Pin
import time

led = Pin(15, Pin.OUT)

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(22, Pin.IN, Pin.PULL_DOWN)
rotaryA = Pin(16, Pin.IN, Pin.PULL_DOWN)
rotaryB = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:
    if button1.value():
        print('1 ', end='')
    if button2.value():
        print('2 ', end='')
    if button3.value():
        print('3 ', end='')
    if rotaryA.value():
        print('A ', end='')
    if rotaryB.value():
        print('B ', end='')
    time.sleep(0.1)