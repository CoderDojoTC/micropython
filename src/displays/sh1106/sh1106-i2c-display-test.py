from machine import Pin, I2C
import sh1106

OLED_SDA_PIN=16
OLED_SCL_PIN=17
sda=machine.Pin(OLED_SDA_PIN)
scl=machine.Pin(OLED_SCL_PIN)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)
print(i2c)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(20), 0x3c)
display.sleep(False)
display.fill(0)
display.text('Testing 1', 0, 0, 1)
display.show()
