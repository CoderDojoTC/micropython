# The heading changes from 0 to 360 as you rotate the sensor around the vertical axis
from machine import I2C, Pin
from hmc5883l import HMC5883L
from time import sleep
from neopixel import NeoPixel

# Please check that correct PINs are set on hmc5883l library!
sensor = HMC5883L(scl=13, sda=12, declination=(0, 71))

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 24
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    x, y, z = sensor.read()
    heading = sensor.heading(x, y)[0]
    # scale 0 to 360 to be in the 0 to 23 range
    # add a few index so we point north
    index = round(heading/15) - 10
    # wrap neg and above 360
    index = (NUMBER_PIXELS - index) % NUMBER_PIXELS
    print(heading, index)
    for i in range(0, NUMBER_PIXELS):
        if i == index:
            # turn index red pixel on for and delay
            strip[i] = (100,70,100)
        else:
            strip[i] = (0,0,0)
    strip.write()
    sleep(.5)
    