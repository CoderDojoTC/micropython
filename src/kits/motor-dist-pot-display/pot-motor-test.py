from machine import Pin, PWM, ADC
from utime import sleep

# lower right pins with USB on top
FORWARD_PIN = 19
REVERSE_PIN = 18

# ADC0 is GPIO 26.  Connect to row 10 the right side.
pot = ADC(26)

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

POWER_LEVEL = 65025
    
def main():
    while True:
        pot_value = pot.read_u16()
        print('pot val', pot_value)
        forward.duty_u16(pot_value)
        sleep(.1)

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Cleanup code
    print('Cleaning up')
    print('Powering motor now.')
    forward.duty_u16(0)
    reverse.duty_u16(0)
