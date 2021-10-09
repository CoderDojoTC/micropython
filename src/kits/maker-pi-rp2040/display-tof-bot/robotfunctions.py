from machine import Pin,PWM
from neopixel import Neopixel
from utime import sleep, ticks_ms

# The Piezo Buzzer is on GP22
BUZZER_PIN = 22
buzzer=PWM(Pin(BUZZER_PIN))

# Motor Pins are A: 8,9 and B: 10,11
RIGHT_FORWARD_PIN =10
RIGHT_REVERSE_PIN =11
LEFT_FORWARD_PIN  = 9
LEFT_REVERSE_PIN  = 8

# our PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

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

NUMBER_PIXELS = 2
STATE_MACHINE = 0
NEOPIXEL_PIN = 18
# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, NEOPIXEL_PIN, "GRB")
strip.brightness(100)

def turn_motor_on(pwm, motor_power):
    pwm.duty_u16(motor_power)

def turn_motor_off(pwm):
   pwm.duty_u16(0)

def forward(motor_power):
    turn_motor_on(right_forward, motor_power)
    turn_motor_on(left_forward, motor_power)
    turn_motor_off(right_reverse)
    turn_motor_off(left_reverse)
    strip.set_pixel(0, green)
    strip.set_pixel(1, green)
    strip.show()

def drive_reverse(motor_power):
    turn_motor_on(right_reverse, motor_power)
    turn_motor_on(left_reverse, motor_power)
    turn_motor_off(right_forward)
    turn_motor_off(left_forward)
    strip.set_pixel(0, purple)
    strip.set_pixel(1, purple)
    strip.show()

def turn_right(motor_power):
    turn_motor_on(right_forward, motor_power)
    turn_motor_on(left_reverse, motor_power)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    strip.set_pixel(0, red)
    strip.set_pixel(1, red)
    strip.show()
    play_turn_right()
    
def turn_left(motor_power):
    turn_motor_on(right_reverse, motor_power)
    turn_motor_on(left_forward, motor_power)
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