# NeoPixels

![NeoPixel Demo](../img/neopixel-demo.gif)

NeoPixels are Red-Green-Blue LEDs that are designed to makes them easy to control with three wires: GND, +5V and a single serial data line.  They are very popular with our students because they are powerful, easy to program and full of **bling**.

!!! Note
    As of March of 2022 there is now built-in support for NeoPixels in the MicroPython 1.18 runtime for the Raspberry Pi RP2040 microcontroller.  Although you can still use custom libraries, this tutorial assumes you are using
    version 1.18 or later.

Controlling NeoPixels is challenging since the timing of data being sent must be very precise.  Python alone is not fast enough to send bits out of a serial port.  So a small function that uses assembly code is used.  This code can be called directly from a neopixel driver file so that the user's don't need to see this code.

[MicroPython Example Code on ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html)

## Different Types of NeoPixels
There are many different types of NeoPixels.  They come in many forms such as strips, rings and matrices.

![](../img/neopixel-types.jpg)

The most common type of NeoPixels are strips.  The strips come in a variety of densities and waterproofing.  The most common and easiest to use are the 60 pixels-per-meter type.

## Circuit connections

![](../img/led-strip-connections.png)

|LED Strip|Pico Name|Pico Pin|Description|
|---------|---------|--------|-----------|
|GND|GND|3|Ground|Third from top on the left with USB on top|
|5v|VBUS|40|Voltage from the USB bus.  Top right with USB on top|
|Data|GP22|22|Row 12 on the right side|

Note that you can also power most of the LED strips using the 3.3 volts available on Grove connectors.  The only difference is the brightness might not be quite as high, but for most applications this will not be a problem.

## Setup Parameters
Our Python code will have four parts:

1. Declaration of the import of the NeoPixel library from the RP2 runtime.  We also import the sleep function from the utime module.
2. Initialization of the fixed static parameters.  This is done once and the parameters are usually at the top of the file to make them easy to find and change for each application.
3. Initialization of the NeoPixel object using these static parameters.  This is also done just once.
4. Sending the drawing commands to the device through the data port.  This is usually done within a main loop.

### Import Statements
Here are the import statements we use:

```py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
```

### Static Initialization Parameters
There are only two values.  The number of pixels in the strip or ring and the pin number the data pin is connected to.

```py
NUMBER_PIXELS = 8
LED_PIN = 22
```

## Initialize the Strip Object

To setup the Neopixel object we just pass it the two parameters like this:

```py
strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)
```

Here is the full initialization code:

```py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NUMBER_PIXELS = 8
LED_PIN_ID = 22
led_pin = machine.Pin(LED_PIN_ID)
```

Now we are ready to write our first small test program!

## Move a red pixel up the strip

![Move LED Up Strip](../img/red-led-move-up.gif)


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
The following program will create 

```py
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 8
LED_PIN = 22

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)

brightness = 25
red = (brightness, 0, 0)
green = (0, brightness, 0)
blue = (0, 0, brightness)
while True:
    for i in range(0, NUMBER_PIXELS):
        strip[i] = red
        strip.write()
        sleep(.1)
        strip[i] = (0,0,0)
    for i in range(0, NUMBER_PIXELS):
        strip[i] =  green
        strip.write()
        sleep(.1)
        strip[i] = (0,0,0)
    for i in range(0, NUMBER_PIXELS):
        strip[i] =  blue
        strip.write()
        sleep(.1)
        strip[i] = (0,0,0)
```

#### Rainbow Cycle
The program cycles each pixel through all the colors in a rainbow.

```py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 22
NUMBER_PIXELS = 8
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
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
        for i in range(NUMBER_PIXELS):
            rc_index = (i * 256 // NUMBER_PIXELS) + j
            # print(rc_index)
            strip[i] = wheel(rc_index & 255)
        strip.write()
    sleep(wait)
        
counter = 0
offset = 0
while True:
    print('Running cycle', counter)
    rainbow_cycle(0)
    counter += 1
```

## References

[Core Electronics: How to use WS2812B RGB LEDs with Raspberry Pi Pico](https://core-electronics.com.au/tutorials/how-to-use-ws2812b-rgb-leds-with-raspberry-pi-pico.html) - HTML page, sample code and video

[MicroPython Library for NeoPixel](https://docs.micropython.org/en/latest/library/neopixel.html) - note the lack of support for the RP2040 microcontroller.

[rp2 port no module named array](https://github.com/micropython/micropython/issues/6837)