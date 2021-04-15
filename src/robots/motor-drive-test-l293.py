from machine import Pin, PWM
from time import sleep

# lower right pins with USB on top
RIGHT_FORWARD_PIN = 17
RIGHT_REVERSE_PIN = 16
LEFT_FORWARD_PIN = 18
LEFT_REVERSE_PIN = 19

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

# while True:
def spin_wheel(pwm):
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0002)
    sleep(1)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0002)
    sleep(.5)

print('right forward')
spin_wheel(right_forward)
print('right reverse')
spin_wheel(right_reverse)
print('left foward')
spin_wheel(left_forward)
print('left_reverse')

spin_wheel(left_reverse)