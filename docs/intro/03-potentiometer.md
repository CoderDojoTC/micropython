# MicroPython Potentiometer Lab

![](../img/pot-blink-speed.jpg)

In this lab we will use a 10K ohm potentiometer to demonstrate how a turn of a knob can result in getting a continuous variable from a user into our code.  We will show how we can use a potentiometer to change the blinking speed of on LED.

## About Analog to Digital Converters

Digital microcontrollers are inherently noisy.  They have clocks that pull power from the power supply and cause voltage fluctuations when we compare a signal to these power lines.  This makes it difficult to get 

ADC_VREF is the ADC power supply (and reference) voltage, and is generated on Pico by filtering the 3.3V supply. This
pin can be used with an external reference if better ADC performance is required.
AGND is the ground reference for GPIO26-29, there is a separate analog ground plane running under these signals and
terminating at this pin.

## Circuit Diagram

![](../img/pot-circuit-diagram.png)

1. Connect the top rail of the potentiometer to row 6 which is the ADC_VREF pin.
2. Connect the center tap to row 10 which is ADC0
3. Connect row 8 to the bottom rail of the potentiometer to the Analog Ground (AGND) pin

Note: to get an accurate noise-free reading from the potentiometer you must use the ADC_VREF and the AGND pins.  These are special pins designed to reduce the noise on the power areas of the pico.

## Sample Code To Print Potentiometer Values

```py
from machine import ADC
from utime import sleep
pot = ADC(26)
while True:
    print(pot.read_u16())
    sleep(.2)
```

```mermaid
graph LR
p[Pico]-->|ADC_VREF 36 row=6| pos(Positive)
p[Pico]-->|AGND 33 row=8| neg(Negative)
p[Pico]-->|GP26 pin=26 ADC0 31 row=10| tap(Center Tap)
    pos(Positive) --- pot(Potentiometer)
    neg(Negative) --- pot(Potentiometer)
    tap(Center Tap) --- pot(Potentiometer)
```

Connect the positive to pin 35 ADC_REF (row 6 on the breadboard) and the negative to pin 33 AGND (row 8 on the breadboard).  The Pico has special noise reduction circuits to avoid power supply jitter on these reference pins.

## Changing Blink Speed with a Potentiometer

```py
from machine import ADC, Pin
from utime import sleep

# this is the built-in LED on the Pico
led = Pin(25, Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side
pot = ADC(26)

MAX_DELAY = 2 # seconds when the pot is fully clockwise

# global variables
delay = .25

# repeat forever
while True:
    pot_value = pot.read_u16() # read the value from the pot
    delay = pot_value/65025 * MAX_DELAY
    print("delay:", delay, "frequency (toggles per second):", 60/delay)
    led.high() # turn on the LED
    sleep(delay) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(delay) # leave it off for 1/2 second
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/lFfSTOOrsIA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>