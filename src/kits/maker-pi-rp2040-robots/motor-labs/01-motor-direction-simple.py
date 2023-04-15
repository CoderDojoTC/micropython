from machine import Pin, PWM
from time import sleep

# power is 0 to 65025
# 3700 just barely moves a DC motor sometimes
POWER_LEVEL = 30000
# lower right pins with USB on top
FORWARD_PIN = 8
REVERSE_PIN = 9

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

delay_time = 1 # 1 second
def main():
    while True:        

        forward.duty_u16(POWER_LEVEL)
        reverse.duty_u16(0)
        sleep(delay_time)
        
        forward.duty_u16(0)
        sleep(delay_time)
        
        reverse.duty_u16(POWER_LEVEL)
        sleep(delay_time)

        reverse.duty_u16(0)
        sleep(delay_time)
        
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