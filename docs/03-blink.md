# Blink in Micropython

## Overview
In this lab, we will use Micropython to make an LED blink on and off using Python.

## Virual Lab

[Unicorn Emulator](http://micropython.org/unicorn/)

## Sample Program
```py
import machine
import time
led = machine.Pin(15, machine.Pin.OUT)

# loop forever
while True:
    led.high()
    time.sleep(0.5)
    led.low()
    time.sleep(0.5)
```