# Maker Pi RP2040 program to check the limits of a 180 degree servo such as a SG90 micro servo
from machine import Pin, PWM
import time

BUTTON_1_PIN = 20 # increment the angle
BUTTON_2_PIN = 21 # decrement the angle

SERVO_1_PIN = 12
SERVO_2_PIN = 13 # MAX=5749@40
SERVO_3_PIN = 14
SERVO_4_PIN = 15
SERVO_MIN_DUTY = 1725
SERVO_MAX_DUTY = 6378
# this is ususlly standard across most servos
SERVO_FREQ_HZ = 40

pwm = PWM(Pin(SERVO_2_PIN))

# the two button on the Maker Pi RP2040
increment_angle_button_pin = machine.Pin(BUTTON_1_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
decrement_angle_button_pin = machine.Pin(BUTTON_2_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This will take in integers of range in (min and max) return a integer in the output range (min and max)
# Used to convert one range of values into another using a linear function like the Arduino map() function
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# globals
angle = -90 # change this to be 90 to test the other end
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
print('Press the GP20 and GP21 buttons on the Maker Pi RP2040 to verify the -90 and 90 angles are correct.')
print('Adjust the SERVO_MIN_DUTY and SERVO_MAX_DUTY values accordingly.')
while True:
    # only print on change in the button_presses value
    if angle != old_angle:
        duty = ServoDuty(angle)
        print('new angle:', angle, 'duty: ', duty)
        pwm.duty_u16(duty)
        old_angle = angle

