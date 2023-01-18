from machine import Pin, PWM
from time import sleep

FORWARD_PIN = 16

MAX_POWER = 65025

forward = PWM(Pin(FORWARD_PIN))

counter = 0
def main():
    while True:
        for i in range(0,  MAX_POWER, 1000):
            print(i)
            forward.duty_u16(i)
            sleep(.1)

try:
    main()
except KeyboardInterrupt:
    print('Got an interrupt.')
finally:
    print('Powering down the motor.')
    forward.duty_u16(0)