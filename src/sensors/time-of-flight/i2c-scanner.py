import machine
sda=machine.Pin(16) # lower right corner pin
scl=machine.Pin(17) # one up from lower right corner
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("Device found at decimal", i2c.scan())