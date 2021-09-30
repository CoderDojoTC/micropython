# Collision Avoidance Demo for Cytron Maker Pi RP2040 board
# Version 3.0 with startup sounds and NeoPixel feedback

from machine import Pin,PWM
from utime import sleep, ticks_ms
import random
import VL53L0X
from neopixel import Neopixel
import ssd1306
from robotfunctions import sound_off, stop, forward, turn_right, turn_left, playnote, drive_reverse

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
    print(mode)

# call the button_pressed_handler when buttons are pressed - down from 3.3 on open
mode_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)
mode_value_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)


# time of flight calibration parameters
# calibration parameters for the Time of Flight Sensor

TOF_ZERO_VALUE = 60
TOF_MAX_SENSOR_DIST = 1200
TOF_SCALE = .25

# get the normalized time-of-flight distance
def get_distance():
    global zero_dist, scale_factor
    tof_distance = tof.read()
    if tof_distance > TOF_MAX_SENSOR_DIST:
        return TOF_MAX_SENSOR_DIST
    # if our current time-of-flight distance is lower than our zero distance then reset the zero distance
    #if tof_distance < TOF_ZERO_VALUE:
    #    zero_dist = tof_distance
    return  int((tof_distance - TOF_ZERO_VALUE) * TOF_SCALE)

def update_display():
    global dist, counter
    oled.fill(0)
    # put the program mode in the first row in reverse text with dark chars on white background
    oled.fill_rect(0, 0, WIDTH - 1, 9, 1)
    oled.text(mode_menu[mode], 0, 1, 0)
    if mode == 0:
        oled.text('Press button', 0, 11, 1)
        oled.text('GP19 to start.', 0, 20, 1)
        oled.text('Dist:', 0, 30, 1)
        oled.text(str(dist), 40, 30, 1)
        oled.text('Action:', 0, 40, 1)
        if dist < turn_distance:
            oled.text('Turn', 55, 40, 1)
        else:
            oled.text('Forward', 55, 40, 1)
    elif mode == 1: # collision avoidance
        oled.text('Dist:', 0, 30, 1)
        oled.text(str(dist), 40, 30, 1)
        oled.text('Action:', 0, 40, 1)
        if dist < turn_distance:
            oled.text('Turn', 55, 40, 1)
        else:
            oled.text('Forward', 55, 40, 1)
    elif mode == 2: # square
        oled.text('Select level:', 0, 10, 1)
        oled.text(motor_power_labels[mode_value], 0, 20, 1)
    elif mode == 3: # select power
        oled.text('Select level:', 0, 10, 1)
        oled.text(motor_power_labels[mode_value], 0, 20, 1)
    elif mode == 4: # turn dist
        oled.text('Select Turn Dist', 0, 10, 1)
        oled.text(turn_dist_labels[mode_value], 0, 20, 1)
    elif mode == 5: # reverse time
        oled.text('Reverse Time:', 0, 10, 1)
        oled.text(reverse_time_labels[mode_value], 0, 20, 1)
    elif mode == 6: # reverse time
        oled.text('Turn Time:', 0, 10, 1)
        oled.text(turn_time_labels[mode_value], 0, 20, 1)
    oled.text(str(counter), 0, 54, 1)
    oled.text(str(mode), 50, 54, 1)
    oled.text(str(mode_value), 80, 54, 1)
    oled.show()

last_mode = -1
# loop forever
def main():
    global dist, counter, mode, mode_value, last_mode, current_mode, motor_power
    while True:
        dist = get_distance()
        update_display()
        if mode != last_mode:
            print('mode', mode, 'Label:', mode_menu[mode])
            last_mode = mode
        if mode == 0: # standby    
            stop()
        if mode == 1: # collision avoidance
            if dist > TOF_MAX_SENSOR_DIST:
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
                    drive_reverse(motor_power)
                    sleep(REVERSE_TIME)
                    # turn in a random direction
                    if random.random() > .5:
                        print('turning right')
                        turn_right(motor_power)
                    else:
                        print('turning left')
                        turn_left(motor_power)
                    sleep(TURN_TIME)
                    # continue going forward
                    forward(motor_power)
                else:
                    print('forward')
                    forward(motor_power)
        if mode == 2: # drive square
            print('mode 2')
            forward(motor_power)
            sleep(SQUARE_FWD_TIME)
            turn_right(motor_power)
            sleep(turn_time)
        if mode == 3: # prog power
            stop()
            motor_power = motor_power_values[mode_value]
            print(mode_menu[mode])
        if mode == 4: # prog turn dist
            print(mode_menu[mode])
        if mode == 4: # prog turn dist
            print(mode_menu[mode])
        sleep(.1)
        counter += 1
        if mode != current_mode:
            print(counter, 'mode:', mode, 'mode val:', mode_value)
            current_mode = mode
        #if (counter % 50) == 0:
            #print(counter, 'mode:', mode, 'mode val:', mode_value)

# startup
tof = VL53L0X.VL53L0X(i2c)
tof.start()

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
