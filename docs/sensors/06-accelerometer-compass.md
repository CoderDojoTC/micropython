# MPU-9250 Accelerometer Gyroscope Compass

The MPU-9250 by InvenSense is a nine-axis motion tracking device.  It includes:

1. A MPU-6500, which contains a 3-axis accelerometer and a 3-axis gyroscope and 
2. A AK8963, the market leading 3-axis digital compass that senses magnetic fields

(Gyro + Accelerometer + Compass) MEMS MotionTracking™ Device

1PCS GY-91 10DOF Accelerometer Gyroscope Compass Temp/Pressure MPU-9250 BMP-280

* [Art of Circuits](https://artofcircuits.com/product/10dof-gy-91-4-in-1-mpu-9250-and-bmp280-multi-sensor-module)

## Pinouts

1. VIN: Voltage Supply Pin
1. 3V3: 3.3v Regulator output
1. GND: 0V Power Supply
1. SCL: I2C Clock / SPI Clock
1. SDA: I2C Data or SPI Data Input
1. SDO/SAO: SPI Data output / I2C Slave Address configuration pin
1. NCS: Chip Select for SPI mode only for MPU-9250
1. CSB: Chip Select for BMP280

You only need to hook the 3.3 to VIN, the GND to GND and the SCL and SDA.  The other connections are not needed.

## I2C Scanner Results

```py
import machine
sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("Device found at decimal", i2c.scan())
```

Device found at decimal [104, 118]

## MPU9250 Drivers

[MicroPython Driver](https://github.com/tuupola/micropython-mpu9250)

```py
import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)
```

## References

[MEMS YouTube Video](https://www.youtube.com/watch?v=9X4frIQo7x0) The ingenious micro mechanisms inside your phone