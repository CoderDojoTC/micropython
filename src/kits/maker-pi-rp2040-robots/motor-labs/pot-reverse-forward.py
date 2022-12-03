from utime import sleep
from machine import Pin, PWM
from time import sleep

FORWARD_PIN = 9
REVERSE_PIN = 8
POT_PIN_1 = 26

# Power is an integer 0 to 65025
# We only need 1/4 of power for the demos
MAX_POWER_LEVEL = 16384
HALF_POT = 32768

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

adc = machine.ADC(POT_PIN_1)

def main():
    while True:
        pot_value = adc.read_u16()
        if pot_value > HALF_POT:
            # forward
            reverse.duty_u16(0)
            power = pot_value - HALF_POT
            print('forward:', power)
            forward.duty_u16(power)
        else:
            forward.duty_u16(0)
            power = HALF_POT - pot_value
            reverse.duty_u16(power)
            print('reverse:', power)
        sleep(.05)

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