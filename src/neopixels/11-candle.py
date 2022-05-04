from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
# https://docs.micropython.org/en/latest/library/random.html

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def candle(delay):
    for i in range(0, NUMBER_PIXELS):
         green = 50 + randint(0,155)
         red = green + randint(0,50)
         strip[randint(0,NUMBER_PIXELS - 1)] = (red, green, 0)
         strip.write()
         sleep(delay)

counter = 0
while True:
   candle(.01)
   # wrap
   counter = counter % (NUMBER_PIXELS-1)
   counter += 1