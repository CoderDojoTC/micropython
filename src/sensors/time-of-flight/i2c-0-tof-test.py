
from machine import Pin,PWM
from utime import sleep
import VL53L0X

sda=Pin(0) # Grove connector 6
scl=Pin(1) # Colors on ToF sensor are RBYW (red, black, yellow white)
i2c_tof=machine.I2C(0, sda=sda, scl=scl)

print(i2c_tof)
print(i2c_tof.scan())

tof = VL53L0X.VL53L0X(i2c_tof)
tof.start()

while True:
    tof_distance = tof.read()
    print(tof_distance)
    sleep(.2)
    