from machine import Pin, PWM
from time import sleep

pot = machine.ADC(26)
# lower right pins with USB on top
FORWARD_PIN = 16
REVERSE_PIN = 17

MAX_POWER = 65025
POT_MAX = 65025
HALF_POT = int(POT_MAX / 2)

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

counter = 0
def main():
    while True:
        global counter
        pot_val = pot.read_u16()
        if pot_val > HALF_POT:
            reverse.duty_u16(0)
            speed = (pot_val - HALF_POT)*2
            forward.duty_u16(speed)
            print('forward', speed)
        else:
            forward.duty_u16(0)
            speed = (HALF_POT - pot_val)*2
            reverse.duty_u16(speed)
            print('reverse', speed)
        counter += 1
        sleep(.1)

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