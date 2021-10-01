from machine import Pin, PWM
from rotary import Rotary
from utime import sleep, sleep_us, ticks_ms, ticks_us
import ssd1306

# Initial Robot Performance Parameters
MOTOR_POWER = 30000
TURN_DIST = 20 # distance to reverse and turn in cm
REV_TIME = .5 # time to spend in reverse
TURN_TIME = .5 # time we spend turning
TURN_MODE = 2 #random turn left and right
MAX_DIST = 200 # cm

# adjustable parameter globals
motor_power = MOTOR_POWER
turn_dist  = TURN_DIST
rev_time = REV_TIME
turn_time = TURN_TIME
turn_mode = TURN_MODE

# static pin assignments - change these if you rewire the robot
TRIGGER_PIN = 7
ECHO_PIN = 6
# row 12 on left
SPEAKER_PIN = 9
# lower right on pico
ROTARY_A_PIN = 16
ROTARY_B_PIN = 17
ROTARY_BUTTON_PIN = 22
# lower left on pico
UP_BUTTON_PIN = 14
DOWN_BUTTON_PIN = 15
# motor pins
RIGHT_FORWARD_PIN = 21
RIGHT_REVERSE_PIN = 20
LEFT_FORWARD_PIN = 18
LEFT_REVERSE_PIN = 19

# motor PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

# Init HC-SR04 pins
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back
# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

WIDTH = 128
HEIGHT = 64
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0,sck=clock, mosi=data)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

rotary = Rotary(ROTARY_A_PIN, ROTARY_B_PIN, ROTARY_BUTTON_PIN)

# our globals
mode = 0 # the program mode
mode_function = 0 # the function to change within a mode
function_value = 0 # the function value (usually a value of 0-to-5)
dist = 0


# setup the IRQ objects
up_irq = machine.Pin(UP_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
down_irq = machine.Pin(DOWN_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

# for the display programming menu options
mode_menu = ['Standby', 'Run', 'Program', 'Test Motors', 'Status']
mode_count = len(mode_menu)
# the programming parameters
function_menu = ['Motor Power', 'Turn Dist', 'Rev. Time', 'Turn Time', 'Turn Direction']
function_count = len(function_menu)
motor_power_labels = ['low', 'medium-low', 'medium', 'fast', 'max']
motor_power_values = [20000, 25000, 30000, 35000, 40000, 50000, 65025]
turn_dist_values = [5, 10, 15, 20, 35, 30, 35, 40, 50]
reverse_time_values = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0, 1.2]
turn_time_values = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0, 1.2]
turn_direction_labels = ['left', 'right', 'random']

def ping():
    trigger.low()
    sleep_us(2) # Wait 2 microseconds low
    trigger.high()
    sleep_us(5) # Stay high for 5 miroseconds
    trigger.low()
    while echo.value() == 0:
        signaloff = ticks_us()
    while echo.value() == 1:
        signalon = ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return int(distance)

# note these are reversed since we have the middle pin on 3.3v
#change == Rotary.ROT_CW:
#change == Rotary.ROT_CCW:
def rotary_changed(change):
    global mode, mode_function
    if change == Rotary.SW_PRESS:
        mode += 1
        mode_function = 0
    if change == Rotary.ROT_CW:
        mode_function +=1
    elif change == Rotary.ROT_CCW:
        mode_function -= 1
    # wrap the mode and mode function
    if mode > mode_count - 1:
        mode = 0
    if mode_function > 5:
        mode_function = 0
    if mode_function < 0:
        mode_function = 5
        
rotary.add_handler(rotary_changed)

last_time = 0
# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global function_value, last_time
    new_time = ticks_ms()
    # print(pin)
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        if '14' in str(pin):
            function_value +=1
        else:
            function_value -=1
        last_time = new_time
# now we register the handler function when the button is pressed
up_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
down_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)


def update_display():
    global mode, dist, motor_power, backup_delay, turn_delay
    oled.fill(0)
    oled.text('Mode:', 0, 0, 1)
    oled.text(mode_menu[mode], 40, 0, 1)
    if mode == 0:
        oled.text(str(mode), 120, 0, 1)
        oled.text('Press Knob', 10, 10, 1)
        oled.text('To Start', 10, 20, 1)
    if mode == 2: # program mode
        oled.text('Funct:', 0, 10, 1)
        oled.text(function_menu[mode_function], 10, 20, 1)
        oled.text('Val:', 0, 30, 1)
        oled.text(str(function_value), 40, 30, 1)
    # do not show on PROG mode
    if (mode != 2):
        oled.text('Dist: ', 0, 40, 1)
        oled.text(str(dist), 50, 40, 1)
        oled.text('Counter: ', 0, 50, 1)
        oled.text(str(counter), 70, 50, 1)
    oled.show()

def sound_off():
    speaker.duty_u16(0)
    
def playtone(frequency):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    
def playnote(frequency, duration):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    sleep(duration)
    sound_off()
    
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

print('Collision Avoidance Display Rotary Ping Adjustable Robot with Speaker V1')
play_startup()

counter = 0
# 1 if there is no signal

def main():
    global counter, dist
    no_signal_status = 0
    last_no_signal_status = 0
    current_mode = mode
    current_mode_function = mode_function
    current_function_value = function_value
    while True:
        dist = ping()
        if dist > MAX_DIST:
            no_signal_status = 1
        update_display()
        
        if no_signal_status != last_no_signal_status:
            print('No signal status:', no_signal_status)
            last_no_signal_status = no_signal_status
        # only print on change
        if current_mode != mode:
            print('mode:', mode)
            current_mode = mode
        if current_mode_function != mode_function:
            print('mode function:', mode_function)
            current_mode_function = mode_function
        sleep(0.2)
        counter += 1

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('cleaning up')