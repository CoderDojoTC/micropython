from time import sleep
from machine import Pin, PWM

VERTICAL_PIN = 15
pwm = PWM(Pin(VERTICAL_PIN))
pwm.freq(50)

# sample values are 0.01 to 0.1
delay = 0.05
max_angle = 7500 # lower this increase the higher angle
min_angle = 9000 # increase this to lower the bottom angle

while True:
    
    for position in range(max_angle,min_angle,50):
        pwm.duty_u16(position)
        sleep(delay)
    for position in range(min_angle,max_angle,-50):
        pwm.duty_u16(position)
        sleep(delay)