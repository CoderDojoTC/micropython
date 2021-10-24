# Collision Avoidance Demo for Cytron Maker Pi RP2040 board
# Version 3.1 with startup sounds and NeoPixel feedback

from machine import Pin,PWM
from utime import sleep, ticks_ms
import random
import VL53L0X
from neopixel import Neopixel
import ssd1306
from robotfunctions import sound_off, stop, forward, turn_right, turn_left, playnote, drive_reverse

# Defualt parameters for collision avoidance mode

DEFAULT_MOTOR_POWER_CODE = 3 # med is 30000
DEFAULT_TURN_DISTANCE_CODE = 4 # 15 cm
DEFAULT_REVERSE_TIME_CODE = 4 # .5 seconds
DEFAULT_TURN_TIME_CODE = 4 # .5 seconds

MAX_POWER_LEVEL = 65025
SQUARE_FWD_TIME = 2

# lower left on pico
MODE_BUTTON_PIN = 21
MODE_VALUE_BUTTON_PIN = 20
# buttons pull down to GND from 3.3v rail
mode_irq = machine.Pin(MODE_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
mode_value_irq = machine.Pin(MODE_VALUE_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)



# Global Variables
mode = 0 # mode of operation.  0=standby, 1=run collision avoidance
current_mode = -1
dist = 0 # distance to object in front of us
valid_dist = 1
mode_value = 0 # the value for the currnt mode
counter = 0 # main loop counter

# Time of flight sensor is on the I2C bus on Grove connector 0
I2C_SDA_PIN = 26
I2C_SCL_PIN = 27
i2c=machine.I2C(1,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)
print("Device found at decimal", i2c.scan())

mode_menu = ['Mode: Standby', 'Run Col Avoid', 'Run Square', 'Change Power', 'Change Turn Dist', 'Chg Reverse Time', 'Chg Turn Time', 'Status']
mode_count = len(mode_menu)
functions_menu = ['Motor Power', 'Turn Dist', 'Rev Time', 'Turn Time']
function_menu_count = len(functions_menu)

# power

# motor_power_labels = ['Off', 'Low', 'Medium-Low', 'Medium', 'Medium-High', 'High', 'Max']
# three letter code due to limited screen area
motor_power_pairs = [('Off', 0), ('Low', 20000), ('ML', 30000), ('Med', 37000), ('MH', 49000), ('Hi', 55000), ('Max', MAX_POWER_LEVEL)]
motor_power_count = len(motor_power_pairs)
motor_power_code = DEFAULT_MOTOR_POWER_CODE
motor_power_pair = motor_power_pairs[motor_power_code]
motor_power_label = motor_power_pair[0]
motor_power = motor_power_pair[1]

# turn distance
turn_dist_list = (5, 7, 10, 15, 20, 30, 40)
turn_dist_count = len(turn_dist_list)
turn_dist_code = DEFAULT_TURN_DISTANCE_CODE
turn_distance = turn_dist_list[DEFAULT_TURN_DISTANCE_CODE]

# rev time
reverse_time_list= (.3, .4, .5, .6, .7, .8, .9, 1.0, 1.1, 1.2, 1.5)
reverse_time_count = len(reverse_time_list)
reverse_time_code = DEFAULT_REVERSE_TIME_CODE
reverse_time = reverse_time_list[DEFAULT_REVERSE_TIME_CODE]

# turn times
turn_time_list= (.3, .4, .5, .6, .7, .8, .9, 1.0, 1.1, 1.2, 1.5)
turn_time_count = len(turn_time_list)
turn_time_code = DEFAULT_TURN_TIME_CODE
turn_time = turn_time_list[DEFAULT_TURN_TIME_CODE]

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
    global mode, mode_value, last_time, mode_count, motor_power_code, turn_dist_code, reverse_time_code, turn_time_code
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 100:
        if '21' in str(pin):
            mode +=1
            if mode > mode_count - 1:
                mode = 0
        else:
            if mode == 3:
                motor_power_code += 1
                if motor_power_code >= motor_power_count:
                    motor_power_code = 0
            if mode == 4:
                turn_dist_code += 1
                if turn_dist_code >= turn_dist_count:
                    turn_dist_code = 0
            if mode == 5:
                reverse_time_code += 1
                if reverse_time_code >= reverse_time_count:
                    reverse_time_code = 0
            if mode == 6:
                turn_time_code += 1
                if turn_time_code >= turn_time_count:
                    turn_time_code = 0
    last_time = new_time


# call the button_pressed_handler when buttons are pressed - down from 3.3 on open
mode_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)
mode_value_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)


# time of flight calibration parameters
TOF_ZERO_VALUE = 60 # subtract this from reading so measurements next to sensor are 0 cm
TOF_MAX_SENSOR_DIST = 1200 # ignore anything above this distance
TOF_SCALE = .25 # multiply this to the raw number to convert to CM

# get the normalized time-of-flight distance
def get_tof_distance_cm():
    global zero_dist, scale_factor
    tof_distance = tof.read()
    if tof_distance > TOF_MAX_SENSOR_DIST:
        return TOF_MAX_SENSOR_DIST
    # if our current time-of-flight distance is lower than our zero distance then reset the zero distance
    #if tof_distance < TOF_ZERO_VALUE:
    #    zero_dist = tof_distance
    return  int((tof_distance - TOF_ZERO_VALUE) * TOF_SCALE)

