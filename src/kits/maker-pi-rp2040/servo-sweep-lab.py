from machine import Pin, PWM
import time

BUTTON_1_PIN = 20
BUTTON_2_PIN = 21

SERVO_1_PIN = 12
SERVO_2_PIN = 13
SERVO_3_PIN = 14
SERVO_4_PIN = 15
SERVO_FREQ_HZ = 50
SERVO_MIN_DUTY = 1500
SERVO_MAX_DUTY = 7200
# this is ususlly standard across most servos
SERVO_FREQ_HZ = 40
DELAY = 0.05 # delay to give the servo time to moce
STEP = 5 # number of steps between angles

pwm = PWM(Pin(SERVO_1_PIN))

# globals
angle = 0

# Thisw will take in integers of range in (min and max) return a integer in the output range (min and max)
# Used to convert one range of values into another using a linear function like the Arduino map() function
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

old_angle = -1

pwm.freq(50)
while True:
    for angle in range(-90, 90, STEP):
        duty = convert(angle, -90, 90, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
        print('angle:', angle, 'duty: ', duty)
        pwm.duty_u16(duty)
        old_angle = angle
        time.sleep(DELAY)
    for angle in range(90, -90, -STEP):
        duty = convert(angle, -90, 90, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
        print('angle:', angle, 'duty: ', duty)
        pwm.duty_u16(duty)
        old_angle = angle
        time.sleep(DELAY)
