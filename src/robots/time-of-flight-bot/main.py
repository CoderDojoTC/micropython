from machine import Pin, PWM
from utime import sleep
import VL53L0X

# used to blink the onboard LED
led_onboard = machine.Pin(25, machine.Pin.OUT)

# driving parameters
POWER_LEVEL = 40000 # use a value from 20000 to 65025
TURN_THRESHOLD = 400 # 25 cm
TURN_TIME = .25 # seconds of turning
BACKUP_TIME = .75 # seconds of backing up if obstacle deteced

# Motor pins to the L293 H-Bridge
RIGHT_FORWARD_PIN = 21
RIGHT_REVERSE_PIN = 20
LEFT_FORWARD_PIN = 18
LEFT_REVERSE_PIN = 19

# setup the PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)


    
def turn_motor_on(pwm):
   pwm.duty_u16(65025)

def turn_motor_off(pwm):
   pwm.duty_u16(0)

def forward():
    turn_motor_on(right_forward)
    turn_motor_on(left_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_reverse)

def reverse():
    turn_motor_on(right_reverse)
    turn_motor_on(left_reverse)
    turn_motor_off(right_forward)
    turn_motor_off(left_forward)

def turn_right():
    turn_motor_on(right_forward)
    turn_motor_on(left_reverse)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)

def turn_left():
    turn_motor_on(right_reverse)
    turn_motor_on(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)

def stop():
    turn_motor_off(right_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    turn_motor_off(left_reverse)

def read_sensor_avg():
    total = 0
    for i in range(10):
        total = total + tof.read()
        sleep(.01)
    return int(total/10)

tof.start() # startup the sensor

while True:
    dist = read_sensor_avg();
    print(dist)
    
    if dist < TURN_THRESHOLD:
        print('object detected')
        reverse()
        sleep(BACKUP_TIME)
        led_onboard.high()
        turn_right()
        sleep(TURN_TIME)
    else:
        if dist > 1300:
            print('no signal')
            led_onboard.low()
        else:
            print('Go forward')
            led_onboard.high()
        forward()

            
