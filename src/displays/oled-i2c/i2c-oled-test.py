import machine
from time import sleep
from ssd1306 import SSD1306_I2C

# reset the display on setup
OLEDinit = machine.Pin(15, machine.Pin.OUT)
OLEDinit.low()
sleep(0.1)
OLEDinit.high()

#now we can get to the I2C interface
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
print (i2c.scan())

# setup the display driver using the i2c interface
oled = SSD1306_I2C(128, 64, i2c)
oled.text('CoderDojo Rocks!', 0, 0)
oled.show()