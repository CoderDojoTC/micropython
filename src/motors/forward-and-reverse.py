from machine import Pin, PWM
from time import sleep

pot = machine.ADC(26)
# lower right pins with USB on top
FORWARD_PIN = 16
REVERSE_PIN = 17

MAX_POWER = 65025

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

def main():
    while True:
        for i in range(0,  MAX_POWER, 1024):
            print(i)
            forward.duty_u16(i)
            sleep(.1)
        forward.duty_u16(0)
        for i in range(0,  MAX_POWER, 1024):
            print(i)
            reverse.duty_u16(i)
            sleep(.1)
        reverse.duty_u16(0)
try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    forward.duty_u16(0)
    reverse.duty_u16(0)