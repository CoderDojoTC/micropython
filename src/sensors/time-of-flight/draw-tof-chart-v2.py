from machine import Pin,PWM
import VL53L0X
from time import sleep
import ssd1306
from neopixel import NeoPixel

# OLED Display dimentions
HEIGHT = 64
WIDTH = 128
MAX_TOF_VALUE = 1200

SCL = machine.Pin(2)
SDA = machine.Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=SCL, mosi=SDA)
print(spi)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

sda=machine.Pin(0) # row one on our standard Pico breadboard
scl=machine.Pin(1) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print('i2c:', i2c)

tof = VL53L0X.VL53L0X(i2c)
tof.start()

x=0
def update_display(distance):
    global x
    print(x, distance)
    if distance > 63:
        distance = 63
    oled.pixel(x,HEIGHT - int(distance) - 1, 1)
    if x > WIDTH - 3:
        oled.scroll(-1,0)
    else:
        x += 1
    oled.show()

# time of flight calibration parameters
zero_dist = 65 # distance measure when an object is about 1/2 cm away
max_dist = 350 # max distance we are able to read
scale_factor = .2

# get the normalized time-of-flight distance
def get_distance():
    global zero_dist, scale_factor
    tof_distance = tof.read()
    if tof_distance > max_dist:
        return tof_distance
    # if our current time-of-flight distance is lower than our zero distance then reset the zero distance
    if tof_distance < zero_dist:
        zero_dist = tof_distance
    return  int((tof_distance - zero_dist) * scale_factor)

# a list of our prior distance measurements for graphing mode
distances=[]

valid_distance = 0
mode = 0
# loop forever
def main():
    global mode, valid_distance
    while True:
        distance = get_distance()      
        if distance < MAX_TOF_VALUE:
            update_display(distance)
        sleep(.05)
        

# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrupt
print('Running Chart Time of Flight')

try:
    main()
except KeyboardInterrupt:
    print('Got interupt')
finally:
    # Optional cleanup code
    print('Powering down sound')
    tof.stop()
