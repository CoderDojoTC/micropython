# VL53L0X Display Test

from machine import Pin, I2C
import VL53L0X
import ssd1306
from utime import sleep

WIDTH  = 128
HEIGHT = 64
CS = machine.Pin(1)
SCL = machine.Pin(2)
SDA = machine.Pin(3)
DC = machine.Pin(4)
RES = machine.Pin(5)
spi=machine.SPI(0, sck=SCL, mosi=SDA)
# print(spi)

display = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

sda=machine.Pin(18) # row one on our standard Pico breadboard
scl=machine.Pin(19) # row two on our standard Pico breadboard
i2c=machine.I2C(1, sda=sda, scl=scl, freq=400000)

tof = VL53L0X.VL53L0X(i2c)


tof.start()
while True:
    dist = tof.read()
    dist = (dist - 30) >> 1
    print(dist)
    display.fill(0)
    display.text('Distance:', 0, 0, 1)
    display.text(str(dist), 20, 20, 1)
    display.show()
    sleep(.1)
    