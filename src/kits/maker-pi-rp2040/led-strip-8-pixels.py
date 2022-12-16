# Collision Avoidance Demo for Cytron Maker Pi RP2040 board
# Version 3.0 with startup sounds and NeoPixel feedback

from machine import Pin,PWM
from utime import sleep
import random
import VL53L0X
from neopixel import NeoPixel


# key parameters
POWER_LEVEL = 35000 # min is 20000 max is 65025
TURN_DISTANCE = 20 # distnce we decide to turn - try 20
REVERSE_TIME = .6 # how long we backup
TURN_TIME = .5 # how long we turn
MAX_DIST = 500 # max ToF sensor value that is reasonable without error

# The Piezo Buzzer is on GP22
buzzer=PWM(Pin(22))

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

NEOPIXEL_PIN = 2
NUMBER_PIXELS = 8
PERCENT_COLOR_WHEEL = round(255/NUMBER_PIXELS)

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Grove Connector 1
sda=machine.Pin(0) # white Grove wire
scl=machine.Pin(1) # yellow Grove wire
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_RED = (15, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 25, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 0, 25)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (10, 10, 10)
OFF = (0, 0, 0)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)
num_colors = len(COLORS)

# color wheel
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def draw_idle(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    for i in range(0, NUMBER_PIXELS):
        color_index = round(i*PERCENT_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        strip[(i + counter) % NUMBER_PIXELS] = color
        strip.write()
    sleep(wait)

def draw_forward(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    for i in range(0, NUMBER_PIXELS):
        if i == NUMBER_PIXELS - pixel_index - 1:
            strip[i] = LIGHT_GRAY
        else:
            strip[i] = OFF
    strip.write()
    sleep(wait)

def draw_reverse(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    for i in range(0, NUMBER_PIXELS):
        if i == pixel_index:
            strip[i] = LIGHT_BLUE
        else:
            strip[i] = OFF
    strip.write()
    sleep(wait)
    
def draw_right(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    if counter % 2:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = LIGHT_RED
    else:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = OFF
    strip.write()
    sleep(wait)

def draw_left(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    if counter % 2:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = LIGHT_GREEN
    else:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = OFF
    strip.write()
    sleep(wait)

def draw_all_off():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = OFF
    strip.write()

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

def sound_off():
    buzzer.duty_u16(0)
    
# play a frequence for a given time and go off
def playnote(frequency, time):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
    # time.sleep(time)
    sleep(0.1)
    sound_off() # always turn off sound after note
    
def play_no_signal():
    playnote(100, 0.1)

def play_turn():
    playnote(500, .1)
 
def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
   
def rest(time):
    sound_off()
    sleep(time)
    
def play_startup():
    playnote(600, 0.2)
    rest(0.05)
    playnote(600, 0.2)
    rest(.05)
    playnote(600, 0.2)
    rest(0.1)
    playnote(800, 0.4)
    
def play_no_signal():
    playnote(300, 0.1)

def play_turn_right():
    playnote(500, 0.1)
    
def play_turn_left():
    playnote(700, 0.1)

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs
# remove 0, 1, 2 and 3 for the I2C busees and remove 26,27 and 28 for the pots
#blue_led_pins = [4,  5,  6,  7, 16, 17]
# dist_scale =    [2, 4, 6, 8, 10, 13, 16, 20, 25, 35, 50, 75, 100]
#dist_scale =    [4, 8, 16, 24, 50]

#number_leds = len(blue_led_pins)
#distance_per_led = (MAX_DIST - TURN_DISTANCE) / number_leds
#led_ports = []
# time for each LED to display
delay = .05

# time of flight calibration parameters
zero_dist = 50 # distance measure when an object is about 1/2 cm away
max_dist = 100 # max distance we are able to read
scale_factor = .2

# create a list of the ports
#for i in range(number_leds):
#   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

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

# map the value from old to new range like the arduino map(x, inmin, inmax, outmin, outmax)
def valmap(value, istart, istop, ostart, ostop):
    denominator = istop - istart
    if denominator == 0:
        return ostop
    else:
      return int(ostart + (ostop - ostart) * ((value - istart) / denominator))

LED_DELAY = .08

min_dist = 5
max_dist = 255

# global variables
counter = 0
state = 0
old_state = 1

# loop forever
def main():
    global counter, state, old_state
    while True:  
        distance = get_distance()
        # print(distance)
        
        # wait hear until we get a valid distance
        if distance > MAX_DIST:
            if state != old_state:
                print('distance > ', MAX_DIST)
                old_state = state
                draw_idle(counter, .1)
                counter += 1
            else:
                state = 1
        # we have a valid distance
        else:
            # print(distance)
            if distance < TURN_DISTANCE:    
                # back up for a bit
                reverse()
                reverse_cycles = round(REVERSE_TIME / .1)
                for i in range(0, reverse_cycles):
                    draw_reverse(counter, .1)
                    counter += 1

                # turn in a random direction
                turn_direction = random.random()
                if turn_direction > .5:
                    print('turning right')
                    turn_right()
                else:
                    print('turning left')
                    turn_left()
                turn_cycles = round(REVERSE_TIME / .1)
                for i in range(0, turn_cycles):
                    if turn_direction > .5:
                        draw_right(counter, .1)
                    else:
                        draw_left(counter, .1)
                    counter += 1
                # now continue going forward
                forward()
                draw_forward(counter, .01)
                counter += 1
            else:
                print('forward')
                forward()
                draw_forward(counter, .01)
                counter += 1

# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrupt
print('Running Collision Avoidence with Time-of-Flight Sensor Version 3.0')

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('turning off sound')
    sound_off()
    print('turning off motors')
    stop()
    # turn off the LEDs
    draw_all_off()
    tof.stop()
