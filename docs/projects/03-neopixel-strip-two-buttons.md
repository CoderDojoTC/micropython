# NeoPixel Two Button Kit

This is a low-cost (around $10) kit that is used for hackathons and activities such as a Halloween costume contest.

## Contents
1. Raspberry Pi Pico with Headers
2. Breadboard
3. NeoPixel Strip (ideally a 1 meter strip with 60 pixels)
4. Two momentary push buttons

## Background

See the Basic Example for the [NeoPixel Strip](../basics/05-neopixel.md) lab.

## Labs

We supply a small set of "getting started" labs to demonstrate how
to program colors on the LED strip and give the perception of
motion up and down the strip.

### Blink

### Move

### Fade In and Out

```py
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 60
LED_PIN = 0

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)

delay = .005

while True:
    for i in range(0, 255):
        strip[0] = (i,0,0) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
        sleep(delay) # keep on 1/10 of a second
    for i in range(255, 0, -1):
        strip[0] = (i,0,0) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
        sleep(delay) # keep on 1/10 of a second
```