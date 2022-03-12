# Blink in MicroPython

![Blink GIF](../img/blink-on-board-led.gif)

## Overview
In this lab, we will use MicroPython to make the green on-board LED on the Raspberry Pi Pico blink on and off using MicroPython.  The only things you need to run this program are an IDE like Thonny, a USB cable and a $4 Raspberry Pi Pico.

## Blinking the Builtin LED

The pico has a single built in LED wired to logical pin 25.  We call this GPIO 25.  Here is a sample program that you can use:

```py
from machine import Pin # get the Pin function from the machine module
from time import sleep # get the sleep library from the time module
# this is the built-in green LED on the Pico
led = machine.Pin(25, machine.Pin.OUT)

# repeat forever
while True:
    led.high() # turn on the LED
    sleep(0.5) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(0.5) # leave it off for 1/2 second
```

This program has two parts.  The first part is often called the preamble - this code gets executed once and loads the right libraries and initializes global variables.  
The second part is the main event loop.  This program continues to run until the device is powered down or reset.

The ```import machine``` statement is required to define the characteristics of our physical machine.  The ```import time``` library is required for the python sleep function.

Note that the text after the hash or pound characters are comments.  Comments are ignored by the Python interpreter.

## Changing the Blink Speed

Next, lets create a global variable for the delay that the LED is on and off.

```py
from machine import Pin
from time import sleep
# this is the builtin LED on the Pico
led = Pin(25, machine.Pin.OUT)

# global variables
delay = .25

# repeat forever
while True:
    led.high() # turn on the LED
    sleep(delay) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(delay) # leave it off for 1/2 second
```

This program will blink the built-in LED on and off every 1/4 of a second.  By changing the delay variable you can make the LED blink faster and slower.

!!! Challenge
    What is the fastest you can make the LED blink and still see it changing?  What does this tell you about the human eye?

## Using Toggle

Instead of using the ```on()``` and ```off()``` methods, we can also just use the ```toggle()``` function.

```py
from machine import Pin
from time import sleep
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    led_onboard.toggle()
    sleep(.25)
```

If you save the file as main.py, this program will run when the pico starts up without the BOOTSEL being pressed.

We will assume that an LED is connected to pin GIO16 and is connected via a 330 ohm resistor to ground.

Here is the code that will blink an LED that is connected to PIN GIO16, which is in the upper right corner of the Pico.

```py
import machine
import time
# this is the lower right corner pin on the Pico with USB on the bottom
led = machine.Pin(16, machine.Pin.OUT)

# repeat forever
while True:
    led.high() # turn on the LED
    time.sleep(0.5) # leave it on for 1/2 second
    led.low() # Turn off the LED
    time.sleep(0.5) # leave it off for 1/2 second
```


```py
import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    led_onboard.toggle()
    utime.sleep(5)
```


## Virtual Lab

If you don't have access to the $4 Raspberry Pi Pico or a similar device, you can also try the MicroPython Emulator:

[Unicorn Emulator](http://micropython.org/unicorn/)
