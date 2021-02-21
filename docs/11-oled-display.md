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

## SH1106 Example

```py
from machine import Pin, I2C
import sh1106

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

display.fill(0)
display.text('CoderDojo', 0, 0, 1)
display.show()

print('done')
```

## Counter Example

```py
from machine import Pin, I2C
import sh1106
import utime

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

for i in range(1, 11):
    display.fill(0) # clear to black
    display.text('CoderDojo Rocks', 0, 0, 1) # at x=0, y=0, white on black
    display.text(str(i), 10, 20, 1)
    display.show() # update display
    utime.sleep(0.5)

print('done')
```

## Drawing Functions


        self.fill = fb.fill
        self.fill_rect = fb.fill_rect
        self.hline = fb.hline
        self.vline = fb.vline
        self.line = fb.line
        self.rect = fb.rect
        self.pixel = fb.pixel
        self.scroll = fb.scroll
        self.text = fb.text
        self.blit = fb.blit


## Animated Box
This draws a title and four lines around a drawing area.  It then draws boxes that move to the right.

```py
from machine import Pin, I2C
import sh1106
import utime

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

display.fill(0) # clear to black
display.text('CoderDojo Rocks', 0, 0, 1) # at x=0, y=0, white on black
# line under title
display.hline(0, 9, 127, 1)
# bottom of display
display.hline(0, 30, 127, 1)
# left edge
display.vline(0, 10, 32, 1)
# right edge
display.vline(127, 10, 32, 1)

for i in range(0, 118):
    # box x0, y0, width, height, on
    display.fill_rect(i,10, 10, 10, 1)
    # draw black behind number
    display.fill_rect(10, 21, 30, 8, 0)
    display.text(str(i), 10, 21, 1)
    display.show() # update display
    # utime.sleep(0.001)

print('done')
```

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

https://github.com/robert-hh/SH1106/blob/master/sh1106.py