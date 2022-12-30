# turn on the plot function of Thonny
# The "Z" is how much upsidedown the sensor is
# When the sensor is right-side up the values is -660
# When the sensor is up-side-down the value is 260
# tilted it goes to 290
from machine import I2C
from hmc5883l import HMC5883L
from time import sleep

sensor = HMC5883L(scl=13, sda=12)

while True:
    x, y, z = sensor.read()
    print(x, y, z)
    sleep(.3)