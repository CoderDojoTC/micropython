from utime import sleep
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 27
STATE_MACHINE = 0
LED_PIN = 0

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

# Color RGB values
red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0,0,0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet)

# set to be 1 to 100 for percent brightness
strip.brightness(100)

delay = .1
color_index = 0
while True:
    for i in range(2, NUMBER_PIXELS-2):
        strip.set_pixel(i-2, red_light)
        strip.set_pixel(i-1, red_med)
        strip.set_pixel(i, red)
        strip.set_pixel(i+1, red_med)
        strip.set_pixel(i+2, red_light)
        if i > 0: strip.set_pixel(i-3, (0,0,0))
        strip.show()
        sleep(delay)
        strip.set_pixel(i, off)
    for i in range(NUMBER_PIXELS-4, 1, -1):
        if i < NUMBER_PIXELS-2: strip.set_pixel(i+3, (0,0,0))
        strip.set_pixel(i-2, red_light)
        strip.set_pixel(i-1, red_med)
        strip.set_pixel(i, red)
        strip.set_pixel(i+1, red_med)
        strip.set_pixel(i+2, red_light)
        strip.show()
        sleep(delay)
