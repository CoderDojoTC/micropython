# display a plot of ping distance vertical and time across the x-axis
# scroll as we get more values
from machine import Pin
from utime import sleep
import hcsr04
import ssd1306

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

TRIGGER_PIN = 14 # Connect the white Grove connector wire next to the 5volt on the ping sensor
ECHO_PIN = 15 # Connect the yellow Grove connector wire next to the GND on the ping sensor
MAX_VALID = 64

ping_sensor = hcsr04.HCSR04(TRIGGER_PIN, ECHO_PIN)

x = 0
def update_display(distance):
    global x
    # print(x, distance)
    if distance > 63:
        distance = 63
    oled.pixel(x,HEIGHT - int(distance) - 1, 1)
    if x > WIDTH - 3:
        oled.scroll(-1,0)
    else:
        x += 1
    oled.show()
    
def avg_dist(num):   
    total_val = 0
    for i in range(0,num):
        total_val += ping_sensor.distance_cm()
        sleep(.01)
    return round(total_val/num, 3)

while True:
    distance_cm = avg_dist(10)
    print(distance_cm)
    if distance_cm < MAX_VALID:
        update_display(distance_cm)
    else:
        print('out of range:', distance_cm)
    sleep(.01)
