# Larson Scanner

![Lason Scanner Pumpkin](../../img/larson-scanner.gif)

The Larson Scanner is a light pattern special effece names after [Glen A. Larson](https://en.wikipedia.org/wiki/Glen_A._Larson).  Larson use this pattern to give his robot eyes a sense of sentience.  See [](https://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series)) and This project uses a LED strip and a Raspberry Pi Pico to produce this effect.

## Parts List

1. Raspberry Pi Pico ($4)
2. Breadboard ($2)
3. 27 pixels of WS2811B NeoPixel Strip (144 per meter preferred) ($8)

![WS2811b 144](../../img/ws2811b-144.pngg)
## Sample Code

```py
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

delay = .1
while True:
    for i in range(2, NUMBER_PIXELS-2):
        strip.set_pixel(i-2, red_light)
        strip.set_pixel(i-1, red_med)
        strip.set_pixel(i, red)
        strip.set_pixel(i+1, red_med)
        strip.set_pixel(i+2, red_light)
        if i > 0: strip.set_pixel(i-3, off)
        strip.show()
        sleep(delay)
    for i in range(NUMBER_PIXELS-4, 1, -1):
        if i < NUMBER_PIXELS-2: strip.set_pixel(i+3, off)
        strip.set_pixel(i-2, red_light)
        strip.set_pixel(i-1, red_med)
        strip.set_pixel(i, red)
        strip.set_pixel(i+1, red_med)
        strip.set_pixel(i+2, red_light)
        strip.show()
        sleep(delay)
```