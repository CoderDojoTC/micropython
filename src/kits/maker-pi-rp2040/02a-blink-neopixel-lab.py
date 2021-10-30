from utime import sleep
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 2
STATE_MACHINE = 0
LED_PIN = 18

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

while True:
    # turn on first pixel red for 1/2 second
    strip.set_pixel(0, (255, 0, 0))
    strip.show()
    sleep(.5)   
    strip.set_pixel(0, (0, 0, 0)) # turn all colors off
    strip.show()
    sleep(.5)