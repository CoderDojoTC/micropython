# Blue LED Lab

I wanted to make sure that everyone knows how easy this board is to program with MicroPython once you have the runtime loaded.  Here is a demo using the 13 nice blue LEDs used to show the status of the pins.

![Maker Pi RP2040 LED Demo](../../img/maker-pi-rp2040-leds.gif)

```py
import machine
import time

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs
blue_led_pins = [0,1,2,3,4,5,6,7,16,17,26,27,28]
number_leds = len(blue_led_pins)
led_ports = []
delay = .05

# create a list of the ports
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

# loop forever
while True:
    # blue up
    for i in range(0, number_leds):
        led_ports[i].high()
        time.sleep(delay)
        led_ports[i].low()
    # blue down
    for i in range(number_leds - 1, 0, -1):
        led_ports[i].high()
        time.sleep(delay)
        led_ports[i].low()
```

This demo uses a list of all the 13 digital I/O ports.  For each port it sets the port to be a digital output.  In the main loop it then goes up and down the strip of LEDs, turning each one on for 1/20th of a second (.05 seconds).
