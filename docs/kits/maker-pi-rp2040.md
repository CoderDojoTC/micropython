# Maker Pi RP2040

The Maker Pi PR2040 kit from [Cytron Technologies](https://www.cytron.io/) is a $9.90 US kit that is designed to simplify learning robotics using the RP2040 chip. It became available in April of 2021.  This is the most powerful robotics board we have ever seen for under $10!

![Maker Pi RP2040 Top View](../img/maker-pi-rp2040-top-view.png)

## Features
All our robots are built around a RP2040 and a motor driver with a few low-cost sensors and displays.  With the exception of the OLED display, this board packs in a huge number of features for a low cost of $9.90.


* Power status LED (green)
* On/off switch
* 13 blue LEDs to show status on GP pins 0,1,2,3,4,5,6,16,17,26,27 and 28
* 2 WS2812B RGB LEDs connected to GP18
* LiPo Battery Connector
* Micro USB Port (use for powering and programming)
* Reset button
* Boot button
* Momentary press buttons on ports GP20 and GP21
* 2 Motor drivers. Motor A is controlled by GP8 and GP10 and motor B is controlled by GP9 and GP11.
* 4 motor test buttons for testing motors A and B, forward and backward
* 4 red motor status LEDs buttons for displaying motors A and B, forward and backward
* 7 Grove Ports on GPs 1:0,1; 2:2,3; 3:4,5; 4:16,17; 5:6,26; 6:26,27 and 7:7,28
* 4 servo connectors on ports GP12, GP13, GP14 and GP15

## Removing the Default CircuitPython 
I had to load the flash_nuke.uf2 file to remove the default CircuitPython runtime.  Note that the board must be fully powered down after this load for it to work.  I had 4 AA batteries connected so it was not resetting correctly.

## LED Demo

Here is a demo using the 13 nice blue LEDs used to show the status of the pins.

![Maker Pi RP2040 LED Demo](../img/maker-pi-rp2040-leds.gif)

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

## Unclear Motor Current Limitations

This board is only designed to work with small DC-hobby motors and there is no documentation on exactly what motor driver chip is used or its precise limitations.  The documentation only indicates that the maximum current is 1A continuous power and 1.5A for up to 5 seconds.  But it is not clear if this is per motor or total.  The input voltage is only rated to an incredibly low 6 volts, which is very odd since almost all the motor driver chips can take much higher input voltages.

If this motor driver chip is similar to the ubiquitous [L293x motor controllers](https://www.ti.com/document-viewer/L293D/datasheet/specifications#ESD_Rating_1), then the current should be 1A per motor.  I suspect it might not be the L293x since the input voltage of the L293x is 4.5 V to 36 V.

I suspect that if you glued a small [heat sink](https://en.wikipedia.org/wiki/Heat_sink) [16 pin DIP fin](https://my.element14.com/fischer-elektronik/ick-14-16-b/heat-sink-dip-glue-on-50-c-w/dp/4620896) to the unknown motor driver IC on the main board you could drive slightly larger motors.

![Maker Pi RP2040 Motor Driver Chip](../img/maker-pi-rp2040-motor-driver.jpg)
Close-up of the motor driver chip.  I can't quite make out the numbers on the chip.

## References
* [Link on Box](https://link.cytron.io/maker-pi-rp2040-start)
* [GitHub Link](https://github.com/CytronTechnologies/MAKER-PI-RP2040)
* [Maker Pi RP2040 Product Page](https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040)
* [Maker Pi RP2040 Datasheet on Google Docs](https://docs.google.com/document/d/1DJASwxgbattM37V4AIlJVR4pxukq0up25LppA8-z_AY/edit)