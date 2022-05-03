import machine
from time import sleep
from ssd1306 import SSD1306_I2C

# reset
OLEDinit = machine.Pin(15, machine.Pin.OUT)
OLEDinit.low()
sleep(0.1)
OLEDinit.high()

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
print (i2c.scan())

oled = SSD1306_I2C(128, 32, i2c)
oled.fill(0)
oled.show()

oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()