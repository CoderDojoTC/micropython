# Running lights

This program turns on all 24 blue LEDs on the board, one at a time.  It then turns them all off.

TODO - record a GIF or video.

```py
import machine
import utime

# RUNNING LIGHT

for i in range(29):                     # from 0 to 28  
    if i != 23 and i != 24:             # pin 23 and 24 are not GPIO pins
        machine.Pin(i,machine.Pin.OUT)  # set the pins to output

while True:
    for i in range(29):                      
        if i != 23 and i != 24:      
            machine.Pin(i).value(0)     # turn off the LED
            utime.sleep(0.1)            # sleep for 100ms
            machine.Pin(i).value(1)     # turn on the LED
            
    for i in range(28,-1,-1):           # from 28 to 0
        if i != 23 and i != 24:
            machine.Pin(i).value(1)     # turn on the LED
            utime.sleep(0.1)
            machine.Pin(i).value(0)     # turn off the LED
```

## References

This program was taken from tje Cytron GitHub site [here](https://github.com/CytronTechnologies/MAKER-PI-PICO/blob/main/Example%20Code/MicroPython/maker-pi-pico-running-light.py).