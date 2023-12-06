from machine import ADC, Pin
from utime import sleep

# this is the built-in LED on the Pico
led = Pin(25, Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side
pot = ADC(26)

MAX_DELAY = .5 # seconds

# global variables
delay = 0

# repeat forever
while True:
    pot_value = pot.read_u16() # read the value from the pot
    delay = pot_value/65025 * MAX_DELAY
    print("delay:", delay)
    if delay > 0:
        print("frequency (toggles per second):", 1/delay)
    led.high() # turn on the LED
    sleep(delay) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(delay) # leave it off for 1/2 second
