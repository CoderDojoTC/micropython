from machine import Pin
import time
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import NeoPixel
NUMBER_PIXELS = 2
LED_PIN = 18
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
# Color RGB values
red = (255, 0, 0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet)


color_index = 0
while True:
    for color in colors:
        for i in range(NUMBER_PIXELS):
            print(i, color_names[color_index])
            strip[i] = color
            strip.write()
            time.sleep(1)
        color_index += 1
        if color_index >= num_colors: color_index = 0
