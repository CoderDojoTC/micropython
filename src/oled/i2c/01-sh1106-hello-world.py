from machine import Pin, I2C
import sh1106

sda=machine.Pin(16)
scl=machine.Pin(17)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

display.fill(0)
display.text('CoderDojo', 0, 0, 1)
display.show()

print('done')