# Rainbow Bot

This robot takes our base robot and adds and LED strip to display colors and patterns based on what the robot is doing or thinking about.

We use the same materials but we add a low cost 10 pixel LED strip that is easy to hook up with just power, ground and data wires added to our breadboard.  The LED is known as an addressable LED strip since you can individually program each LED.  The standard is called the  WS-2811B LED strip and is often called a NeoPixel LED strip (The Adafruit Term).

![](../img/led-strip.md)

Of course, you can also add longer LED strips and program the patterns in interesting ways.

## Part 1: Ordering The LED Strip

The LED strips come in a variety of lengths, density and packing.  We use the 1 meter long 60 pixels/meter strips that use the IP65 waterproofing.  We like the black backgrounds.  A sample place to purchase them is [here](https://www.ebay.com/itm/333953423650?hash=item4dc12cd922%3Ag%3AsxcAAOSwND9gYtgi&LH_BIN=1)

![](../img/led-strip.png)

We can take a $3 strip of 60 LEDs and cut them up into six segments of 10 LEDs each for a cost of around 50 cents per strip.  We solder stranded wire to the segments and then put 22 gauge solid wire to make them easy to put in the breadboards.

## Connecting the LED Strips

![](../img/rainbow-bot-connecting-strips.jpg)

## Adding a Standoff

![](../img/rainbow-bot-standoff.jpg)

## Upgrading to 9 Volt Power

Our base robot only needed power for the motors.  This robot has 72 RGB LEDs so it might draw more power.  So we upgraded the 6 volt battery pack with 4 AA batteries to two packs of 3 batteries for a total of 9 volts.  This allows the robot to continue to run even when the batteries are partially drained.  The battery packs must be wired in series to deliver the full 9 volts to the input of the motor controller where it powers the motors and also runs though a voltage regulator to power the reset of the robot.

![](../img/rainbow-bot-underside.jpg]

## 72 Pixel Configuration

Here is the top view of the LEDs shining through the clear plexiglass.

![](../img/rainbow-bot-top-view.jpg)

You can see the individual LEDs in this configuration.  By adding a small space between the plexiglass and a diffusion layer you can get a much more uniform color distribution over the top surface of the robot.

## Part 2: Making The Connections
The LED strips use 5 volts of power and have a GND and a data connector.  To make the connections we connect the center pin to Pin 0 (upper left corner of the Pico), the GND to the ground rail and the 5 volt to the 5 volt power rail.

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
