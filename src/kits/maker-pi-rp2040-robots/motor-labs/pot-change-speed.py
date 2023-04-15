from utime import sleep
from machine import Pin, PWM
from time import sleep

# power is 0 to 65025
# 3700 just barely moves a DC motor sometimes
MAX_POWER_LEVEL = 30000
# lower right pins with USB on top
FORWARD_PIN = 8
REVERSE_PIN = 9
POT_PIN_1 = 26

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

adc = machine.ADC(POT_PIN_1)

def main():
    while True:
        pot_value = adc.read_u16()
        # shift two bits right (divide by 4)
        power = pot_value >> 2
        print(pot_value, power)
        forward.duty_u16(power)
        reverse.duty_u16(0)
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