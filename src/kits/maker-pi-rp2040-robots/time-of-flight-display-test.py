# Test program for VL53L0X
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import VL53L0X

I2C0_SDA_PIN = 0
I2C0_SCL_PIN = 1
I2C1_SDA_PIN = 2
I2C1_SCL_PIN = 3
i2c0=machine.I2C(0,sda=machine.Pin(I2C0_SDA_PIN), scl=machine.Pin(I2C0_SCL_PIN))
i2c1=machine.I2C(1,sda=machine.Pin(I2C1_SDA_PIN), scl=machine.Pin(I2C1_SCL_PIN), freq=400000)

oled = SSD1306_I2C(128, 64, i2c0)
tof = VL53L0X.VL53L0X(i2c1)

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