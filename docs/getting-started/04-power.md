# Managing Power With MicroPython

## Power connectors

### USB Power

### Battery Power

4 AA Rechargeable

!!! WARNING
    Do not use 4 AA batteries.  6 volts is too high for the Pico.  Use a voltage regulator such as is found on motor driver boards.

## Monitoring Power

On the Pico, GP24 can be used to indicate if power is being drawn from the USB cable.



https://www.raspberrypi.org/forums/viewtopic.php?t=300676

```py
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
USBpower = machine.Pin(24, machine.Pin.IN) 

while True:
   led_onboard.value(1)
   utime.sleep(0.5)
   led_onboard.value(0)
   utime.sleep(0.5)
   if USBpower() != 1:
      utime.sleep(1)
```

```py
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
USBpower = machine.Pin(24, machine.Pin.IN) 

if USBpower() = 1:
    print('drawing power from the USB')
else
    print('drawing power from VSYS - a battery or external power source')
```

Power consumption when running this code is approximately 0.1W (19mA at 4.99V, so 4 x AA batteries (@ 2,000mAh each) would keep the Pico running for well over 4 days

The battery should provide a voltage greater than 1.8v and less than 5.5v. Importantly if both a battery and a micro USB cable are connected at the same time a Schottky diode should be placed between the battery positive and VSYS [see section 4.4 & 4.5 of the Raspberry Pi Pico Datasheet https://datasheets.raspberrypi.org/pico ... asheet.pdf] . . . then, as long as the battery voltage is less than that coming in from the USB cable, power will be drawn from the USB supply and not the battery . . . and, when you unplug the Pico from its USB supply, the Pico will keep on running, using power from the battery (and visa versa when you plug it back in).