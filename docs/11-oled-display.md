# OLED Display

## I2C Scanner
```py
import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
print(i2c.scan())
```

returns: [60]

## Install SSD1306 Module

![](img/install-ssd1306.png)

## ssd1306 module

[SSD1306 Library](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py) - click the RAW button and then right click to do a "Save As"


## SSD1306 vs. SH1106
There is only one small difference between SSD1306 and SH1106: The SH1106 controller has an internal RAM of 132x64 pixel. The SSD1306 only has 128x64 pixel.

## References

[robert-hh's SH1106 Driver](https://github.com/robert-hh/SH1106)

https://www.mfitzp.com/article/oled-displays-i2c-micropython/

https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/blob/master/examples/ssd1306_stats.py