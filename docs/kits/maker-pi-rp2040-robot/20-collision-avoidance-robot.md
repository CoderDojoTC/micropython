# Maker Pi RP2040 Collision Avoidance Robot

This robot works very similar to our standard CoderDojo Collision Avoidance Robot but all the pins are now configured to use the connections on the Maker Pi RP2040 board.

The board is mounted on a SmartCar Chassis and Grove Connector 0 is used to connect to a Time-of-Flight distance sensor that is using the I2C bus.

## Random Turn Direction

```py
if dist < TURN_DIST:
    play_reverse()
    reverse()
    sleep(REVERSE_TIME)
    # half right and half left turns
    if urandom.random() < .5:
        turn_right()
        play_turn_right()
    else:
        turn_left()
        play_turn_left()
    sleep(TURN_TIME)
    forward()
```


```py
# Demo for Maker Pi RP2040 board

from machine import Pin,PWM
from time import sleep, sleep_ms
import urandom
import VL53L0X

# Piezo Buzzer is on GP22
buzzer=PWM(Pin(22))

# this is the max power level
POWER_LEVEL = 65025

# Motor Pins are A: 8,9 and B: 10,11
RIGHT_FORWARD_PIN = 8
RIGHT_REVERSE_PIN = 9
LEFT_FORWARD_PIN = 11
LEFT_REVERSE_PIN = 10

# our PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))


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

# Time of flight sensor is on the I2C bus on Grove connector 0
sda=machine.Pin(0) # row one on our standard Pico breadboard
scl=machine.Pin(1) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
# print("Device found at decimal", i2c.scan())

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs
blue_led_pins = [2, 3,  4,  5,  6,  7, 16, 17, 26, 27, 28]
# dist_scale =    [2, 4, 6, 8, 10, 13, 16, 20, 25, 35, 50, 75, 100]
dist_scale =    [2, 4, 6, 8, 10, 15, 20, 25, 50, 100, 150, 200, 300]

number_leds = len(blue_led_pins)
led_ports = []
delay = .05

# calibration parameters
zero_dist = 65 # distance measure when an object is about 1/2 cm away
max_dist = 350 # max distance we are able to read
scale_factor = .2

# create a list of the ports
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

# blue up
for i in range(0, number_leds):
    led_ports[i].high()
    time.sleep(delay)
    led_ports[i].low()
# blue down
for i in range(number_leds - 1, 0, -1):
    led_ports[i].high()
    time.sleep(delay)
    led_ports[i].low()

# get the normalized time-of-flight distance
def get_distance():
    global zero_dist, scale_factor
    tof_distance = tof.read()
    if tof_distance > max_dist:
        return tof_distance
    # if our current time-of-flight distance is lower than our zero distance then reset the zero distance
    if tof_distance < zero_dist:
        zero_dist = tof_distance
    return  int((tof_distance - zero_dist) * scale_factor)

def led_show_dist(in_distance):
    global number_leds
    for led_index in range(0, number_leds):
        if in_distance > dist_scale[led_index]:
            led_ports[led_index].high()
        else:
            led_ports[led_index].low()

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
    
def play_no_signal():
    playtone(100)
    time.sleep(0.1)
    bequiet()

def play_turn():
    playtone(500)
    sleep(0.1)
    bequiet()
    
# start our time-of-flight sensor
tof.start()
valid_distance = 1

# loop forever
def main():
    global valid_distance
    while True:  
        distance = get_distance()
        if distance > 1000:
            # only print if we used to have a valid distance
            if valid_distance == 1:
                print('no signal')      
            valid_distance = 0
        else:
            print(distance)
            if distance < 30:
                play_turn()
                # back up for 1/2 second
                reverse()
                sleep(0.5)
                turn_right()
                sleep(0.75)
                forward()
            else:
                print('forward')
                forward()
            valid_distance = 1
            led_show_dist(distance)
        sleep(0.05)

# clean up


# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrup
try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('turning off sound')
    buzzer.duty_u16(0)
    print('powering down all motors')
    stop()
    print('stopping time of flight sensor')
    tof.stop()
```