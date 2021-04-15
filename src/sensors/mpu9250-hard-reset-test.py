import utime
from machine import I2C, Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S

# micropython.alloc_emergency_exception_buf(100)

sda=machine.Pin(16) # second from bottom right
scl=machine.Pin(17) # bottom right corner
i2c=I2C(0, sda=sda, scl=scl, freq=400000)

mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)