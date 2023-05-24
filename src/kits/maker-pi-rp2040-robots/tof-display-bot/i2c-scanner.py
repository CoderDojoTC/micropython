# I2C Scanner
import machine
sda=machine.Pin(26)
scl=machine.Pin(27)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)
print('This should return [41]')
print(i2c.scan())