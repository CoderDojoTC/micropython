# I2C Scanner
import machine
from time import sleep
from ssd1306 import SSD1306_I2C
sda=machine.Pin(2)
scl=machine.Pin(3)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

WIDTH=128
HEIGHT=64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

HALF_WIDTH = int(WIDTH/2)
HALF_HEIGHT = int(HEIGHT/2)

OFF = 0
ON = 1
FILL_OFF = 0
FILL_ON = 1
QUAD_CODE = 1

delay = 1
while True:  
    for quad_code in range(1,16):
        oled.fill(0)
        oled.text("elipse " + str(quad_code), 0, 0, 1)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, 50, 20, ON, FILL_OFF, quad_code)
        oled.show()
        sleep(delay)
    for quad_code in range(1,16):
        oled.fill(1)
        oled.text("elipse " + str(quad_code), 0, 0, 0)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, 50, 20, OFF, FILL_OFF, quad_code)
        oled.show()
        sleep(delay)
    for quad_code in range(1,16):
        oled.fill(0)
        oled.text("elipse " + str(quad_code), 0, 0, 1)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, 50, 20, ON, FILL_ON, quad_code)
        oled.show()
        sleep(delay)
    for quad_code in range(1,16):
        oled.fill(1)
        oled.text("elipse " + str(quad_code), 0, 0, 0)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, 50, 20, OFF, FILL_ON, quad_code)
        oled.show()
        sleep(delay)