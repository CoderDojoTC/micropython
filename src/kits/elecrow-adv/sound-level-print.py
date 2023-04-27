# Elcrow Voice-activated Light
# Connect OUT to GP0
from machine import Pin,PWM
from utime import sleep_ms

sound = Pin(0, Pin.IN, Pin.PULL_DOWN)

while True:
    print(sound.value())
    if sound.value() == 1:
        print(1)
    sleep_ms(50)