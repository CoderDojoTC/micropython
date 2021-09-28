# Program to calibrate the VL53L0X time-of-flight sensor by monitoring minimum distance
from utime import sleep
from machine import Pin
from machine import I2C
import ssd1306
import VL53L0X

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

I2C_SDA_PIN = 26
I2C_SCL_PIN = 27
i2c=machine.I2C(1,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)

MAX_DIST = 1000
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)
tof.start()

min_dist = MAX_DIST
while True:
    dist = tof.read()
    # register new min distance?
    if dist < min_dist:
        min_dist = dist
        print('min dist:', min_dist)
    print(dist)
    oled.fill(0)
    oled.text('dist:', 0, 0, 1)
    oled.text(str(dist), 50, 0, 1)
    oled.text('min dist:', 0, 10, 1)
    oled.text(str(min_dist), 70, 10, 1)
    oled.text('cal dist:', 0, 20, 1)
    oled.text(str(dist - min_dist), 70, 20, 1)
    oled.show()  
    sleep(0.2)