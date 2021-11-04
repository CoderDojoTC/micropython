from machine import Pin, PWM
import time

POWER_LEVEL = 65025
# lower right pins with USB on top
RIGHT_FORWARD_PIN = 10
RIGHT_REVERSE_PIN = 11
LEFT_FORWARD_PIN = 9
LEFT_REVERSE_PIN = 8

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

def spin_wheel(pwm):
        pwm.duty_u16(POWER_LEVEL)
        time.sleep(2)
        pwm.duty_u16(0)
        time.sleep(1)

while True:
    print('right forward')
    spin_wheel(right_forward)

    print('right reverse')
    spin_wheel(right_reverse)

    print('left foward')
    spin_wheel(left_forward)

    print('left_reverse')
    spin_wheel(left_reverse)