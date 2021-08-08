# program to fade the builtin LED slowly on and off
from machine import PWM, Pin
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(100)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)