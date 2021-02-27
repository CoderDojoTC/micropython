# OLED Potentiometer Example

In this lesson, we will use a potentiometer to change the value of an OLED display.  We will use a small SSD1306 with an I2C interface.

## Circuit Diagram

![](img/oled-i2c-clock-data.png)

![](img/oled-pot-lab-pins.png)
## Sample Code

## Testing the POT

GP26 is the same as ADC0.  This is pin number 31 on the Pico.

```py
import machine
import utime
 
POT_PIN = machine.ADC(26)
 
while True:
    print(POT_PIN.read_u16())
    utime.sleep(2)
```

## Testing the OLED

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