# Ultrasonic Ping Sensor
The HC-SR04 is a low cost ($4) sensor that measures the distance to an object in front of it.

## Wiring Diagram

1. Connect GND to any GND pin on the Pico
2. Connect VCC to VBUS or 5 Volt power
3. Connect Trigger to pin 15.  With USB on the top, this pin is the bottom left corner.
4. Connect Echo to pin 14.  One up from bottom left corner.

## Sample Code

```py
# Sample code to test HC-SR04 Ultrasonice Ping Sensor
# Connect GND to any GND pin on the Pico
# Connnect VCC to VBUS or 5 Volt power

from machine import Pin, Timer
import utime

TRIGGER_PIN = 15 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 14 # One up from bottom left corner

# Init HC-SR04 pins
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back

def ping():
    trigger.low()
    utime.sleep_us(2) # Wait 2 microseconds low
    trigger.high()
    utime.sleep_us(5) # Stay high for 5 miroseconds
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

while True:
    print("Distance:", ping(), " cm")
    utime.sleep(.25)
```

## OLED

If you have a small OLED screen, you can also display the results
of the distance measurement directly on an OLED screen.

See the OLED example here: [OLED Ping Example](../displays/graph/11-oled-ping.md)