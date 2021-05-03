# drive forward
from machine import Pin, PWM
from time import sleep
import ssd1306

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)

width=128
height=64
oled = ssd1306.SSD1306_SPI(width, height, spi, DC, RES, CS)

# lower right pins with USB on top
RIGHT_FORWARD_PIN = 18
RIGHT_REVERSE_PIN = 19
LEFT_FORWARD_PIN = 21
LEFT_REVERSE_PIN = 20

DRIVE_SPEED = 255 # 100 to 255

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

TEST_TIME = 2 # seconds per test

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
    print(' stop ', sep='')
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)
    
def test():
    print('runnint forward, reverse, right, left test')
    
    stop()
    forward()
    oled.fill(0)
    oled.text('Foward', 4, 10, 1)
    oled.show()
    sleep(TEST_TIME)
    reverse()
    oled.fill(0)
    oled.text('Reverse', 4, 10, 1)
    oled.show()
    sleep(TEST_TIME)
    turn_right()
    oled.fill(0)
    oled.text('Right', 4, 10, 1)
    oled.show()
    sleep(TEST_TIME)
    turn_left()
    oled.fill(0)
    oled.text('Left', 4, 10, 1)
    oled.show()
    sleep(TEST_TIME)

while True:
    test()