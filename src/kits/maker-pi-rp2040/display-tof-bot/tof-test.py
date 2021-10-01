# Test program for VL53L0X
import time
from machine import Pin
from machine import I2C
import VL53L0X

# Test program for VL53L0X
import time
from machine import Pin
from machine import I2C
import VL53L0X

I2C_SDA_PIN = 26
I2C_SCL_PIN = 27
i2c=machine.I2C(1,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

while True:
    tof.start()
    tof.read()
    print(tof.read())
    tof.stop()
    time.sleep(0.1)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

while True:
    tof.start()
    tof.read()
    print(tof.read())
    tof.stop()
    time.sleep(0.1)