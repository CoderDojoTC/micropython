# Collision Avoidance Demo for Maker Pi RP2040 board
# Version 2.0 with random turn direction and different sounds for left and right turns

from machine import Pin,PWM
from utime import sleep
import random
import hcsr04
from array import array
import framebuf
import ssd1306

# Piezo Buzzer is on GP22
buzzer=PWM(Pin(22))

TRIGGER_PIN = 14 # Connect the white Grove connector wire next to the 5volt on the ping sensor
ECHO_PIN = 15 # Connect the yellow Grove connector wire next to the GND on the ping sensor
MAX_VALID = 64
ping_sensor = hcsr04.HCSR04(TRIGGER_PIN, ECHO_PIN)

# max = 65025, min = 20000
POWER_LEVEL = 20000
BACKUP_TIME = 0.5 # time to backup get near an obsticle
TURN_TIME = 0.75 # time to turn if we get near an obsticle

# Motor Pins are A: 8,9 and B: 10,11
RIGHT_FORWARD_PIN = 9
RIGHT_REVERSE_PIN = 8
LEFT_FORWARD_PIN = 11
LEFT_REVERSE_PIN = 10

# our PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

WIDTH = 128
# bit shifting only works when the numbers are a power of 2
HALF_WIDTH = WIDTH >> 1
QUARTER_WIDTH = HALF_WIDTH >> 1
HEIGHT = 64
HALF_HEIGHT = HEIGHT >> 1
QUARTER_HEIGHT = HALF_HEIGHT >> 1
ONE_THIRD_HEIGHT = int(HEIGHT/3)

# draw readability
ON = 1
OFF = 0
NO_FILL = 0
FILL = 1

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

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

# get the normalized time-of-flight distance
def avg_dist(num):   
    total_val = 0
    for i in range(0,num):
        total_val += ping_sensor.distance_cm()
        sleep(.01)
    return round(total_val/num, 3)

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
    
def play_no_signal():
    playtone(100)
    sleep(0.1)
    bequiet()

def play_turn_right():
    playtone(500)
    sleep(0.1)
    bequiet()
    
def play_turn_left():
    playtone(700)
    sleep(0.1)
    bequiet()

x = 0
def update_display(distance):
    global x
    print('updating display:', x, distance)
    if distance > 63:
        distance = 63
    oled.pixel(x,HEIGHT - int(distance) - 1, 1)
    if x > WIDTH - 3:
        oled.scroll(-1,0)
    else:
        x += 1
    oled.show()

# start our time-of-flight sensor
valid_distance = 1

# loop forever
def main():
    global valid_distance
    while True:  
        distance = avg_dist(10)
        update_display(distance)
        if distance > 1000:
            # only print if we used to have a valid distance
            if valid_distance == 1:
                print('no signal')      
            valid_distance = 0
        else:
            print(distance)
            if distance < 30:
                
                # back up for a bit
                reverse()
                sleep(BACKUP_TIME)
                # turn in a random direction
                if random.random() > .5:
                    print('turning right')
                    play_turn_right()
                    turn_right()
                else:
                    print('turning left')
                    play_turn_left()
                    turn_left()
                sleep(TURN_TIME)
            else:
                print('forward')
                forward()
            valid_distance = 1
            update_display(distance)
        sleep(0.05)

# clean up


# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrupt
print('Running Collision Avoidence version 1.0')

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('turning off sound')
    buzzer.duty_u16(0)
    stop()
