from machine import Pin, PWM
from time import sleep
from machine import Pin
from machine import I2C
import VL53L0X
from neopixel import NeoPixel

# Motor Code
# lower right pins with USB on top
RIGHT_FORWARD_PIN = 19
RIGHT_REVERSE_PIN = 18
LEFT_FORWARD_PIN = 20
LEFT_REVERSE_PIN = 21

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

# Sensor Code
sda=machine.Pin(16)
scl=machine.Pin(17)
i2c=machine.I2C(0, sda=sda, scl=scl)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)
tof.start() # startup the sensor

# used to blink the onboard LED
led_onboard = machine.Pin(25, machine.Pin.OUT)

# LED Code
NEOPIXEL_PIN = 15
NUMBER_PIXELS = 72
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# driving parameters
POWER_LEVEL = 30000 # use a value from 20000 to 65025
TURN_THRESHOLD = 400 # 25 cm
TURN_TIME = .25 # seconds of turning
BACKUP_TIME = .75 # seconds of backing up if obstacle detected

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
colors = (red, orange, yellow, green, blue, indigo, violet)

def turn_motor_on(pwm):
   pwm.duty_u16(POWER_LEVEL)

def turn_motor_off(pwm):
   pwm.duty_u16(0)

def forward():
    turn_motor_on(right_forward)
    turn_motor_on(left_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_reverse)
    #for i in range(numpix):
    #    strip.set_pixel(i, green)
    #strip.show()

def reverse():
    turn_motor_on(right_reverse)
    turn_motor_on(left_reverse)
    turn_motor_off(right_forward)
    turn_motor_off(left_forward)
    #for i in range(numpix):
    #    strip.set_pixel(i, red)
    #strip.show()
    
def turn_right():
    turn_motor_on(right_forward)
    turn_motor_on(left_reverse)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    #for i in range(numpix):
    #    strip.set_pixel(i, blue)
    #strip.show()
    
def turn_left():
    turn_motor_on(right_reverse)
    turn_motor_on(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)
    #for i in range(numpix):
    #    strip.set_pixel(i, yellow)
    #strip.show()
    
def stop():
    turn_motor_off(right_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    turn_motor_off(left_reverse)
    for i in range(numpix):
        strip.set_pixel(i, violet)
    strip.show()

def read_sensor_avg():
    total = 0
    for i in range(10):
        total = total + tof.read()
        sleep(.01)
    return int(total/10)

# offset is the color to start (0 to 6)
# dir is 1 for forward and -1 for reverse
def color_wipe_4(offset, dir):
    for i in range(12):
        if dir == 1:
            this_color = colors[ ((i-offset) %7 )]
        else:
            this_color = colors[ ((i+offset) %7 )]
        strip[i] = this_color
        strip[23-i] = this_color
        strip[i+24] = this_color
        strip[47-i] = this_color
        strip[48+i] = this_color
        strip[71-i] = this_color
        strip.write()
        # time.sleep(0.01)

counter = 0
while True:
    dist = read_sensor_avg()
    print(dist)
    if dist < TURN_THRESHOLD:
        print('object detected')
        reverse()
        
        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1
        
        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1

        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1        

        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1        

        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1        

        turn_right()
        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1        

        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1        

        color_wipe_4(counter % 7, -1)
        sleep(.1)
        counter += 1        

    else:
        forward()
        print("going forward")
        color_wipe_4(counter % 7, 1)
    counter += 1