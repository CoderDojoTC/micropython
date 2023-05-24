# blink the builtin blue LED
from machine import Pin
from utime import sleep

# hardware config parameters
BUILTIN_LED_PIN = 25
led = Pin(BUILTIN_LED_PIN, Pin.OUT)

while True:
    led.toggle()
    sleep(.5)
