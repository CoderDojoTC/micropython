from machine import Pin, PWM
from time import sleep

# lower right pins with USB on top
FORWARD_PIN = 18
REVERSE_PIN = 19

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))
forward.freq(50)
forward.freq(50)

forward.duty_u16(0)
reverse.duty_u16(0)
print('Motor Stopped')