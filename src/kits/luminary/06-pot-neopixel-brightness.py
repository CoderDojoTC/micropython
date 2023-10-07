from machine import ADC, Pin, PWM
from utime import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 60
LED_PIN = 0

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# Pins Used
BUILT_IN_LED_PIN = 25
POT_PIN = 26

pot = ADC(POT_PIN)

POLL_DELAY = .01 # poll the pot after this delay in seconds

# repeat forever
while True:
    pot_value = pot.read_u16() >> 8 # read the value from the pot
    print("pot value:", pot_value)
    strip[0] = (pot_value,0,0)
    strip.write()
    sleep(POLL_DELAY)
