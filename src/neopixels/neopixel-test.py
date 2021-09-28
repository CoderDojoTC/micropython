import machine, neopixel, time
# Set the pin number and number of pixels
from neopixel import Neopixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 144
strip = Neopixel(NUMBER_PIXELS, 0, 0, "GRB")

# blink the first pixel red

while True:
    # set pixel 0 to be red
    strip.set_pixel(0,(255,0,0))
    strip.show()
    time.sleep(0.5)
    # turn pixel 0 off
    strip.set_pixel(0, (0,0,0))  
    
    # set pixel 1 to be green
    strip.set_pixel(1,(0,255,0))
    strip.show()
    time.sleep(0.5)
    # turn pixel 0 off
    strip.set_pixel(1, (0,0,0))
     
    # set pixel 2 to be blue
    strip.set_pixel(2,(0,0,255))
    strip.show()
    time.sleep(0.5)
    # turn pixel 0 off
    strip.set_pixel(2, (0,0,0))
    strip.show()
    time.sleep(0.5)