def update_display():
    global dist, counter, mode_value, motor_power, turn_distance, reverse_time, turn_time
    oled.fill(0)
    # put the program mode in the first row in reverse text with dark chars on white background
    oled.fill_rect(0, 0, WIDTH - 1, 9, 1)
    oled.text(mode_menu[mode], 0, 1, 0)
    
    # standby mode - motors are off
    if mode == 0:
        oled.text('Press button', 0, 10, 1)
        oled.text('GP%d to start.' % MODE_BUTTON_PIN, 0, 20, 1)
        oled.text('Dist:%d' % dist, 0, 30, 1)
        action = 'Turn' if dist < turn_distance else 'Forward'
        oled.text('Action:' + action, 0, 40, 1)
    
    # collision avoidance motors are on
    elif mode == 1:
        oled.text('Dist:%d' % dist, 0, 10, 1)
        oled.text('Motor Pwr:' + motor_power_pairs[motor_power_code][0], 0, 20, 1)
        oled.text('Motor Pwr:' + str(motor_power_pairs[motor_power_code][1]), 0, 30, 1)
        action = 'Turn' if dist < turn_distance else 'Forward'
        oled.text('Action:' + action, 0, 40, 1)
    
    # dive in a square
    elif mode == 2:
        oled.text('Sqr Fwd Time:%d' % SQUARE_FWD_TIME, 0, 10, 1)
        oled.text('Motor Pwr:' + str(motor_power_pairs[motor_power_code][0]), 0, 20, 1)
        oled.text('Turn Time:' + str(turn_time_list[turn_time_code]), 0, 30, 1)
        action = 'Turn' if dist < turn_distance else 'Forward'
        oled.text('Action:' + action, 0, 40, 1)
    
    # select power, turn dist, reverse time, turn time
    elif mode == 3: 
        oled.text('Select Power:', 0, 10, 1)
        oled.text(motor_power_pairs[motor_power_code][0], 0, 20, 1)
        oled.text(str(motor_power_pairs[motor_power_code][1]), 0, 30, 1)
        oled.text(str(mode_value), 0, 40, 1)
    
     # turn dist
    elif mode == 4:
        oled.text('Select Turn Dist', 0, 10, 1)
        oled.text(str(turn_dist_list[turn_dist_code]), 0, 20, 1)
        oled.text(str(mode_value), 0, 40, 1)
        
    # reverse time
    elif mode == 5: 
        oled.text('Reverse Time:', 0, 10, 1)
        oled.text(str(reverse_time_list[reverse_time_code]), 0, 20, 1)
    
    # turn time
    elif mode == 6: 
        oled.text('Turn Time:', 0, 10, 1)
        oled.text(str(turn_time_list[turn_time_code]), 0, 20, 1)
        oled.text(str(mode_value), 0, 40, 1)
        
    # summary screen
    elif mode == 7:
        oled.text('Motor Pwr:' + str(motor_power_pairs[motor_power_code][0]), 0, 10, 1)
        oled.text('Turn Dist:' + str(turn_dist_list[turn_distance_code]), 0, 20, 1)
        oled.text('Rev Time:' + str(reverse_time_list[reverse_time_code]), 0, 30, 1)
        oled.text('Turn Time:' + str(turn_time_list[turn_time_code]), 0, 40, 1)
    
    # add to the bottom of the display
    br = 54 # bottom row for numbers
    oled.text('ct:', 0, br, 1)
    oled.text(str(counter), 25, br, 1)
    
    oled.text('md:', 60, br, 1)
    oled.text(str(mode), 75, br, 1)
    
    oled.text('mv:', 90, br, 1)
    oled.text(str(mode_value), 110, br, 1) if (mode != 0 and mode != 1 and mode != 2 and mode != 7) else None
    oled.show()

last_mode = -1
# loop forever
def main():
    global dist, counter, mode, mode_value, last_mode, current_mode, motor_power, turn_distance, reverse_time, turn_time
    while True:
        dist = get_tof_distance_cm()
        update_display()
        
        if mode == 0: # standby    
            stop()
        elif mode == 1: # collision avoidance
            if dist > TOF_MAX_SENSOR_DIST:
                # only print if we used to have a valid distance
                if valid_distance == 1:
                    print('no signal')
                    play_no_signal()
                valid_distance = 0
            # we have a valid distance
            else:
                print(dist)
                if dist < turn_distance:    
                    # back up for a bit
                    drive_reverse(motor_power)
                    sleep(reverse_time)
                    # turn in a random direction
                    if random.random() > .5:
                        print('turning right')
                        turn_right(motor_power)
                    else:
                        print('turning left')
                        turn_left(motor_power)
                    sleep(turn_time)
                    # continue going forward
                    forward(motor_power)
                else:
                    print('forward')
                    forward(motor_power)
        elif mode == 2: # drive square
            print('mode 2')
            forward(motor_power)
            sleep(SQUARE_FWD_TIME)
            turn_right(motor_power)
            sleep(turn_time)
        
        elif mode == 3: # prog power
            stop()
            motor_power = motor_power_pairs[mode_value][1]
            
        elif mode == 4: # prog turn dist
            turn_distance = turn_dist_list[mode_value]
            
        elif mode == 5: # prog rev time
            reverse_time = reverse_time_list[mode_value]
            
        elif mode == 6: # prog turn time
            turn_time = turn_time_dict[mode_value]
         
        sleep(.1)
        counter += 1
        if mode != current_mode:
            print(counter, 'mode:', mode, 'mode val:', mode_value)
            current_mode = mode
            mode_value = 0
        # if (counter % 50) == 0:
            # print(counter, 'mode:', mode, 'mode val:', mode_value)

# startup
tof = VL53L0X.VL53L0X(i2c)
tof.start()

# play_startup()

# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrupt
print('Running Collision Avoidence with Time-of-Flight Sensor Version 3.1')

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