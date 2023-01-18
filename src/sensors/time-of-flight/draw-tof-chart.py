from machine import Pin,PWM
import VL53L0X
from time import sleep
import ssd1306
from neopixel import NeoPixel

# OLED Display dimentions
HEIGHT = 64
WIDTH = 128
CS = machine.Pin(6)
DC = machine.Pin(5)
SCK=machine.Pin(2)
SDA=machine.Pin(3)
RES = machine.Pin(4)
spi=machine.SPI(0,sck=SCK, mosi=SDA)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)


sda=Pin(26) # Grove connector 6
scl=Pin(27) # Colors on ToF sensor are RBYW (red, black, yello white)
i2c_tof=machine.I2C(1, sda=sda, scl=scl, freq=400000)
MAX_DIST = 365
# print(i2c_tof)

# the two on-board NeoPixels
NUMBER_PIXELS = 2
NEOPIXEL_PIN = 18

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
red = (255, 0, 0)
lightPink = (10,0,0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
lightGreen = (0, 25, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130) # purple?
purple = (75, 0, 130)
violet = (138, 43, 226) # mostly pink
cyan = (0, 255, 255)
lightgreen = (100, 255, 100)
white = (128, 128, 128) # not too bright
pink = (255, 128, 128)
color_names = ('red', 'orange', 'yellow', 'green', 'light green', 'blue', 'indigo', 'violet', 'cyan', 'lightgreen', 'white')
num_colors = len(color_names)
colors = (red, orange, yellow, green, lightGreen, blue, indigo, violet, cyan, lightgreen, white, pink)

# The Piezo Buzzer is on GP22
buzzer=PWM(Pin(22))

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

x=0
def update_display(distance):
    global x
    print(x, distance)
    if distance > 63:
        distance = 63
    oled.pixel(x,HEIGHT - int(distance) - 1, 1)
    if x > WIDTH - 3:
        oled.scroll(-1,0)
    else:
        x += 1
    oled.show()

# time of flight calibration parameters
zero_dist = 65 # distance measure when an object is about 1/2 cm away
max_dist = 350 # max distance we are able to read
scale_factor = .2

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

# a list of our prior distance measurements for graphing mode
distances=[]

# startup
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_tof)
tof.start()

valid_distance = 0
mode = 0
# loop forever
def main():
    global mode, valid_distance
    while True:
        distance = get_distance()      
        if distance < MAX_DIST:
            update_display(distance)
            strip[0] = lightGreen
            strip[1] = lightGreen
            strip.write()
        else:
            strip[0] = lightPink
            strip[1] = lightPink
            strip.write()
            play_no_signal()
        sleep(.05)
        

# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrupt
print('Running Chart Time of Flight')

try:
    main()
except KeyboardInterrupt:
    print('Got interupt')
finally:
    # Optional cleanup code
    print('Powering down sound')
    sound_off()
    tof.stop()
