from machine import Pin, PWM
from rotary import Rotary
from utime import sleep, sleep_us, ticks_us, ticks_ms
import urandom
import ssd1306

# The Default Parameters
TURN_DIST = 15
MOTOR_POWER = 30000
REVERSE_TIME = .5
TURN_TIME = .5

# ignore any ping measurements above this number
MAX_DIST = 200
POWER_POWER_LEVEL = 65025

# static pin assignments
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

# Motor Pins
RIGHT_FORWARD_PIN = 21
RIGHT_REVERSE_PIN = 20
LEFT_FORWARD_PIN = 18
LEFT_REVERSE_PIN = 19

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
motor_power = MOTOR_POWER
motor_power_val = 2
turn_dist = TURN_DIST
turn_dist_val = 3
reverse_time = REVERSE_TIME
reverse_time_val = 3
turn_time = TURN_TIME
turn_time_val = 3

mode_menu = ['Standby', 'Run', 'Program', 'Test Motors', 'Status']
mode_count = len(mode_menu)
functions_menu = ['Motor Power', 'Turn Dist', 'Rev Time', 'Turn Time']
function_menu_count = len(functions_menu)
# power
power_level_labels = ['Off', 'Low', 'Medium-Low', 'Medium', 'Medium-High', 'High', 'Max']
power_level_values = [0,      20000, 30000,        40000,   50000,         55000,  POWER_POWER_LEVEL]
power_level_count = len(power_level_labels)
# turn distance
turn_dist_labels = ['5cm', '7cm', '10cm', '15cm', '20cm', '30cm', '40cm']
turn_dist_values = [5, 7, 10, 15, 20, 30, 40]
turn_dist_count = len(turn_dist_labels)
# rev time
reverse_time_labels = ['.2 sec', '.3 sec', '.4 sec', '.5 sec', '.6 sec', '.7 sec', '.8 sec', '.9 sec', '1 sec']
reverse_time_values = [.2, .3, .4, .5, .6, .7, .8, .9, 1]
reverse_time_count = len(reverse_time_labels)
# turn time
turn_time_labels = ['.2 sec', '.3 sec', '.4 sec', '.5 sec', '.6 sec', '.7 sec', '.8 sec', '.9 sec', '1 sec']
turn_time_values = [.2, .3, .4, .5, .6, .7, .8, .9, 1]
turn_time_count = len(turn_time_labels)

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
    global mode, mode_function, function_menu_count
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
    if mode_function > function_menu_count - 1:
        mode_function = function_menu_count - 1
    if mode_function < 0:
        mode_function = 0
        
rotary.add_handler(rotary_changed)

# the lower right coner has a wire that goes throuh 3.3v
up_irq = machine.Pin(UP_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
down_irq = machine.Pin(DOWN_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
last_time = 0
def button_pressed_handler(pin):
    global mode_function, function_value, last_time, power_level_count, turn_dist_count, reverse_time_count, turn_time_count
    new_time = ticks_ms()
    # print(pin)
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        if '14' in str(pin):
            function_value +=1
        else:
            function_value -=1
        # keep the function values at 0 or above
        if function_value < 0:
            function_value = 0
        # wrap the function values
        if mode_function == 0:
            if function_value >= power_level_count - 1:
                function_value =  power_level_count - 1
            power_level = power_level_values[function_value]
        elif mode_function == 1:
            if function_value >= turn_dist_count - 1:
                function_value = turn_dist_count - 1
            turn_dist = turn_dist_values[function_value]
        elif mode_function == 2:
            if function_value >= reverse_time_count - 1:
                function_value = reverse_time_count - 1
            reverse_time = reverse_time_values[function_value]
        elif mode_function == 3:
            if function_value >= turn_time_count - 1:
                function_value = turn_time_count - 1
            turn_time = turn_time_values[function_value]
        last_time = new_time

# now we register the handler function when the button is pressed
up_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
down_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

def update_display():
    global mode, dist, motor_power, backup_delay, turn_dist, turn_delay
    oled.fill(0)
    
    # draw current mode in reverse in top 10 rows
    oled.fill_rect(0, 0, WIDTH, 10, 1)
    oled.text('Mode:', 0, 2, 0)
    oled.text(mode_menu[mode], 40, 1, 0)
    
    # standby mode
    if mode == 0:
        oled.text(str(mode), 120, 0, 1)
        oled.text('Press Knob', 10, 10, 1)
        oled.text('To Start', 10, 20, 1)
        
    # display distance and action in standby and run modes
    if mode == 0 or mode == 1:
        oled.text('Dist: ', 0, 30, 1)
        oled.text(str(dist), 50, 30, 1)
        oled.text('Action:', 0, 40, 1)
        if dist < TURN_DIST:
            oled.text('Turning', 55, 40, 1)
        else:
            oled.text('Forward', 55, 40, 1)
            
    # program mode
    if mode == 2:
        oled.text('Par: ', 0, 20, 1)
        oled.text(functions_menu[mode_function], 30, 20, 1)
        
        # display the modes function labels and values
        oled.text('Val: ', 0, 30, 1)
        # for each mode function like "Power Level" we use a different list of label/value pairs
        if mode_function == 0:
            oled.text(power_level_labels[function_value], 30, 30, 1)
            oled.text(str(power_level_values[function_value]), 40, 40, 1)
        elif mode_function == 1:
            oled.text(turn_dist_labels[function_value], 30, 30, 1)
            oled.text(str(turn_dist_values[function_value]), 40, 40, 1)
        elif mode_function == 2:
            oled.text(reverse_time_labels[function_value], 30, 30, 1)
            oled.text(str(reverse_time_values[function_value]), 40, 40, 1)
        elif mode_function == 3:
            oled.text(turn_time_labels[function_value], 30, 30, 1)
            oled.text(str(turn_time_values[function_value]), 40, 40, 1)
        oled.text('ValN: ', 0, 40, 1)
                
    # show function
    if mode == 4:
        oled.text('Funct: ', 0, 30, 1)
        oled.text(str(mode_function), 50, 30, 1) 
        oled.text('Dist: ', 0, 40, 1)
        oled.text(str(dist), 50, 40, 1)
    
    # draw on the bottom row
    oled.text('Counter: ', 0, 57, 1)
    oled.text(str(counter), 65, 57, 1)
    
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

def play_reverse():
    playnote(400, 0.1)
    
def play_turn_right():
    playnote(500, 0.1)
    
def play_turn_left():
    playnote(700, 0.1)

# our PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

def turn_motor_on(pwm):
   pwm.duty_u16(motor_power)

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
    
print('Collision Avoidance Display Rotary Ping with Speaker')
play_startup()

counter = 0
current_dist = 0
# change the defaut mode
mode = 2
def main():
    global counter, dist, current_dist
    current_mode = mode
    current_mode_function = mode_function
    current_function_value = function_value
    print('in main')
    while True:
        dist = ping()
        if dist != current_dist and dist < MAX_DIST and mode != 2:
            print("Distance:", dist, " cm")
            current_dist = dist
        update_display()
        
        # run mode
        if mode == 1:
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
            else:
                print('forward')
                forward()

        # program mode
        if mode == 2:
            stop()
        
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
    stop()