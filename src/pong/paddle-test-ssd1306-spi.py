# Pong game on Raspberry Pi Pico with a OLED and two Potentimeters
from machine import Pin, PWM, SPI
import ssd1306
from utime import sleep
import random # random direction for new ball

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)
# connect the center tops of the potentiometers to ADC0 and ADC1
pot_pin_1 = machine.ADC(26)
pot_pin_2 = machine.ADC(26) # make them the same for testing

# lower right corner with USB connector on top
SPEAKER_PIN = 16
# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

# globals variables
# static variables are constants are uppercase variable names
WIDTH = 128
HEIGHT = 64
HALF_HEIGHT = HEIGHT
BALL_RADIUS = 5
PAD_WIDTH = 2
PAD_HEIGHT = 8
HALF_PAD_WIDTH = int(PAD_WIDTH / 2)
HALF_PAD_HEIGHT = int(PAD_HEIGHT / 2)
POT_MIN = 3000
POT_MAX = 65534
MAX_ADC_VALUE = 65534 # Maximum value from the Analog to Digital Converter is 2^16 - 1
# dynamic global variables use lowercase
ball_pos = [0,0]
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

def play_startup_sound():
    speaker.duty_u16(1000)
    speaker.freq(600)
    sleep(.25)
    speaker.freq(800)
    sleep(.25)
    speaker.freq(1200)
    sleep(.25)
    speaker.duty_u16(0)
    
# note that OLEDs have problems with screen burn it - don't leave this on too long!
def border(WIDTH, HEIGHT):
    oled.rect(0, 0, WIDTH, HEIGHT, 1)


# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def valmap(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

# draw a vertical bar
def draw_paddle(paddle_no, paddle_center):
    if paddle_no == 1:
        x = 1
    else:
        x = WIDTH - PAD_WIDTH - 1
    y = paddle_center - HALF_PAD_HEIGHT
    ## x, y, width, height
    oled.fill_rect(x,  y, PAD_WIDTH, PAD_HEIGHT, 1) # fill with 1s
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





# continiuous update of the paddle and ball
play_startup_sound()
current_pot_val_1 = 0
print('p=63')
while True:
    oled.fill(0) # clear screen
    border(WIDTH, HEIGHT)
    # read both the pot values
    pot_val_1 = pot_pin_1.read_u16()
    pot_val_2 = pot_pin_1.read_u16()
    # print(pot_val_1)
    
    # scale the values from the max value of the input is a 2^16 or 65536 to 0 to HEIGHT - PAD_HEIGHT
    # ideally, it should range from 5 to 58
    pot_val_1 = valmap(pot_val_1, POT_MIN, POT_MAX, HALF_PAD_HEIGHT, HEIGHT - HALF_PAD_HEIGHT - 2)
    pot_val_2 = valmap(pot_val_2, POT_MIN, POT_MAX, HALF_PAD_HEIGHT, HEIGHT - HALF_PAD_HEIGHT - 2)
    
    # print only on change of value
    if current_pot_val_1 != pot_val_1:
        print('p=', pot_val_1)
        current_pot_val_1 = pot_val_1
    oled.vline(0, pot_val_1, 10, 1)
    
    # print(pot_val, pot_scaled)
    draw_paddle(1, pot_val_1 + HALF_PAD_HEIGHT)
    draw_paddle(2, pot_val_2 + HALF_PAD_HEIGHT)
    
    oled.text('p1:', 5, HALF_HEIGHT + 5, 1)
    oled.text(str(pot_val_1), 30, HALF_HEIGHT + 5, 1)
    
    oled.text('p2:', 5, HALF_HEIGHT + 15, 1)
    oled.text(str(pot_val_2), 60, HALF_HEIGHT + 15, 1)
    
    oled.show()

print('Done')