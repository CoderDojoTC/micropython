# Raspberry Pi RGB Box

![RGB Box](../../img/rgb-box.png)

This is a box with three potentiometers and a NeoPixel strip.  Changing the potentiometers changes the mix of Red, Green and Blue colors.  We use this at many science fairs or demonstration projects that has kids as young as three years old!  As the kids learn to adjust the knobs, we say "Hey, your a programmer!".

## Related Labs

Before you do this project, it is a good idea to get familiar with the [Potentiometer lab](../basics/03-potentiometer/).  This lab will show you how to hook up a single potentiometer to the Raspberry Pi Pico and read it's values.

## Required Tools

Although we will be using a solderless breadboard to connect the components, we use a hot-glue gun to make sure the wires don't get dislocated when the box get bumped around.

1. Soldering iron (unless you have pre-solders potentiometers)
2. Hot glue gun (for securing the wires to the breadboard)
3. Drill (for putting hole in the box)

## Parts List

1. Raspberry Pi Pico with headers ($4)
2. 1/2 size breadboard ($2)
3. Three 10K linear potentiometers ($2)
4. LED strip with 10 NeoPixels ($2)
5. Battery case with 3 AA batteries (2)
6. 22-gauge solid hookup wire
7. Power switch (optional) (50 cents)
8. Clear plastic box (4)

With a bit of clever shopping you can get the total part costs: under about $15.  If you purchase the parts in Quantity 10+ you can get the costs under $10/kit.

## Circuit Diagram

TBD

## Assembly
Solder six-inches of hookup wire to each of the three pins on the three potentiometers.

![Potentiometer Hookups](../../img/rgb-box-potentiometer-hookups.png)

## Sample Code

### Test the NeoPixel Connection
Our first step will be to verify we have the NeoPixel strip connected correctly and that we have the right configuration.  There are two items you might have to change:

1. The pin number connected to the data wire of the LED strip
2. The number of pixels

We use two Python variables to configure
```py
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 10
```

```py
import machine, neopixel
from utime import sleep
from neopixel import Neopixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 10
strip = Neopixel(NUMBER_PIXELS, 0, NEOPIXEL_PIN, "GRB")

print('flashing pixel 0 red')
delay=.3
while True:
    strip.set_pixel(0, (255,0,0)) // turn pixel 0 red
    strip.show()
    sleep(delay)
    strip.set_pixel(0, (0,0,0)) // turn pixel 0 off
    strip.show()
    sleep(delay)
```

