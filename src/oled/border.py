import machine
import utime
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl)
# Screen size
width=128
height=64
oled = SSD1306_I2C(width, height, i2c)

oled.hline(0, 0, width - 1, 1) # top edge
oled.hline(0, height - 1, width - 1, 1) # bottom edge
oled.vline(0, 0, height - 1, 1) # left edge
oled.vline(width - 1, 0, height - 1, 1) # right edge
oled.show()