from machine import Pin, PWM
import time # sleep

POWER_LEVEL = 65025
# lower right pins with USB on top

RIGHT_FORWARD_PIN = 8
RIGHT_REVERSE_PIN = 9
LEFT_FORWARD_PIN = 11
LEFT_REVERSE_PIN = 10

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))


def spin_wheel(pwm):
        pwm.duty_u16(POWER_LEVEL)
        time.sleep(3)
        pwm.duty_u16(0)
        time.sleep(2)

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

# This allows us to stop the sound and motors when we do a Stop or Control-C which is a keyboard interrupt
try:
    main()
except KeyboardInterrupt:
    print('Got Control-c')
finally:
    print('shutting motors down')
    stop()
