from machine import PWM, Pin
from utime import sleep

# Motor Setup
MAX = 65025
# lower right pins with USB on top
FOR_PIN = 16
REV_PIN = 17


forward = PWM(Pin(FOR_PIN))
reverse = PWM(Pin(REV_PIN))
forward.freq(50)
# turn off the reverse motor
reverse.duty_u16(0)

while True:
    print('forward')
    forward.duty_u16(MAX)
    sleep(2)
    
    print('stop')
    forward.duty_u16(0)
    sleep(2)