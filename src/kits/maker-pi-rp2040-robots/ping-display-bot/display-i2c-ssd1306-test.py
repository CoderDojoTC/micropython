import machine
from utime import sleep
from ssd1306 import SSD1306_I2C

# import config.py
OLED_SDA_PIN=16
OLED_SCL_PIN=17

sda=machine.Pin(OLED_SDA_PIN) # row one on our standard Pico breadboard
scl=machine.Pin(OLED_SCL_PIN) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("CoderDojo Rocks!", 0, 0)
oled.show()
print('Done')
    
