
import machine
sda=machine.Pin(16)
scl=machine.Pin(17)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
print(i2c.scan())