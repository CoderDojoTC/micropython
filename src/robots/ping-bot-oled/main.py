from machine import Pin, PWM
import ssd1306
from utime import sleep, sleep_us, ticks_us
from urandom import randint

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)

spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)

CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)

TRIGGER_PIN = 16 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 17 # One up from bottom left corner
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back

width=128
height=64
oled = ssd1306.SSD1306_SPI(width, height, spi, DC, RES, CS)

# Motor controller pins
RIGHT_FORWARD_PIN = 18
RIGHT_REVERSE_PIN = 19
LEFT_FORWARD_PIN = 21
LEFT_REVERSE_PIN = 20

# Our PWM objects - one for each motor and direction
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))
# onboard LED
led_onboard = machine.Pin(25, machine.Pin.OUT)


# DRIVING PARAMETERS
# Distance in CM that we stop, backup and turn.  A value from 10 to 30 is a good range.
TURN_DISTANCE = 15
# Seconds we backup
BACKUP_TIME = .75
# Seconds we turn
TURN_TIME = .75
DRIVE_SPEED = 200 # 100 to 255

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
    return distance

def turn_motor_on(pwm):
   pwm.duty_u16(int(DRIVE_SPEED * 254)) # 0 to 65025

def turn_motor_off(pwm):
   pwm.duty_u16(0)

def forward():
    print(' forward ', sep='')
    turn_motor_on(right_forward)
    turn_motor_on(left_forward)
    #turn_motor_off(right_reverse)
    #turn_motor_off(left_reverse)

def reverse():
    print(' reverse ', sep='')
    turn_motor_on(right_reverse)
    turn_motor_on(left_reverse)
    turn_motor_off(right_forward)
    turn_motor_off(left_forward)
    
def turn_right():
    print(' turning right ', sep='')
    turn_motor_on(right_reverse)
    turn_motor_on(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)
    
def turn_left():
    print(' turning left ', sep='')
    turn_motor_on(right_forward)
    turn_motor_on(left_reverse)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)

def stop():
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)

    # test
def test():
    print('runnint forward, reverse, right, left test')
    stop()
    forward()
    sleep(1)
    reverse()
    sleep(1)
    turn_right()
    sleep(1)
    turn_left()
    sleep(1)

def update_oled(dist, message):
    oled.fill(0)
    oled.text(str(dist), 0, 0, 1)
    oled.text(message, 0, 20, 1)
    oled.show()
# while True:
#    test()

update_oled(ping(), 'CoderDojo Rocks!')
sleep(.25)
stop()

counter = 0
while True:
    distance = ping()

    # skip over large numbers
    while distance > 100:
        distance = ping()
    print(distance)
    if distance < TURN_DISTANCE:
        print('Reversing')
        update_oled(distance, 'Reversing')
        reverse()
        sleep(BACKUP_TIME)
        stop()
        sleep(.5)

        if randint(0,2): # 50% chance of being true
           turn_right()
           update_oled(distance, 'Turning Right')
        else:
            turn_left()
            update_oled(distance, 'Turning Left')
        sleep(TURN_TIME)
        stop()
        sleep(.5)
    else:
        print('Forward')
        update_oled(distance, 'Forward')
        forward()
        sleep(.1)
        
    print("counter: ", counter)
    led_onboard.toggle()
    counter += 1
    # sleep(.5)