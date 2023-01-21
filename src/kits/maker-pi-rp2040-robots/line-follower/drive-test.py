from machine import Pin, PWM
from time import sleep

# lower right pins with USB on top
RIGHT_FORWARD_PIN = 11
RIGHT_REVERSE_PIN =10
LEFT_FORWARD_PIN = 8
LEFT_REVERSE_PIN = 9

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

MAX_POWER_LEVEL = 65025
QUARTER_POWER = 65025 >> 2
SLOW_DRIVE_POWER = 26000

# while True:
def spin_wheel(pwm):
    pwm.duty_u16(SLOW_DRIVE_POWER)
    sleep(2)
    pwm.duty_u16(0)
    sleep(1)

def stop():
    right_forward.duty_u16(0)
    right_reverse.duty_u16(0)
    left_forward.duty_u16(0)
    left_reverse.duty_u16(0)    
    
def main():
    while True:
        print('right forward')
        spin_wheel(right_forward)
        
        print('right reverse')
        spin_wheel(right_reverse)
        
        print('left foward')
        spin_wheel(left_forward)
        
        print('left_reverse')
        spin_wheel(left_reverse)
# end of main()

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    stop()
