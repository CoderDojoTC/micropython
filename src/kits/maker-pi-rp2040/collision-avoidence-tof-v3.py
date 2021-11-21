# Collision Avoidance Demo for Cytron Maker Pi RP2040 board
# Version 3.0 with startup sounds and NeoPixel feedback

from machine import Pin,PWM
from utime import sleep
import random
import VL53L0X
from neopixel import Neopixel

# key parameters
POWER_LEVEL = 35000 # min is 20000 max is 65025
TURN_DISTANCE = 25 # distnce we decide to turn - try 20
REVERSE_TIME = .4 # how long we backup
TURN_TIME = .4 # how long we turn
MAX_DIST = 200

# The Piezo Buzzer is on GP22
buzzer=PWM(Pin(22))

# Motor Pins are A: 8,9 and B: 10,11
RIGHT_FORWARD_PIN = 11
RIGHT_REVERSE_PIN = 10
LEFT_FORWARD_PIN = 8
LEFT_REVERSE_PIN = 9

# our PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

NUMBER_PIXELS = 2
STATE_MACHINE = 0
NEOPIXEL_PIN = 18

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, NEOPIXEL_PIN, "GRB")
strip.brightness(100)

sda=machine.Pin(2) # lower right pin
scl=machine.Pin(3) # one up from lower right pin
i2c=machine.I2C(1, sda=sda, scl=scl, freq=400000)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)

red = (255, 0, 0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130) # purple?
purple = (75, 0, 130)
violet = (138, 43, 226) # mostly pink
cyan = (0, 255, 255)
lightgreen = (100, 255, 100)
white = (128, 128, 128) # not too bright
pink = (255, 128, 128)
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'cyan', 'lightgreen', 'white')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet, cyan, lightgreen, white, pink)

def turn_motor_on(pwm):
   pwm.duty_u16(POWER_LEVEL)

def turn_motor_off(pwm):
   pwm.duty_u16(0)

def forward():
    turn_motor_on(right_forward)
    turn_motor_on(left_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_reverse)
    strip.set_pixel(0, green)
    strip.set_pixel(1, green)
    strip.show()

def reverse():
    turn_motor_on(right_reverse)
    turn_motor_on(left_reverse)
    turn_motor_off(right_forward)
    turn_motor_off(left_forward)
    strip.set_pixel(0, purple)
    strip.set_pixel(1, purple)
    strip.show()

def turn_right():
    turn_motor_on(right_forward)
    turn_motor_on(left_reverse)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    strip.set_pixel(0, red)
    strip.set_pixel(1, red)
    strip.show()
    play_turn_right()
    
def turn_left():
    turn_motor_on(right_reverse)
    turn_motor_on(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)
    strip.set_pixel(0, blue)
    strip.set_pixel(1, blue)
    strip.show()
    play_turn_left()

def stop():
    turn_motor_off(right_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    turn_motor_off(left_reverse)
    strip.set_pixel(0, yellow)
    strip.set_pixel(1, yellow)
    strip.show()

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
blue_led_pins = [4,  5,  6,  7, 16, 17]
# dist_scale =    [2, 4, 6, 8, 10, 13, 16, 20, 25, 35, 50, 75, 100]
dist_scale =    [4, 8, 16, 24, 50]

number_leds = len(blue_led_pins)
distance_per_led = (MAX_DIST - TURN_DISTANCE) / number_leds
led_ports = []
# time for each LED to display
delay = .05

# time of flight calibration parameters
zero_dist = 65 # distance measure when an object is about 1/2 cm away
max_dist = 350 # max distance we are able to read
scale_factor = .2

# create a list of the ports
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

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

def led_show_dist(in_distance):
    global number_leds, distance_per_led 
    for led_index in range(0, number_leds):
        val = TURN_DISTANCE + led_index * distance_per_led
        if in_distance > val:
            led_ports[led_index].high()
        else:
            led_ports[led_index].low()

LED_DELAY = .08
def run_lights():
    for i in range(0, number_leds):
        led_ports[i].high()
        strip.set_pixel(0, colors[i])
        strip.set_pixel(1, colors[i])
        strip.show()
        sleep(LED_DELAY)
        led_ports[i].low()
    # blue down
    for i in range(number_leds - 1, 0, -1):
        led_ports[i].high()
        strip.set_pixel(0, colors[i])
        strip.set_pixel(1, colors[i])
        strip.show()
        sleep(LED_DELAY)
        led_ports[i].low()
# start our time-of-flight sensor

# loop forever
def main():
    global valid_distance
    while True:  
        distance = get_distance()
        if distance > MAX_DIST:
            # only print if we used to have a valid distance
            if valid_distance == 1:
                print('no signal')
                play_no_signal()
            valid_distance = 0
        # we have a valid distance
        else:
            print(distance)
            if distance < TURN_DISTANCE:    
                # back up for a bit
                reverse()
                sleep(REVERSE_TIME)
                # turn in a random direction
                if random.random() > .5:
                    print('turning right')
                    turn_right()
                else:
                    print('turning left')
                    turn_left()
                sleep(TURN_TIME)
                # continue going forward
                forward()
            else:
                print('forward')
                forward()
            valid_distance = 1
            led_show_dist(distance)
        sleep(0.05)

# startup
run_lights()
tof.start()
play_startup()
valid_distance = 1

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
    tof.stop()
