from machine import Pin, PWM
from utime import sleep

MAX_POWER_LEVEL = 65025
# lower right pins with USB on top
FORWARD_PIN = 8
REVERSE_PIN = 9

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

# set the frequencey to be 50 Khz
forward.freq(50)
reverse.freq(50)

# turn off the PWM
reverse.duty_u16(0)
forward.duty_u16(0)
