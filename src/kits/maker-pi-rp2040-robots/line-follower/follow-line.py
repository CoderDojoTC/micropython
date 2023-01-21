from machine import Pin, PWM
from time import sleep

# sensor setup
RIGHT_SENSOR_PIN = 2
LEFT_SENSOR_PIN = 4

right_sensor = Pin(RIGHT_SENSOR_PIN)
left_sensor = Pin(LEFT_SENSOR_PIN)

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
BOOST_LEVEL = 5000

# while True:
def spin_wheel(pwm):
    pwm.duty_u16(SLOW_DRIVE_POWER)
    sleep(2)
    pwm.duty_u16(0)
    sleep(1)

def forward():
    right_forward.duty_u16(SLOW_DRIVE_POWER)
    right_reverse.duty_u16(0)
    left_forward.duty_u16(SLOW_DRIVE_POWER)
    left_reverse.duty_u16(0)

def right():
    right_forward.duty_u16(SLOW_DRIVE_POWER)
    right_reverse.duty_u16(0)
    left_forward.duty_u16(SLOW_DRIVE_POWER+BOOST_LEVEL)
    left_reverse.duty_u16(0)

def left():
    right_forward.duty_u16(SLOW_DRIVE_POWER+BOOST_LEVEL)
    right_reverse.duty_u16(0)
    left_forward.duty_u16(SLOW_DRIVE_POWER)
    left_reverse.duty_u16(0)

def stop():
    right_forward.duty_u16(0)
    right_reverse.duty_u16(0)
    left_forward.duty_u16(0)
    left_reverse.duty_u16(0)    
    
def main():
    while True:
        r = right_sensor.value()
        l = left_sensor.value()
        if r == 0 and l == 1:
            print("right over white - turning left")
            left()
        if l == 0:
            print("left over white")
            right()
        else:
            forward()
            
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
