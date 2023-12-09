from machine import Pin
from time import sleep
led_onboard = Pin(25, Pin.OUT)
while True:
    led_onboard.toggle()
    sleep(.25)