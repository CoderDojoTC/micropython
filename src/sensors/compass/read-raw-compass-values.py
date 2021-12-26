from array import array
I2C_SDA_PIN = 0
I2C_SCL_PIN = 1
i2c=machine.I2C(0,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)
data = array('B', [0] * 6)
while True:
    i2c.readfrom_mem_into(0x1e, 0x03, data)
    print(data)