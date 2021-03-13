# OLED Setup

## SSD1306 I2C Setup

```py
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)
```
## ## SSH1106 I2C Setup

```py
from machine import Pin, I2C
import sh1106

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)
```
