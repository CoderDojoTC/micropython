import machine
from utime import sleep
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

# Screen size
width=128
height=64
oled = SSD1306_I2C(width, height, i2c)

oled.fill(0)
# draw yellow border in top 17 lines
oled.rect(0, 0, width-1, 16, 1)
# draw blue border from 18 to 64
oled.rect(0, 17, width-1, height-17, 1)
oled.show()