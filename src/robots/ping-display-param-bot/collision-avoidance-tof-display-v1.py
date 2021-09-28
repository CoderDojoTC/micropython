# Collision Avoidance Demo for Cytron Maker Pi RP2040 board
# Version 3.0 with startup sounds and NeoPixel feedback

from machine import Pin,PWM
from utime import sleep, ticks_ms
import random
import VL53L0X
from neopixel import Neopixel
import ssd1306

# key parameters
MOTOR_POWER = 20000 # min is 20000 max is 65025
motor_power = MOTOR_POWER
MOTOR_POWER_CODE = 3
TURN_DISTANCE = 25 # distnce we decide to turn - try 20
turn_distance = TURN_DISTANCE
REVERSE_TIME = .4 # how long we backup
reverse_time = REVERSE_TIME
TURN_TIME = .4 # how long we turn
turn_time = TURN_TIME
MAX_DIST = 200
MAX_POWER_LEVEL = 65025

# The Piezo Buzzer is on GP22
BUZZER_PIN = 22
buzzer=PWM(Pin(BUZZER_PIN))

# lower left on pico
MODE_BUTTON_PIN = 21
MODE_VALUE_BUTTON_PIN = 20
# buttons pull down to GND from 3.3v rail
mode_irq = machine.Pin(MODE_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
mode_value_irq = machine.Pin(MODE_VALUE_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

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

NUMBER_PIXELS = 2
STATE_MACHINE = 0
NEOPIXEL_PIN = 18

# Global Variables
mode = 0 # mode of operation.  0=standby, 1=run collision avoidance
current_mode = -1
dist = 0 # distance to object in front of us
valid_dist = 1
mode_value = 0 # the value for the currnt mode
counter = 0 # main loop counter

mode_menu = ['Standby', 'Run Col Avoid', 'Run Square', 'Change Power', 'Change Disk', 'Ch Rev Time', 'Ch Turn Time', 'Status']
mode_count = len(mode_menu)
functions_menu = ['Motor Power', 'Turn Dist', 'Rev Time', 'Turn Time']
function_menu_count = len(functions_menu)
# power
motor_power_code = MOTOR_POWER_CODE
motor_power_labels = ['Off', 'Low', 'Medium-Low', 'Medium', 'Medium-High', 'High', 'Max']
# three letter code due to limited screen area
motor_power_abbr =    ['Off', 'Low', 'ML',         'Med',    'MH',          'Hi',   'Max']
motor_power_values = [0,      20000, 30000,       40000,    50000,         55000,  MAX_POWER_LEVEL]
motor_power_count = len(motor_power_labels)
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
# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, NEOPIXEL_PIN, "GRB")
strip.brightness(100)

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

# display setup
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
WIDTH=128
HEIGHT=64
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# This function gets called every time the button is pressed.  The parameter "pin" used to determine what pin is pressed.
last_time = 0
def button_pressed_handler(pin):
    global mode, mode_value, last_time
    new_time = ticks_ms()
    print(pin)
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 100:
        if '21' in str(pin):
            mode +=1
            if mode > mode_count - 1:
                mode = 0
        else:
            mode_value +=1
            if mode_value > 6:
                mode_value = 0
        last_time = new_time

# call the button_pressed_handler when buttons are pressed - down from 3.3 on open
mode_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)
mode_value_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)

def turn_motor_on(pwm):
   pwm.duty_u16(motor_power)

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

# Time of flight sensor is on the I2C bus on Grove connector 0
I2C_SDA_PIN = 26
I2C_SCL_PIN = 27
i2c=machine.I2C(1,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)
print("Device found at decimal", i2c.scan())

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs
blue_led_pins = [2, 3,  4,  5,  6,  7, 16, 17, 26, 27, 28]
# dist_scale =    [2, 4, 6, 8, 10, 13, 16, 20, 25, 35, 50, 75, 100]
dist_scale =    [2, 4, 6, 8, 10, 15, 20, 25, 50, 100, 150, 200, 300]

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

def update_display():
    global dist, counter
    oled.fill(0)
    # put the first row in reverse text with dark chars on white background
    oled.fill_rect(0, 0, WIDTH - 1, 9, 1)
    if mode == 0:
        oled.text('Mode: Standby', 0, 1, 0)
        oled.text('Press button', 0, 11, 1)
        oled.text('GP19 to start.', 0, 20, 1)
        oled.text(str(dist), 0, 30, 1)
    elif mode == 1:
        oled.text('Mode: Run CA', 0, 1, 0)
    elif mode == 2:
        oled.text('Change Power', 0, 1, 0)
    oled.text(str(counter), 0, 54, 1)
    oled.show()

# loop forever
def main():
    global dist, valid_distance, counter, mode, current_mode
    while True:
        if mode == 0:
            update_display()
        if mode == 1:
            dist = get_distance()
            if dist > MAX_DIST:
                # only print if we used to have a valid distance
                if valid_distance == 1:
                    print('no signal')
                    play_no_signal()
                valid_distance = 0
            # we have a valid distance
            else:
                print(dist)
                if dist < TURN_DISTANCE:    
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
                led_show_dist(dist)
        if mode == 2:
            print('mode 2')
        if mode == 3:
            print('mode 3')
        if mode == 4:
            print('mode 4')
        sleep(.1)
        counter += 1
        if mode != current_mode:
            print(counter, 'mode:', mode, 'mode val:', mode_value)
            current_mode = mode
        if (counter % 50) == 0:
            print(counter, 'mode:', mode, 'mode val:', mode_value)

# startup
tof = VL53L0X.VL53L0X(i2c)
tof.start()
oled.fill(0)
oled.text('Mode: Standby', 0, 1, 0)
oled.text('Press button', 0, 11, 1)
oled.text('GP19 to start.', 0, 20, 1)
oled.show()
# run_lights()
# play_startup()

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
