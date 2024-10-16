from machine import Pin # get the Pin function from the machine module
from time import sleep # get the sleep library from the time module
# this is the built-in green LED on the Pico
led = machine.Pin(0, machine.Pin.OUT)

# repeat forever
while True:
    led.high() # turn on the LED
    sleep(0.5) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(0.5) # leave it off for 1/2 second