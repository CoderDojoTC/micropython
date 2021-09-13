from machine import Pin, PWM
import time

POWER_LEVEL = 30000 # 65025
# lower right pins with USB on top
RIGHT_FORWARD_PIN =10
RIGHT_REVERSE_PIN =11
LEFT_FORWARD_PIN = 9
LEFT_REVERSE_PIN = 8

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
    print('right forward')
    spin_wheel(right_forward)

    print('right reverse')
    spin_wheel(right_reverse)

    print('left foward')
    spin_wheel(left_forward)

    print('left_reverse')
    spin_wheel(left_reverse)

print('Press CTRL-C to stop all motors.')

try:
    while True:
        main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    print('Turning all motors off.')
    stop()
