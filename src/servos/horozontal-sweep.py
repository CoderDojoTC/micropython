from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(14))
pwm.freq(50)

delay = 0.04
min = 3000
angle_span = 1000
max = min + angle_span

while True:
    for position in range(min,max,50):
        pwm.duty_u16(position)
        sleep(delay)
    for position in range(max,min,-50):
        pwm.duty_u16(position)
        sleep(delay)