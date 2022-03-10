# NeoPixel

![NeoPixel Demo](../img/neopixel-demo.gif)

NeoPixels are Red-Green-Blue LEDs that are designed to makes them easy to control with three wires: GND, +5V and a single serial data line.  They are very popular with our students because they are powerful, easy to program and full of **bling**.

!!! Note
    As of March of 2022 there is now built-in support for NeoPixels in the MicroPython 1.18 runtime for the Raspberry Pi RP2040 microcontroller.  Although you can still use custom libraries, this tutorial assumes you are using
    version 1.18 or later.

Controlling NeoPixels is challenging since the timing of data being sent must be very precise.  Python alone is not fast enough to send bits out of a serial port.  So a small function that uses assembly code is used.  This code can be called directly from a neopixel driver file so that the user's don't need to see this code.

[MicroPython Example Code on ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html)


## Circuit connections

![](../img/led-strip-connections.png)

|LED Strip|Pico Name|Pico Pin|Description|
|---------|---------|--------|-----------|
|GND|GND|3|Ground|Third from top on the left with USB on top|
|5v|VBUS|40|Voltage from the USB bus.  Top right with USB on top|
|Data|GP22|22|Row 12 on the right side|


## Setup Parameters

```py
NUMBER_PIXELS = 8
LED_PIN = 22
```

## Initialize the Strip Object

```py
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 8
LED_PIN = 22
```

## Move a red pixel down the strip

```py
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 8
LED_PIN = 22

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)
        
while True:
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (255,0,0)
        strip.write()
        sleep(.1)
        strip[i] = (0,0,0)
```

## Turn All the Pixels Red, Green and Blue

```py
import time
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 12
STATE_MACHINE = 0
LED_PIN = 0

# We are using the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")
# set 100% brightness
strip.brightness(100)
delay = .1

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
while True:
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, red)
        strip.show()
        time.sleep(delay)
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, green)
        strip.show()
        time.sleep(delay)
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, blue)
        strip.show()
        time.sleep(delay)

```


## Full code (no library)
```py
# Example using PIO to drive a set of WS2812 LEDs.

import array, time
from machine import Pin
import rp2

# Configure the number of WS2812 LEDs.
NUM_LEDS = 60
PIN_NUM = 22
brightness = 0.2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

def color_chase(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        time.sleep(wait)
        pixels_show()
    time.sleep(0.2)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            pixels_set(i, wheel(rc_index & 255))
        pixels_show()
        time.sleep(wait)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

print("fills")
for color in COLORS:
    pixels_fill(color)
    pixels_show()
    time.sleep(0.2)

print("chases")
for color in COLORS:
    color_chase(color, 0.01)

print("rainbow")
rainbow_cycle(0)
```

## References

[Core Electronics: How to use WS2812B RGB LEDs with Raspberry Pi Pico](https://core-electronics.com.au/tutorials/how-to-use-ws2812b-rgb-leds-with-raspberry-pi-pico.html) - HTML page, sample code and video

[MicroPython Library for NeoPixel](https://docs.micropython.org/en/latest/library/neopixel.html) - note the lack of support for the RP2040 microcontroller.

[rp2 port no module named array](https://github.com/micropython/micropython/issues/6837)