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

![NeoPixel Types](../img/neopixel-types.jpg)

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

1. Declaration of the imports from the RP2 MicroPython runtime.  We also import the sleep function from the utime module and some samples will also need the random library.  All our programs have been tested on version 1.18 of the MicroPython RP2 library or later.
2. Initialization of the fixed static parameters.  This is done once and the parameters are usually at the top of the file to make them easy to find and change for each application.  Make sure you adjust the pin number and the number of pixels in your setup in this area.
3. Initialization of the NeoPixel object using these static parameters.  This is also done just once.
4. Sending the drawing commands to the device through the data port.  This is usually done within a main loop.

### Import Statements
Here are the import statements we use:

```py
from machine import Pin
from utime import sleep
from neopixel import NeoPixel
```

### Static Initialization Parameters
There are only two values.  The number of pixels in the LED strip or LED ring and the pin number the data pin is connected to.

```py
NUMBER_PIXELS = 8
LED_PIN = 22
```

### Initialize the Strip Object

To setup the NeoPixel object we just pass it the two parameters like this:

```py
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)
```

Here is the full initialization code:

```py
from machine import Pin
from utime import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 8
LED_PIN = 22
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

```

## Sample Programs
Now we are ready to write our first small test program!

### Move Red Pixel Across Strip

![Move LED Up Strip](../img/red-led-move-up.gif)

```py
from machine import Pin
from time import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 8
LED_PIN = 22

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)
        
while True:
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (255,0,0) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
        sleep(.1) # keep on 1/10 of a second
        strip[i] = (0,0,0) # change the RAM back but don't resend the data
```

### Fade in and Out
Make the first pixel fade the red color in and out.  We do this by slowly turning up the color level of the red on strip[0].

```
Off: strip[0] = (0,0,0)
Red Very Dim: strip[0] = (1,0,0)
Dim Red: strip[0] = (10,0,0)
Red Half Brightness: strip[0] = (128,0,0)
Red Full Brightness: strip[0] = (255,0,0)
```

We start a 0 and go up to 255.  Then we go back from 255 back down to zero.  We delay about 5 milliseconds between each of the 255 brightness levels.


```py
from machine import Pin
from time import sleep
from neopixel import NeoPixel


NUMBER_PIXELS = 60
LED_PIN = 0

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

delay = .005

while True:
    for i in range(0, 255):
        strip[0] = (i,0,0) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
        sleep(delay)
    for i in range(255, 0, -1):
        strip[0] = (i,0,0)
        strip.write()
        sleep(delay)
```

### Heartbeat Lab

What if you were building a robot and you wanted to flash the LED to look like a human heartbeat?  Instead of slowing fading in and out, you would want the brightness to follow the electrical signals coming from the heart.  This is called an electro cardiogram (EKG) and it look like this:

![EKG Sample](../img/ekg-sample.png)

Notice that the signal is low for about one second and then it spikes up to maximum brightness and then comes back down.  When we are moving the brightness up and down, we don't have to pause between each of the 256 brightness values.  The eye can't usually see the intermediate brightness values if the brightness is changing quickly.  To make our code efficient we can skip over 9 out of 10 of the brightness gradations between 0 and 255.  We call this the ```skip_interval``` in our code below.

The following code emulates this heart beat pattern:

```py
from machine import Pin
from time import sleep
from neopixel import NeoPixel

# Most people have a heart rate of around 60-70 beats per minute
# If we add a once second delay between "beats" you can make and LED
# look like a beating heart.

NUMBER_PIXELS = 1
LED_PIN = 0

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

ramp_delay = .001
beat_delay = 1
skip_interval = 10

while True:
    # ramp brightness up using the ramp_delay
    for i in range(0, 255, skip_interval):
        strip[0] = (i,0,0)
        strip.write()
        sleep(ramp_delay)
    # ramp brightness down using the same delay
    for i in range(255, 0, -skip_interval):
        strip[0] = (i,0,0)
        strip.write()
        sleep(ramp_delay)
    strip[0] = (0,0,0)
    strip.write()
    sleep(beat_delay)
```

### Move Red, Green and Blue

![neopixel-red-green-blue](../img/neopixel-red-green-blue.gif)

The following program will just take the block of code in the for loop above and duplicate it three times, one for red, one for blue and one for green.

```py
from machine import Pin
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 8
LED_PIN = 0

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# we use the same brightness for each color
brightness = 25
delay = .1
# here we define variables for each color
red = (brightness, 0, 0)
green = (0, brightness, 0)
blue = (0, 0, brightness)
while True:
    # draw red up the strip
    for i in range(0, NUMBER_PIXELS):
        strip[i] = red
        strip.write()
        sleep(delay)
        strip[i] = (0,0,0)
    # draw blue up the strip
    for i in range(0, NUMBER_PIXELS):
        strip[i] =  green
        strip.write()
        sleep(delay)
        strip[i] = (0,0,0)
    # draw green up the strip
    for i in range(0, NUMBER_PIXELS):
        strip[i] =  blue
        strip.write()
        sleep(delay)
        strip[i] = (0,0,0)
```

### Rainbow Cycle
The program cycles each pixel through all the colors in a rainbow.  It uses two functions:

1. **wheel(pos)** this function takes a position parameter from 0 to 255 and returns a triple of numbers for the red, green and blue values as the position moves around the color wheel.  This is a handy program anytime you want to cycle through all the colors of the rainbow!
2. **rainbow_cycle(wait)** will cycle each of the pixels in a strip through the color wheel.  It gives the appearance that colors are moving across the strip.  The wait is the delay time between updating the colors.  A typical value for wait is .05 seconds or 50 milliseconds.

```py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 22
NUMBER_PIXELS = 8
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

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
    global NUMBER_PIXELS, strip
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
    rainbow_cycle(.05)
    counter += 1
```

## References

* [MicroPython RP2 Reference for NeoPixel Driver](https://docs.micropython.org/en/latest/rp2/quickref.html#neopixel-and-apa106-driver)
* [Core Electronics: How to use WS2812B RGB LEDs with Raspberry Pi Pico](https://core-electronics.com.au/tutorials/how-to-use-ws2812b-rgb-leds-with-raspberry-pi-pico.html) - HTML page, sample code and video
* [MicroPython Library for NeoPixel (used before version 1.18 of the MicroPython RP2 Runtime)](https://docs.micropython.org/en/latest/library/neopixel.html) - note the lack of support for the RP2040 microcontroller.
* [rp2 port no module named array](https://github.com/micropython/micropython/issues/6837)