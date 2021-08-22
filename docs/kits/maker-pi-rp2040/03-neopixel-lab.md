## NeoPixel Demo Lab

The Maker Pi RP2040 comes with two built-in NeoPixels.  Each NeoPixel has a red, green and blue LED inside it.  Each of these LEDs can be set to any one of 256 values from 0 (off) to 255 (brightest value).


![Maker Pi RP2040 NeoPixel Demo](../img/maker-pi-rp2040-neopixel-demo.gif)

## NeoPixel Setup

```py
from neopixel import Neopixel

NUMBER_PIXELS = 2
STATE_MACHINE = 0
LED_PIN = 18

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")
```

```py
import time
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 2
STATE_MACHINE = 0
LED_PIN = 18

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

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

# set to be 1 to 100 for percent brightness
strip.brightness(100)

color_index = 0
while True:
    for color in colors:
        for i in range(NUMBER_PIXELS):
            print(i, color_names[color_index])
            strip.set_pixel(i, color)
            strip.show()
            time.sleep(1)
        color_index += 1
        if color_index >= num_colors: color_index = 0

```


