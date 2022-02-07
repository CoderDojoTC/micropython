from hmc5883l import HMC5883L
# from https://github.com/gvalkov/micropython-esp8266-hmc5883l

I2C_DATA_PIN = 0
I2C_CLOCK_PIN = 1

I2C_SDA_PIN = 0
I2C_SCL_PIN = 1

i2c=machine.I2C(0,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)

print(i2c)

sensor = HMC5883L(scl=I2C_DATA_PIN, sda=I2C_CLOCK_PIN)

x, y, z = sensor.read()
print(sensor.format_result(x, y, z))