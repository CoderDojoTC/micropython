# St. Patrick's Day Hat
# 36 pixels in a circule in a hat
# The pattern are green, orange and white colors
# The pattern changes every five seconds
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
# This is the best number of pixels for most hats
# if you use 160 pixels/meter strips
NUMBER_PIXELS = 36
RAINBOW_LENGTH = 7
PERCENT_SMALL_COLOR_WHEEL = round(255/RAINBOW_LENGTH)
PERCENT_COLOR_WHEEL = round(255/NUMBER_PIXELS)

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

builtin_led = machine.Pin(25, Pin.OUT)

red = (255,0,0)
green = (0, 255, 0)
green_med = (0,32, 0)
green_light = (0, 8, 0)
blue = (0,0,255)
off = (0, 0, 0)
orange = (140, 60, 0)
white = (255, 255, 255)
colors = (red, white, blue)
color_count = len(colors)
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

mode_list = ['moving rainbow',
             'solid red', 'solid white', 'solid blue',
             'red commet', 'white commet', 'blue commet'
             'running lights red', 'running lights red', 'running lights blue',
             '3-bands 3', '3-bands 4', '3-bands 5',
             'move dot red', 'move dot green', 'move dot blue',
             'rainbow cycle']

mode_count = len(mode_list)
print('mode_count:', mode_count)


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

# erase the entire strip
def erase():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
        strip.write()

def move_dot(counter, color, delay):
        strip[counter] = color
        strip.write()
        sleep(delay)
        strip[counter] = (0,0,0)

def move_dot_rev(counter, color, delay):
        strip[NUMBER_PIXELS - counter - 1] = color
        strip.write()
        sleep(delay)
        strip[NUMBER_PIXELS - counter - 1] = (0,0,0)

def comet_tail(counter, color, delay):
    for i in range(0, color_count):
        # we start to draw at the head of the commet N levels away from the counter
        target = ((level_count - i - 1) + counter) % NUMBER_PIXELS
        # number to scale by
        scale = (levels[i] / 255)
        strip[target] = (int(color[0]*scale), int(color[1]*scale), int(color[2]*scale))
        # erase the tail
        if counter > 0:
            strip[counter-1] = (0,0,0)
        if counter == NUMBER_PIXELS-1:
            strip[counter] = (0,0,0)
    strip.write()
    sleep(delay)

def comet_tail_rev(counter, color, delay):
    for i in range(0, color_count):
        # we start to draw at the head of the commet N levels away from the counter
        target = NUMBER_PIXELS - (((level_count - i - 1) + counter) % NUMBER_PIXELS) - 1
        # number to scale by
        scale = (levels[i] / 255)
        # write up to the color_count
        if target > color_count:
            strip[target] = (int(color[0]*scale), int(color[1]*scale), int(color[2]*scale))
    if counter < NUMBER_PIXELS-1:
            strip[NUMBER_PIXELS - counter - 1] = (0,0,0)
    strip.write()
    sleep(delay)
            
            
def solid_color(color, delay):
    for i in range(0, NUMBER_PIXELS-1):
        strip[i] = color;
    strip.write()
    sleep(delay)


