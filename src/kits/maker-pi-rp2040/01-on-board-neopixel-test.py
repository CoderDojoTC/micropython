from neopixel import NeoPixel
from utime import sleep

NUMBER_PIXELS = 2
NEOPIXEL_PIN = 18

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

counter = 0
while True:
    
    # turn both on red
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (255,0,0)
    strip.write()
    sleep(.5)
    
    # turn both on green
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,255,0)
    strip.write()
    sleep(.5)
    
    # turn both on blue
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,255)
    strip.write()
    sleep(1)
    counter += 1
    print(counter)