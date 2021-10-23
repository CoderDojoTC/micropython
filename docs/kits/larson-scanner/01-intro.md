# Larson Scanner Pumpkin

![Larson Scanner Pumpkin](../../img/larson-scanner.gif)

The Larson Scanner is a light pattern special effect named after [Glen A. Larson](https://en.wikipedia.org/wiki/Glen_A._Larson).  Larson used this pattern to give his [Battlestar Galactica Cylon](https://en.wikipedia.org/wiki/Cylon_(Battlestar_Galactica)) and [KITT](https://en.wikipedia.org/wiki/KITT) robot eyes a sense of sentience.  See [Kinght Rider](https://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series)) for the backstory.

This project uses a 144 pixel/meter LED strip and a Raspberry Pi Pico to produce this effect.

![Craft Pumpkin](../../img/craft-pumpkin.jpg)
I used a craft pumpkin from Michaels.  I cut a slit in it and used hot-glue to hold the LED strip in place.

## Parts List

1. 9" Craft Pumpkin from [Micheals](https://www.michaels.com/9-in-orange-craft-pumpkin-by-ashland/10638818.html) $10
1. Raspberry Pi Pico ($4)
2. Breadboard ($2)
3. 27 pixels of WS2811B NeoPixel Strip [144 pixels per meter preferred](https://www.ebay.com/itm/324452155664?hash=item4b8adb0110:g:-kUAAOSwwT9f9avu) ($8)
4. [3 AA battery pack](https://www.ebay.com/itm/234251696371?hash=item368a7d38f3%3Ag%3AZe8AAOSwTmtaqyvb) or a [USB battery pack](https://www.amazon.com/Compact-5000mAh-External-Portable-More-Black/dp/B09BJGVH17/ref=dp_fod_2?th=1)

![WS2811b 144](../../img/ws2811b-144.png)
This is a screen image from e-bay showing a 1/2 meter of LED strip for $8.

## Sample Code

This code shows a five-pixel wide "eye" moving back-an-forth over a 27 pixel strip.  There is a central bright red LED surrounded by dimmer red LEDs that move back-and-forth.  We are using the NeoPixel library supplied by [Blaž Rolih](https://github.com/blaz-r/pi_pico_neopixel).

The example below has a delay of 1/10th of a second between drawing events.  You can make the delay smaller to speed up the speed of the eye movement.

```py
from utime import sleep
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 27
STATE_MACHINE = 0
LED_PIN = 0

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

## More to Explore

1. Add a potentiometer to change the speed of the eye scan.
2. Add a button to cycle through colors of the eye.
3. Add multiple patterns such as a "comet trail" that has the first pixel brighter and the following pixels dimmer.
4. Add a PIR motion sensor that will sense motion and get brighter if motion is sensed.
5. Use the new [I2S](https://github.com/miketeachman/micropython-i2s-examples) software to play a sound when the PIR motion sensor has been triggered.
6. Use an MP3 player such as the [DRF0229](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299) to play the cylon sound when motion is detected.
7. Add an OLED display and buttons to the back of the pumpkin to change the parameters of the display and the sounds.