# Test program for VL53L0X
import time
from machine import Pin, I2C
import ssd1306
import VL53L0X

sda=machine.Pin(26)
scl=machine.Pin(27)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

WIDTH = 128
HEIGHT = 64
SCK=machine.Pin(2)
SDL=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDL)
RES = machine.Pin(13)
DC = machine.Pin(14)
CS = machine.Pin(15)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

tof = VL53L0X.VL53L0X(i2c)

tof.start()
while True:
    tof.read()
    print(tof.read())
    oled.fill(0)
    oled.text("CoderDojo Robot", 0, 0)
    oled.text("P1:", 0, 20)
    oled.text(str(tof.read()), 40, 20)
    oled.show()
    time.sleep(0.05)

# tof.stop()