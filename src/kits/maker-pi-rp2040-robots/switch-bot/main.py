from machine import Pin, PWM
from time import sleep

# GPIO is the internal built-in LED
led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)

# input on the lower left of the Pico using a built-in pull-down resistor to keep the value from floating
middle_switch = Pin(7, Pin.IN, Pin.PULL_DOWN) 
right_switch = Pin(28, Pin.IN, Pin.PULL_DOWN)
left_switch = Pin(27, Pin.IN, Pin.PULL_DOWN)

POWER_LEVEL = 30000
RIGHT_FORWARD_PIN = 10
RIGHT_REVERSE_PIN = 11
LEFT_FORWARD_PIN = 9
LEFT_REVERSE_PIN = 8

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

def turn_motor_on(pwm):
   pwm.duty_u16(POWER_LEVEL)

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


def main():
    distance = ping()
    # skip over large numbers
    while distance > 100:
        distance = ping()
        update_display(distance, 'forward')
    print(distance)
    if distance < TURN_DISTANCE:
        print('Reverseing')
        reverse()
        sleep(BACKUP_TIME)
        stop()
        sleep(.5)
        print('Turning')
        if randint(0,2): # 50% chance of being true
           turn_right()
        else:
            turn_left()
        sleep(TURN_TIME)
        stop()
        sleep(.5)
    else:
        print('Forward')
        forward()
        sleep(.5)
        
    print("counter: ", counter)
    led_onboard.toggle()
    counter += 1
        

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('turning off sound')
    # sound_off()
    print('turning off motors')
    stop()