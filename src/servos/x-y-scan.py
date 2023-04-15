from time import sleep
from machine import Pin, PWM
import VL53L0X

sda=machine.Pin(0) # lower right pin
scl=machine.Pin(1) # one up from lower right pin
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

VERTICAL_PIN = 15
HORIZONTAL_PIN = 14
vpwm = PWM(Pin(VERTICAL_PIN))
vpwm.freq(50)
hpwm = PWM(Pin(HORIZONTAL_PIN))
hpwm.freq(50)

# sample values are 0.01 to 0.1
vdelay = 0.01
hdelay = 0.05
max_vangle = 7500 # lower this increase the higher angle
min_vangle = 9000 # increase this to lower the bottom angle

horz_min = 3000 # this is where we start horizontal scane
angle_span = 1000 # the angle between the min and max
horz_max = horz_min + angle_span
tof = VL53L0X.VL53L0X(i2c)
tof.start()

def read_tof():
    return tof.read() - 50

while True:

    for h_pos in range(horz_min,horz_max,50):
        hpwm.duty_u16(h_pos)
        sleep(hdelay)
        for vposition in range(max_vangle,min_vangle,50):
            vpwm.duty_u16(vposition)
            dist = read_tof()
            print(dist)
            sleep(vdelay)
        for vposition in range(min_vangle,max_vangle,-50):
            vpwm.duty_u16(vposition)
            dist = read_tof()
            print(dist)
            sleep(vdelay)

