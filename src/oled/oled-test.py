# Display Image I2C driven ssd1306 OLED display 
from machine import Pin, I2C
# https://github.com/stlehmann/micropython-ssd1306
from ssd1306 import SSD1306_I2C
import uos

print(uos.uname())
print("Frequency: ", str(machine.freq()), " Hz.")

WIDTH  = 128 # oled display width
HEIGHT = 64  # oled display height

sda=machine.Pin(0) # bus 0 data
scl=machine.Pin(1) # bus 0 clock

# should be 400000, 1000 prints some text
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("I2C Address Decimal:", i2c.scan())
print("I2C Address Hex: ", hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: ", str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
# oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)
#oled.fill(1)
#oled.fill(0)
#oled.show()
oled.text("Hello", 0, 0)
oled.text("Hello", 40, 20)
oled.text("Hello", 60, 30)
oled.text("Hello", 80, 40)
oled.text("Hello", 100, 50)
oled.show()

print("Done ")
