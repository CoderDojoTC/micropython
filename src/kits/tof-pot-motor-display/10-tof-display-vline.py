# VL53L0X Display Test

from machine import Pin, I2C
import VL53L0X
import ssd1306
from utime import sleep

WIDTH  = 128
HEIGHT = 64
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
TOF_MAX_VALUE = 200 # dist in cm anything beyond this we will ignore
TOF_MIN_OFFSET = 35 # subtract from raw sensor
TOF_SCALE = 0.5 # scale the result

# map a value from one rante into another range
# checks for divide by zero
def map(value, istart, istop, ostart, ostop):
  # check ff (istop - istart)
  if (istop - istart) == 0:
      return ostop
  else:
      return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

def update_display(dist):
    oled.fill(0)
    if dist < TOF_MAX_VALUE:
        print('dist:', dist)
        oled.text('Distance:'+ str(round(dist))+'cm', 0, 56, 1)
        # convert to a scale of 0 to 127
        tofX = map(dist, 0, TOF_MAX_VALUE, 0, WIDTH)
        oled.vline(tofX, 0, HEIGHT, 1)
    else:
        print('out of range:', dist)
        oled.text('Out of range', 0, 0, 1)
    oled.show()

def dist_cm():
    tof_value = tof.read()
    # these constants need clibration
    dist_in_cm = (tof_value - TOF_MIN_OFFSET) * TOF_SCALE
    if dist_in_cm < 0:
        return 0
    elif dist_in_cm > TOF_MAX_VALUE:
        return TOF_MAX_VALUE
    else:
        return dist_in_cm

tof.start()
while True:
    # get distace in cm
    dist = dist_cm()
    update_display(dist)
    sleep(.1)
    
