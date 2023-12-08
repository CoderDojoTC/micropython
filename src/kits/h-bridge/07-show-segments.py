from machine import Pin
from utime import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 28
LED_PIN = 12

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# one segment for the 6 parts of the H brige
segments = [[0,4], [5,9], [10,14], [15,19], [20, 23], [24, 27]]
num_segments = len(segments)

color_names = ["red", "orange", "yellow", "green", "indigo", "violet"]
red = (255, 0, 0)
off = (0,0,0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (255, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
colors = (red, orange, yellow, green, blue, indigo, violet)

for i in range(0, num_segments):
    seg_length = segments[i][1] - segments[i][0] + 1
    print(i, seg_length)
    for j in range(segments[i][0], segments[i][1]+1):
        strip[j] = colors[i]
        strip.write()

