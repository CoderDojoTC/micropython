# Pong game on Raspberry Pi Pico with a OLED and two Potentimeters
import machine
import utime
import random # random direction for new ball
from ssd1306 import SSD1306_I2C
# import sh1106

# connect the OLED SDA (data) on top pin 1 on the left with USP on top
sda=machine.Pin(0)
# connect the OLED SCL (clock) on send from the top pin 1 
scl=machine.Pin(1)
# connect the center tops of the potentiometers to ADC0 and ADC1
pot_pin_1 = machine.ADC(26)
pot_pin_2 = machine.ADC(27)

# globals variables
# static variables are constants are uppercase variable names
WIDTH = 128
HEIGHT = 64
HALF_HEIGHT = HEIGHT
BALL_RADIUS = 5
PAD_WIDTH = 2
PAD_HEIGHT = 8
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
MAX_ADC_VALUE = 65534 # Maximum value from the Analog to Digital Converter is 2^16 - 1
# dynamic global variables use lowercase
ball_pos = [0,0]
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

# initialize the I2C communications interface with the OLED
i2c=machine.I2C(0,sda=sda, scl=scl)


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
# oled = sh1106.SH1106_I2C(width, height, i2c, machine.Pin(4), 0x3c)

# note that OLEDs have problems with screen burn it - don't leave this on too long!
def border(WIDTH, HEIGHT):
    oled.hline(0, 0, WIDTH - 1, 1) # top edge
    oled.hline(0, HEIGHT - 1, WIDTH - 1, 1) # bottom edge
    oled.vline(0, 0, HEIGHT - 1, 1) # left edge
    oled.vline(WIDTH - 1, 0, HEIGHT - 1, 1) # right edge

# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def valmap(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

# draw a vertical bar
def draw_paddle(paddle_no, paddle_center):
    top_edge = paddle_center - HALF_PAD_HEIGHT
    bottom_edge = paddle_center + HALF_PAD_HEIGHT
    if paddle_no == 1:
        left_edge = 2
    else:
        left_edge = WIDTH - PAD_WIDTH - 1
    right_edge = left_edge + PAD_WIDTH
    oled.fill_rect(int(left_edge), int(top_edge), int(bottom_edge), left_edge + PAD_WIDTH, 1) # fill with 1s
    # utime.sleep(.1) # wait a bit

def check_edge():
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel
    
    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel
    #update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

# continiuous update
# while True:
# for i in range(10):
while True:
    oled.fill(0) # clear screen
    border(WIDTH, HEIGHT)
    # read both the pot values
    pot_val_1 = int(pot_pin_1.read_u16())
    pot_val_2 = int(pot_pin_2.read_u16())
    print(pot_val_1)
    
    # scale the values from the max value of the input is a 2^16 or 65536 to 0 to HEIGHT - PAD_HEIGHT
    pot_val_1 = valmap(pot_val_1, 0, MAX_ADC_VALUE, PAD_HEIGHT, HEIGHT - PAD_HEIGHT)
    pot_val_2 = valmap(pot_val_2, 0, MAX_ADC_VALUE, PAD_HEIGHT, HEIGHT - PAD_HEIGHT)
    print(pot_val_1)
    
    oled.vline(0, pot_val_1, 10, 1)
    
    # print(pot_val, pot_scaled)
    draw_paddle(1, pot_val_1)
    draw_paddle(2, pot_val_1)
    
    oled.text('p1:', 5, HALF_HEIGHT + 5, 1)
    oled.text(str(pot_val_1), 30, HALF_HEIGHT + 5, 1)
    
    oled.text('p2:', 5, HALF_HEIGHT + 15, 1)
    oled.text(str(pot_val_2), 60, HALF_HEIGHT + 15, 1)
    
    oled.show()

print('Done')