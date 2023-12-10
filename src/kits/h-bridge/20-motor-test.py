from machine import Pin, PWM
from utime import sleep

MAX_POWER_LEVEL = 65025
# lower right pins with USB on top
RIGHT_FORWARD_PIN = 8
RIGHT_REVERSE_PIN = 9
LEFT_FORWARD_PIN = 11
LEFT_REVERSE_PIN = 10


forward = PWM(Pin(RIGHT_FORWARD_PIN))
reverse = PWM(Pin(RIGHT_REVERSE_PIN))
# set the frequencey to be 50 Khz
forward.freq(50)
reverse.freq(50)

while True:
    print('forward')
    forward.duty_u16(MAX_POWER_LEVEL)
    reverse.duty_u16(0)
    sleep(2)

    print('reverse')
    reverse.duty_u16(MAX_POWER_LEVEL)
    forward.duty_u16(0)
    sleep(2)

    print('stop')
    reverse.duty_u16(0)
    forward.duty_u16(0)
    sleep(3)