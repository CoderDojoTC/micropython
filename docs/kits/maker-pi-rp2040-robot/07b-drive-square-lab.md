# Drive Square Lab

## Prerequsites

This lab assumes you have your Maker Pi RP2040 mounted on a SmartCar chassis with two motors and a battery hooked up.

In this lab we will program our robot to drive in a square pattern. We will start out doing a "bench test" that will require you to put the robot up on a block so you can see the wheels turn, but it will not drive off your desktop.  You can also observe the red LED lights on the many board to see which motor direction is on.

The main loop will look like this:

```py
while True:
    forward()
    sleep(FWD_TIME)
    
    stop()
    sleep(STOP_TIME)
    
    turn_right()
    sleep(TURN_TIME)
    
    stop()
    sleep(STOP_TIME)
```

We will need to adjust the TURN_TIME parameter to have the robot turn 90 degrees.  A good value for most robots is about 1/2 second or sleep(.5).

Since we will be calling the sleep function many times we will use the following import format to keep our code tidy:

```py
from utime import sleep
```
This says that whenever we want to pause our system we just use the ```sleep(time)``` function we mean to use the sleep function in the micropython time library.  This keeps our code small and portable.


## Adding a Keyboard Interrupt Handler (Control-C)

It is also a problem that when we stop a program running that the PWM circuits keep generating signals, which means the robot keeps moving even after we press the STOP/RESET button.  To clean this up we will allow you to run a special cleanup handler that will add a function to set all the motors to off using the ```stop()``` function.

```py
try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    stop()
```

## Full Program

You are now ready to test the full program.  Save the following to the main.py file, disconnect the USB connector and turn on the power on the main board.  Your robot should not we driving in a square!

```py
from machine import Pin, PWM
from utime import sleep

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

FWD_TIME = 2
TURN_TIME = .5 # adjust this to get the turn to be 90 degrees
STOP_TIME = 2

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

print('Running Drive Square Lab')
print('Use Control-C to Stop All Motors')

def main():
    while True:
        print('forward')
        forward()
        sleep(FWD_TIME)
        
        print('stop')
        stop()
        sleep(STOP_TIME)
        
        print('turning right')
        turn_right()
        sleep(TURN_TIME)
        
        print('stop')
        stop()
        sleep(STOP_TIME)
    
try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    stop()
```