def moving_rainbow(counter, delay):
    for i in range(0, RAINBOW_LENGTH-1):
        color_index = round(i*PERCENT_SMALL_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        # start at the end and subtract to go backwards and add the counter for offset
        index = RAINBOW_LENGTH-1 - i  + counter
        # print(index)
        if index < NUMBER_PIXELS:
            strip[index] = color    
        strip.write()
    # erase the tail if we are not at the start
    if counter > 0:
        strip[counter-1] = (0,0,0)
        strip.write()
    # turn off the last pixel at the top
    if counter == NUMBER_PIXELS-1:
        strip[counter] = (0,0,0)
    sleep(delay)

def candle_rnd():
     green = 50 + randint(0,155)
     red = green + randint(0,50)
     strip[randint(0,NUMBER_PIXELS - 1)] = (red, green, 0)
     strip.write()

def candle(delay):
    for i in range(0, 5):
        candle_rnd()
        sleep(delay)

def random_color_pixel():
    random_offset = randint(0, NUMBER_PIXELS-1)
    random_green_brightness = randint(0, 255)
    strip[random_offset] = (0, random_green_brightness, 0)
    strip.write()
    

def random_color(delay):
    for i in range(0, 5):
        random_color_pixel()
        sleep(delay)

HALF_LENGTH = round(NUMBER_PIXELS/2)
def bounce(counter, color, delay):
    if counter < HALF_LENGTH:
        strip[counter] = color
        strip[NUMBER_PIXELS-1 - counter] = color
        strip.write()
        strip[counter] = (0,0,0)
        strip[NUMBER_PIXELS-1 - counter] = (0,0,0)
        sleep(delay)
    else:
        half_counter = counter - HALF_LENGTH
        strip[HALF_LENGTH - half_counter] = color
        strip[HALF_LENGTH + half_counter] = color
        strip.write()
        strip[HALF_LENGTH - half_counter] = (0,0,0)
        strip[HALF_LENGTH + half_counter] = (0,0,0)
        sleep(delay)

def running_lights(counter, color, spacing, delay):
    for i in range(0, NUMBER_PIXELS):
        if (counter+i) % spacing:
            strip[i] = (0,0,0)
        else:
            strip[i] = color
    strip.write()
    sleep(delay)

def running_lights_rev(counter, color, spacing, delay):
    for i in range(NUMBER_PIXELS-1, 0, -1):
        if (counter-i) % spacing:
            strip[i] = (0,0,0)
        else:
            strip[i] = color
    strip.write()
    sleep(delay)

# Three bands of color rotating down the strip
# This has some bugs but they are not too visible
def three_bands(c, spacing, c1, c2, c3, delay):
    band_length = spacing * 3
    bands = int((NUMBER_PIXELS/ (spacing*3)))
    # print('bands=', bands)
    for i in range(bands): 
        for j in range(spacing):
            index = (i*band_length + j + c) % NUMBER_PIXELS
            #print('red', i,j,c, index)
            if (index) < NUMBER_PIXELS:
                strip[index] = c1
        for j in range(spacing, spacing*2):
            index = (i*band_length + j + c) % NUMBER_PIXELS
            #print('green', i,j,c, index)
            if (index) < NUMBER_PIXELS:
                strip[index] = c2
        for j in range(spacing*2, spacing*3):
            index = (i*band_length + j + c) % NUMBER_PIXELS
            #print('blue', i,j,c, index)
            if (index) < NUMBER_PIXELS:
                strip[index] = c3
        strip.write()
        sleep(delay)

def rainbow_cycle(counter, delay):
    for i in range(0, NUMBER_PIXELS):
        color_index = round(i*PERCENT_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        strip[(i + counter) % NUMBER_PIXELS] = color
        strip.write()
    sleep(delay)

# 0=fwd, 1=rev
state = 0
def cylon_scanner(delay):
    global counter, state
    if state == 0:
        #print('going forward', counter)
        strip[counter] = green_light
        strip[counter+1] = green_med
        strip[counter+2] = green
        strip[counter+3] = green_med
        strip[counter+4] = green_light
        # erase the tail
        if counter > 0: strip[counter-1] = off
        strip.write()
        sleep(delay)
        # reverse direction
        if counter == NUMBER_PIXELS-5:
            state = 1
            counter = 0
            #print('go to reverse', state)
            return
    else:
        i = NUMBER_PIXELS-counter - 5
        #print('in reverse c=', counter, 'i=', i)
        strip[i] = green_light
        strip[i+1] = green_med
        strip[i+2] = green
        strip[i+3] = green_med
        strip[i+4] = green_light
        strip.write()
        sleep(delay)
        # turn off as we move in reverse
        if i < NUMBER_PIXELS-2:
            strip[i+4] = off
        if i == NUMBER_PIXELS - 6:
            strip[NUMBER_PIXELS-1] = off
        if i == 0:
            state = 0
            counter = 0
            #print('switching to forward', counter)

# Global variables
# where in the mode loop we get started
mode = 0
counter = 0
last_mode = 1
while True:
    # print only on change
    if mode != last_mode:
        print('mode=', mode, 'running program', mode_list[mode])
        last_mode = mode
    # 'green fade-in-and-out', 'moving green dot', 'green theater chase', 'green theater chase backwards',
    #         'green commet', 'random green and orange', 'random greens', 'green bounce',
    #         'rainbow cycle', 'green cylon scanner'
    if mode == 0:
        moving_rainbow(counter, .04)
    elif mode == 1:
        solid_color(red, .05)
    elif mode == 2:
        solid_color(white, .05)
    elif mode == 2:
        solid_color(blue, .05)
        
    elif mode == 3:  
        comet_tail(counter, red, .05)
    elif mode == 4:
        comet_tail(counter, white, .05)
    elif mode == 5: 
        comet_tail(counter, blue, .05)
    
    elif mode == 6:  
        running_lights(counter, red, 4, .1)
    elif mode == 7: 
        running_lights(counter, white, 4, .1)
    elif mode == 8: 
        running_lights_rev(counter, blue, 4, .1)
    
    elif mode == 9: 
        three_bands(counter, 3, red, white, blue, 0.04)
    elif mode == 10: 
        three_bands(counter, 4, red, white, blue, 0.04)
    elif mode == 11: 
        three_bands(counter, 5, red, white, blue, 0.04)
    
    elif mode == 12:
        move_dot(counter, red, 0.03)
    elif mode == 13:
        move_dot(counter, white, 0.03)        
    elif mode == 14:
        move_dot(counter, blue, 0.03)
    
    elif mode == 15: 
        rainbow_cycle(counter, .03)

    else:
        print('mode', mode, 'not configured')

    counter += 1
    # wrap the counter using modulo
    if counter > NUMBER_PIXELS -1 :
        counter = 0
        mode += 1
        if mode > mode_count - 1:
            mode = 0
