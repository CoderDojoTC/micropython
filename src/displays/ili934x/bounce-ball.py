from ili934x import ILI9341, color565
from machine import Pin, SPI
from utime import sleep

WIDTH = 320
HEIGHT = 240
ROTATION = 3 # landscape with 0,0 in upper left and pins on left
SCK_PIN = 2
MISO_PIN = 3
DC_PIN = 4
RST_PIN = 5
CS_PIN = 6

# mosi=Pin(23)
# miso=Pin(MISO_PIN)
spi = SPI(0, baudrate=20000000, mosi=Pin(MISO_PIN),sck=Pin(SCK_PIN))
display = ILI9341(spi, cs=Pin(CS_PIN), dc=Pin(DC_PIN), rst=Pin(RST_PIN), w=WIDTH, h=HEIGHT, r=ROTATION)
display.erase()

# color defintions convered to 565 represnetations
black = color565(0, 0, 0)
white = color565(255, 255, 255)
red = color565(255, 0, 0)
green = color565(0, 255, 0)
blue = color565(0, 0, 255)

# ok, not really a circle - just a square for now
def draw_ball(x,y, size, color):
    if size == 1:
        display.pixel(x, y, color) # draw a single pixel
    else:
        display.fill_rectangle(x, y, size, size, color)

ball_size = 20
# start in the middle of the screen
current_x = int(WIDTH / 2)
current_y = int(HEIGHT / 2)
# start going down to the right
direction_x = 1
direction_y = -1
# delay_time = .0001

# Bounce forever
while True:
    draw_ball(current_x,current_y, ball_size, white)
    sleep(.1)
    draw_ball(current_x,current_y,ball_size, black)
    if current_x < 2:
        direction_x = 1
    # right edge test
    if current_x > WIDTH - ball_size -2:
        direction_x = -1
    # top edge test
    if current_y < 2:
        direction_y = 1
    # bottom edge test
    if current_y > HEIGHT - ball_size - 2:
        direction_y = -1
    # update the ball
    current_x = current_x + direction_x
    current_y = current_y + direction_y
