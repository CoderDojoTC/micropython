from neopixel import Neopixel
from time import sleep

NUMBER_PIXELS = 2
STATE_MACHINE = 0
LED_PIN = 11

strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

while True:
    
    # blink red
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, (255,0,0))
    strip.show()
    sleep(.5)

    # blink green
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, (0,255,0))
    strip.show()
    sleep(.5)

    # blink blue
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, (0,0,255))
    strip.show()
    sleep(.5)
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, (0,0,0))
    strip.show()
    sleep(.5)