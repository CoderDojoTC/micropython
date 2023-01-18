# The heading changes from 0 to 360 as you rotate the sensor around the vertical axis
from machine import I2C
from hmc5883l import HMC5883L
from time import sleep

# Please check that correct PINs are set on hmc5883l library!
# The declination is based on using Minneapolis as a city
sensor = HMC5883L(scl=13, sda=12, declination=(0, 71))

while True:
    sleep(.5)
    x, y, z = sensor.read()
    print(sensor.heading(x, y)[0])