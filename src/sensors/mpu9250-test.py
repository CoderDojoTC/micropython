import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=I2C(0, sda=sda, scl=scl, freq=400000)
print("Found I2C device at decimal", i2c.scan())
print('Expecting [104, 118]')

sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)