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
# vertical delay moving the scanner down
vdelay = 0.04

# return delay moving the scanner back up - no data being collected
updelay = 0.01
hdelay = 0.05
max_vangle = 7500 # lower this increase the higher angle
min_vangle = 9000 # increase this to lower the bottom angle
step = 25

horz_min = 3000 # this is where we start horizontal scane
angle_span = 1000 # the angle between the min and max
horz_max = horz_min + angle_span
tof = VL53L0X.VL53L0X(i2c)
tof.start()

def read_tof():
    return tof.read() - 20


print('depth = [')
# for each horizontal position gather a stripe of data
for h_pos in range(horz_min,horz_max,step):
    hpwm.duty_u16(h_pos)
    sleep(hdelay)
    print('[', end='')
    for vposition in range(max_vangle,min_vangle,step):
        vpwm.duty_u16(vposition)
        dist = read_tof()
        if vposition < min_vangle - step:
            print(dist, ', ', sep='', end='')
        else:
            if h_pos < horz_max
                print(dist, '],', sep='')
            else:
                print(dist, ']')
        sleep(vdelay)
    # move the servo back up but don't gather data
    for vposition in range(min_vangle,max_vangle,-step):
        vpwm.duty_u16(vposition)
#             dist = read_tof()
#             if vposition > max_vangle:
#                 print(dist, ', ', sep='', end='')
#             else:
#                 print(dist)
        sleep(updelay)
print(']')