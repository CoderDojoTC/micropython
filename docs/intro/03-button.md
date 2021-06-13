# Button

In this lesson we will hook a single momentary push button up to our Raspberry Pi Nano.

You will hook up an LED to GP15.

```py
from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN) # input with pull down resistor

while True:
    if button.value(): # if the value changes
	    led.toggle()
        time.sleep(0.1) # wait 1/10th of a second
```

## References

1. [Raspberry Pi Pico Getting Started Guide Lab 6](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6)
1. [YouTube Video](https://www.youtube.com/watch?v=nPMU10mfFbs)