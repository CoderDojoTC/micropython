from machine import PWM, Pin
from utime import sleep

# Motor Setup
# motors just barely turn at this power level
MAX = 65025
# lower right pins with USB on top
FOR_PIN = 16
REV_PIN = 17


forward = PWM(Pin(FOR_PIN))
reverse = PWM(Pin(REV_PIN))
forward.freq(50)
reverse.freq(50)

while True:
    print('forward')
    forward.duty_u16(MAX)
    reverse.duty_u16(0)
    sleep(2)
    
    print('stop')
    forward.duty_u16(0)
    sleep(2)
    
    print('reverse')
    reverse.duty_u16(MAX)
    sleep(2)
    
    print('stop')
    reverse.duty_u16(0)
    sleep(2)
    
