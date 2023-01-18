# Test display connections

from machine import Pin, I2C
from utime import sleep
import ssd1306

WIDTH  = 128
HEIGHT = 64

# for SPI0, the clock should be on 2 and data on 3
# https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#pinout-and-design-files
SCL = machine.Pin(2)
SDA = machine.Pin(3)

RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)
spi=machine.SPI(0, sck=SCL, mosi=SDA)
# print(spi)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)              # Init oled display

counter = 0
while True:
    oled.fill(0)
    oled.text(str(counter), 0, 1)
    oled.show()
    sleep(1)
    counter += 1

    