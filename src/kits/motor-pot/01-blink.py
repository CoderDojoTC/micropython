# Setup - run once
from machine import Pin # Get the Pin function from the machine module.
from time import sleep # Get the sleep library from the time module.

# This is the built-in green LED on the Pico.
BUILT_IN_LED_PIN = 25
# change this to the following named pin on the "W"
# BUILT_IN_LED_PIN = Pin("LED", Pin.OUT)

# The line below indicates we are configuring this as an output (not input)
led = machine.Pin(BUILT_IN_LED_PIN, machine.Pin.OUT)

# Main loop: Repeat the forever...
while True:
    led.high() # turn on the LED
    sleep(0.2) # leave it on for 1/2 second
    led.low()  # Turn off the LED
    sleep(0.2) # leave it off for 1/2 second
