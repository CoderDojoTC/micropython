# Ten Bar LED Display

<iframe width="560" height="315" src="https://www.youtube.com/embed/SooCyURMsPE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


![](../img/led-bar-graph-10-segments.png)

## Goals for the Lesson

 These LED displays can be purchased on eBay for around 40 cents each in quantity 10.  These displays are ideal for showing a reading such as a battery charge or a signal strength.

 Our goal is to learn how to use python lists to turn on and off a row of 10 LEDs.

## Circuit

![](../img/led-10-segment-package-circuit.png)

The LEDs come in a dual-in-line package with each of the LEDs connected by the pins aligned across the package.

In the circuit below, I connected the positive (anode) of each LED to a GPIO pin and the negative (cathode) through a 330-ohm resistor to the GND rail of the solderless breadboard.

![](../img/led-10-segment-circuit.png)

Note!  You **MUST** use a current limiting resistor or you will burn out the LED.

One end of each of the bars will go to one of the power rails and the other to a GIPO pin.  I used the pis on the lower part of the Raspberry Pi Pico for this demo.

## Programming

We will create a list that has each of the GPIO pins for output.

```py
pin_ids = [12,13,14,15,20,19,18,17,16]
```

For each pin on this list, we will create a new list that contains the pin object that we can turn on or off.

```py
from machine import Pin
from utime import sleep

pin_ids = [12,13,14,15,20,19,18,17,16]
pins = []
pin_ids
for i in pin_ids:
    pins.append(machine.Pin(pin_ids[i], machine.Pin.OUT))
```

We will use this same preamble code in all our examples.

# Code to Blink all 10 LEDs

```py
from machine import Pin
from utime import sleep

pin_ids = [12,13,14,15,20,19,18,17,16]
pins = []
pin_ids
for i in pin_ids:
    pins.append(machine.Pin(pin_ids[i], machine.Pin.OUT))

delay = .5
while True:
    # turn all the pins on
    for pin in pins:
        pins.on()
    sleep(delay) # wait
    # turn all the pins off
    for pin in pins:
        pins[i].off()
    sleep(delay)
```

## Sample Running Lights Example

The "running lights" pattern gives the impression that there is a red object that is moving up and down a row.  We do this by successively turning on adjacently LEDs and then turning them off.  This give the illusion of motion.

```python
from machine import Pin
from utime import sleep

pin_ids = [12,13,14,15,20,19,18,17,16]
pins = []

for i in range(0, 9):
    pins.append(machine.Pin(pin_ids[i], machine.Pin.OUT))

delay = .1
while True:
    for i in range(0, 9):
        pins[i].on()
        sleep(delay)
        pins[i].off()
    for i in range(8, 1, -1):
        pins[i].on()
        sleep(delay)
        pins[i].off()
```

## swipe

The swipe pattern turns each LED on but keeps it on until the direction is reversed.

## Adding a Binary Counter Patterns

We can also create another patten that will demonstrate binary counting.  In this pattern, the least significant bit flickers on and off.  For each cycle the adjacent pixel toggles once.  The happens for each adjacent pixel.  The most significant bit will only change every 1024 cycles of the least significant bit.