# Maker Pi RP2040 Servo Lab

Servo motors are ideal for controlling the angle of an item such as a steering angle or the direction of a sensor.  The servos used in these labs are inexpensive SG90 micro-servos that draw very little power and are ideal for a teaching lab.  They can be purchased for about [$3 each US on eBay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=SG90+micro+servos&_sacat=0&rt=nc&LH_BIN=1).  To control a 180 degree servo, you just tell it what angle you would like it to move to.  The range of values is typically -90 to 90 degrees with 0 being the nominal resting position for many applications such as the steering wheel angle of a car.

The Maker Pi RP2040 has four servo ports in the upper left corner of the board (with the USB on the bottom) that use ports GP12, GP13, GP14 and GP15.  You can connect any small micro servo directly to these ports.  Just make sure to get the polarity correct.  The colors for servos may vary somewhat, but the two most common standards are:

* Orange, red and brown - signal, positive and ground
* White, red, black - signal, positive and ground

The general rule is that the lighter colors of orange and white will be the signal and the brown and black will be ground.

## Servo Control

We will use the PWM functions in our MicroPython library to send a PWM signal to each of the servos.  Servos are not controlled by the duty cycle directly.  They are controlled by the width of the pulses.  But we can control the approximate with of the pulses by holding the frequency constant and changing the duty cycle.

We will use a 40 hertz signal to send a PWM signal to each of the servos like this.

```py
SERVO_FREQ_HZ = 40
# SERVO_PERIOD_MS = 1000 / SERVO_FREQ_HZ is a 25 millisecond pulse width
my_pwm.freq(SERVO_FREQ_HZ)
```


## Calibration of the Servo
There are small manufacturing variations in servos.  This means to get the full sweep of a 180% servo you have to adjust the duty cycle.

* Minimum duty cycle: 1700
* Maximum duty cycle: 6300

By some experimentation I got the following results
```py
SERVO_MIN_DUTY = 1725 # -90 degrees
SERVO_MAX_DUTY = 6378 # 90 degrees
```

We can use a linear mapping function to convert the angle (from -90 to 90):

```py
# This will take in integers of range in (min and max) return a integer in the output range (min and max)
# Used to convert one range of values into another using a linear function like the Arduino map() function
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

angle = 0
duty = convert(angle, -90, 90, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
print('For angle: ', angle, ' the duty is: ', duty)
pwm.duty_u16(duty)
```

## Checking your Servo Calibration with Buttons
We can also use the buttons on the Maker Pi RP2040 to verify that the extreme angles are correct.  One button will increase the angle and one will decrease the angle.

```py
# Maker Pi RP2040 program to check the limits of a 180 degree servo such as a SG90 micro servo
from machine import Pin, PWM
import time

BUTTON_1_PIN = 20 # increment the angle
BUTTON_2_PIN = 21 # decrement the angle

SERVO_1_PIN = 12
SERVO_2_PIN = 13 # MAX=5749@40
SERVO_3_PIN = 14
SERVO_4_PIN = 15
# this is ususlly standard across most servos
SERVO_FREQ_HZ = 40

pwm = PWM(Pin(SERVO_2_PIN))

# the two button on the Maker Pi RP2040
increment_angle_button_pin = machine.Pin(BUTTON_1_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
decrement_angle_button_pin = machine.Pin(BUTTON_2_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

     
#  return int( ( (0.0015*SERVO_FREQ_HZ) + ((angle/90) * (0.0005*SERVO_FREQ_HZ)) ) * 65535 )
# This will take in integers of range in (min and max) return a integer in the output range (min and max)
# Used to convert one range of values into another using a linear function like the Arduino map() function
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# globals
angle = -90
last_time = 0 # the last time we pressed the button

# if the pin is 20 then increment, else decement
def button_pressed_handler(pin):
    global angle, last_time
    new_time = time.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in str(pin):
            angle +=1
        else:
            angle -=1
        last_time = new_time
 # now we register the handler function when the button is pressed
increment_angle_button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
decrement_angle_button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

pwm.freq(SERVO_FREQ_HZ)
old_angle = -1

while True:
    # only print on change in the button_presses value
    if angle != old_angle:
        duty = ServoDuty(angle)
        print('new angle:', angle, 'duty: ', duty)
        pwm.duty_u16(duty)
        old_angle = angle
```

## Sample Sweep Code

```py
from machine import Pin, PWM
import time

BUTTON_1_PIN = 20
BUTTON_2_PIN = 21

SERVO_1_PIN = 12
SERVO_2_PIN = 13
SERVO_3_PIN = 14
SERVO_4_PIN = 15
SERVO_FREQ_HZ = 50
SERVO_MIN_DUTY = 1725
SERVO_MAX_DUTY = 6378
# this is ususlly standard across most servos
SERVO_FREQ_HZ = 40

pwm = PWM(Pin(SERVO_2_PIN))

# the two button on the Maker Pi RP2040
clock_button_pin = machine.Pin(BUTTON_1_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
counter_clock_button_pin = machine.Pin(BUTTON_2_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

# globals
angle = 90
last_time = 0 # the last time we pressed the button

def button_pressed_handler(pin):
    global angle, last_time
    new_time = time.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in str(pin):
            angle +=1
        else:
            angle -=1
        # wrap around to first mode
        if mode >= mode_count: mode = 0
        if mode < 0: mode = mode_count - 1
        last_time = new_time
        
# now we register the handler function when the button is pressed
clock_button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
counter_clock_button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)      
#  return int( ( (0.0015*SERVO_FREQ_HZ) + ((angle/90) * (0.0005*SERVO_FREQ_HZ)) ) * 65535 )

# Thisw will take in integers of range in (min and max) return a integer in the output range (min and max)
# Used to convert one range of values into another using a linear function like the Arduino map() function
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# -90 should generate 1725
# 90 should generate 7973

old_angle = -1

pwm.freq(50)
while True:
    for angle in range(-90, 90):
        duty = convert(angle, -90, 90, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
        print('angle:', angle, 'duty: ', duty)
        pwm.duty_u16(duty)
        old_angle = angle
        time.sleep(.01)
    for angle in range(90, -90, -1):
        duty = convert(angle, -90, 90, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
        print('angle:', angle, 'duty: ', duty)
        pwm.duty_u16(duty)
        old_angle = angle
        time.sleep(.01)
```

## Shutting Down All Servos

```py
from machine import Pin, PWM
import time

SERVO_1_PIN = 12
SERVO_2_PIN = 13
SERVO_3_PIN = 14
SERVO_4_PIN = 15

print('shutting down all servos!')
for i in range(12, 16):
    print('Servo', i, 'shutting down')
    pwm1 = PWM(Pin(SERVO_1_PIN))
    pwm1.duty_u16(0)
```

## Adding Cleanup Code

PWM signals continue to be generated even after you do a STOP/RESET on your microcontroller.  This could drain batteries and wear out your servo motors.  To stop the servos from getting PWM signals you can add an interrupt to your code to catch these signals and set the PWM duty cycle back to zero. This

```py

```

## References

[MicroPython Reference Page](https://docs.micropython.org/en/latest/pyboard/tutorial/servo.html) - this page is not very helpful.  The implication is that servo controls are standardized across MicroPython system.  This does not appear to be the case.