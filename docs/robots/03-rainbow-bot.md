# Rainbow Bot

This robot takes our base robot and adds and LED strip to display colors and patterns based on what the robot is doing or thinking about.

We use the same materials but we add a low cost 10 pixel LED strip that is easy to hook up with just power, ground and data wires added to our breadboard.  The LED is known as an addressable LED strip since you can individually program each LED.  The standard is called the  WS-2811B LED strip and is often called a NeoPixel LED strip (The Adafruit Term).

![](../img/led-strip.md)

Of course, you can also add longer LED strips and program the patterns in interesting ways.

## Part 1: Ordering The LED Strip

The LED strips come in a variety of lengths, density and packing.  We use the 1 meter long 60 pixels/meter strips that use the IP65 waterproofing.  We like the black backgrounds.  A sample place to purchase them is [here](https://www.ebay.com/itm/333953423650?hash=item4dc12cd922%3Ag%3AsxcAAOSwND9gYtgi&LH_BIN=1)

![](img/led-strip.png)

We can take a $3 strip of 60 LEDs and cut them up into six segments of 10 LEDs each for a cost of around 50 cents per strip.  We solder stranded wire to the segments and then put 22 gauge solid wire to make them easy to put in the breadboards.

## Part 2: Making The Connections
The LED strips use 5 volts of power and have a GND and a data connector.

## Part 3: Adding the WS-2811B Library


## Part 4: Testing Your Code
In our first test, we will just make the first pixel on the LED strip blink bright red.

```py
import machine, neopixel, time
# Set the pin number and number of pixels
LED_PIN = machine.Pin(4)
NUMBER_PIXELS = 10
np = neopixel.NeoPixel(LED_PIN, NUMBER_PIXELS)

# blink the first pixel red

while True:
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
```

## References

1. Micropython [NeoPixel Library](https://docs.micropython.org/en/v1.15/esp8266/tutorial/neopixel.html)