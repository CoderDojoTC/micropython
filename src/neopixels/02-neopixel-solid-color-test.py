from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 10

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def solid_color(color):
    for i in range(0, NUMBER_PIXELS):
        strip[i] = color
    strip.write()
 
delay = 4
while True:
    # red
    print('red')
    solid_color((255,0,0))
    sleep(delay)
    print('green')
    solid_color((0,255,0))
    sleep(delay)
    print('blue')
    solid_color((0,0,255))
    sleep(delay)
    print('off')
    solid_color((0,0,0))
    sleep(delay)
