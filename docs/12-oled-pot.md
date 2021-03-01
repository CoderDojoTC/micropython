# OLED Potentiometer Example

In this lesson, we will use a potentiometer to change the value of an OLED display.  We will use a small SSD1306 OLED with an I2C interface.

A potentiometer has three wires.  The two outside wires connect to GND and the 3.3 volt output.  The center wire, called the "tap" wire will connect to the pin that converts an continuous analog voltage value into a digital number.

[Wikipedia Page on Potentiometer](https://en.wikipedia.org/wiki/Potentiometer)

## Circuit Diagram

![](img/oled-i2c-clock-data.png)

![](img/oled-pot-lab-pins.png)
## Sample Code

## Testing the POT

Our first task is to find what pin to use for our first Analog to Digital concerter. GP26 is the same as ADC0.  This is pin number 31 on the Pico.

```py
import machine
import utime
pot = machine.ADC(26)
while True:
    print(pot.read_u16())
    utime.sleep(.2)
```
### Sample 16 bit output
A 16-bit integer can store 216 (or 65,536) distinct values. In an unsigned representation, these values are the integers between 0 and 65,535.  So we are expecting numbers from 0 to 65,535.

Sample results as we move the potentiometer from the minimum to the maximum values.
```data
65535
52844
31047
7745
256
352
19140
41114
62239
65535
57277
33384
10114
352
288
19940
28086
```

## Testing the OLED

### Getting the defaults

```py
from machine import Pin, I2C
# i2c=machine.I2C(0)
i2c=machine.I2C(0)
print("Device found at decimal", i2c.scan())
print(i2c)
```

Results:
This tells you the default pins and frequency that the I2C bus is running at.

```data
Device found at decimal [60]
I2C(0, freq=399361, scl=9, sda=8)
```

```data
Device found at decimal [60]
I2C(0, freq=399361, scl=1, sda=0)
```

This tells us that the default pins are GP9 (row 12) for clock and GP8 (row 11) for data.

```py
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
WIDTH  = 128
HEIGHT = 32
i2c = I2C(0) # Init I2C using I2C0 defaults SCL on GP9 (12) and SDA on GP8 (11) 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.text("CoderDojo Rocks",0,0)
oled.show()
```

## Full Program

```py
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
WIDTH  = 128
HEIGHT = 32
i2c = I2C(0) # Init I2C using I2C0 defaults SCL on GP9 (12) and SDA on GP8 (11) 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

POT_PIN = machine.ADC(26)
 
while True:
    oled.fill(0)
    oled.text(POT_PIN.read_u16())
    oled.show()
    utime.sleep(.2)
```