# Measuring VSys

You need to set GP25 to output and set it high and also set GP29 to input with no pull resistors before reading. 
And don't forget that the input from VSYS to ADC is divided by 3, so you have to multiply your result to get real value. 
When I do that I get around 4.7 V when powered from USB, so it definitely works.

https://forums.raspberrypi.com/viewtopic.php?t=301152

```py
import machine

# Vsys = machine.ADC(3)
Vsys = machine.ADC(29)
conversion_factor = (3.3 / (65535)) * 3

reading = Vsys.read_u16() * conversion_factor

print(reading)
```
