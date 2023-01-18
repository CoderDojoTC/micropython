from machine import Pin, PWM
from time import sleep

# pot init
POT_PIN_1 = 27
adc = machine.ADC(POT_PIN_1)


# motor stuff
HALF_POT = 32768
FORWARD_PIN = 8
REVERSE_PIN = 9
forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

counter = 0
def main():
    global counter
    while True:
        pot_value = adc.read_u16()
        if pot_value > HALF_POT:
            # forward
            reverse.duty_u16(0)
            power = pot_value - HALF_POT
            print('forward:', power)
            # cut max power by shifting on bit right (div 2)
            forward.duty_u16(power >> 1)
        else:
            forward.duty_u16(0)
            power = HALF_POT - pot_value
            # cut max power by shifting on bit right (div 2)
            reverse.duty_u16(power >> 1)
            print('reverse:', power)
        
        sleep(.1)
        counter += 1

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