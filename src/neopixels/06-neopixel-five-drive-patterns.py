'''
Five drive patterns
1 - idle - rainbow moving
2 - forward - white going front (7) to back (0)
3 - reverse - blue boing back (0) to front (7)
4 - right turn - blink red
5 - left turn - blink green
'''
import machine
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 2
NUMBER_PIXELS = 8
PERCENT_COLOR_WHEEL = round(255/NUMBER_PIXELS)

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_RED = (15, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 25, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 0, 25)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (10, 10, 10)
OFF = (0, 0, 0)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def idle(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    for i in range(0, NUMBER_PIXELS):
        color_index = round(i*PERCENT_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        strip[(i + counter) % NUMBER_PIXELS] = color
        strip.write()
    sleep(wait)

def forward(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    for i in range(0, NUMBER_PIXELS):
        if i == NUMBER_PIXELS - pixel_index - 1:
            strip[i] = LIGHT_GRAY
        else:
            strip[i] = OFF
    strip.write()
    sleep(wait)

def reverse(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    for i in range(0, NUMBER_PIXELS):
        if i == pixel_index:
            strip[i] = LIGHT_BLUE
        else:
            strip[i] = OFF
    strip.write()
    sleep(wait)
    
def right(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    if counter % 2:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = LIGHT_RED
    else:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = OFF
    strip.write()
    sleep(wait)

def left(counter, wait):
    global NUMBER_PIXELS, PERCENT_COLOR_WHEEL
    pixel_index = counter % NUMBER_PIXELS
    if counter % 2:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = LIGHT_GREEN
    else:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = OFF
    strip.write()
    sleep(wait)

def all_off():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = OFF
    strip.write()

counter = 0
between_pattern_delay = 1
while True:
    for i in range(8):
        print('Idle', counter)
        idle(counter, .4)
        counter += 1
    all_off()
    sleep(between_pattern_delay)
    
    for i in range(8):
        print('Forward', counter)
        forward(counter, .2)
        counter += 1
    all_off()
    sleep(between_pattern_delay)
    
    for i in range(8):
        print('Reverse', counter)
        reverse(counter, .2)
        counter += 1
    all_off()
    sleep(between_pattern_delay)
    
    for i in range(8):
        print('Right', counter)
        right(counter, .4)
        counter += 1
    all_off()
    sleep(between_pattern_delay)
    
    for i in range(8):
        print('Left', counter)
        left(counter, .4)
        counter += 1
    all_off()
    sleep(between_pattern_delay)