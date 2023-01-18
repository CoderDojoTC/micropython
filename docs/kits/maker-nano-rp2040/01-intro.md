# Cytron Maker Nano RP2040

The [Cytron Nano RP2040](https://www.cytron.io/maker-nano-rp2040-simplifying-projects-with-raspberry-pi-rp2040) is a low-cost ($9), high-functionality board.

## features

1. Low cost: $9
2. 14 GPIO blue LEDs
3. 2 RGB LEDs (Neopixels)
4. 1 Piezo buzzer
5. 2 4-wire JST-SH ports (with Grove connectors)

![](../img/cytron-nano-rp2040-pinout.png)

## Blink Lab

```py
from machine import Pin # get the Pin function from the machine module
from time import sleep # get the sleep library from the time module
# this is the built-in green LED on the Pico
led = machine.Pin(0, machine.Pin.OUT)

# repeat forever
while True:
    led.high() # turn on the LED
    sleep(0.5) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(0.5) # leave it off for 1/2 second
```

