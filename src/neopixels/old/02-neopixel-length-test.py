import machine
from neopixel import Neopixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 72
strip = Neopixel(NUMBER_PIXELS, 0, 0, "GRB")

delay = .01
# blink the first pixel red

while True:
    for i in range(0,5):
        strip.set_pixel(NUMBER_PIXELS -1 ,(255,0,0))
        strip.show()
        sleep(0.1)
        strip.set_pixel(NUMBER_PIXELS -1 ,(0,0,0))
        strip.show()
        sleep(0.1)
        
    for i in range(0, NUMBER_PIXELS - 1):
        # set pixel 0 to be red
        strip.set_pixel(i,(255,0,0))
        strip.show()
        sleep(delay)
        # turn pixel 0 off
        strip.set_pixel(i, (0,0,0))
    for i in range(NUMBER_PIXELS-1, 0, -1):
        # set pixel 0 to be red
        strip.set_pixel(i,(255,0,0))
        strip.show()
        sleep(delay)
        # turn pixel 0 off
        strip.set_pixel(i, (0,0,0))  

