# import MatrixBuffer
import bitmapfont
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, sleep_ms, ticks_ms, ticks_diff

NEOPIXEL_PIN = 0
ROWS = 8
COLS = 32
NUMBER_PIXELS = ROWS * COLS
# how many steps to get through the color wheel of 256 colors
COLOR_WHEEL_STEP = round(256/COLS)

matrix = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Configuration:
DISPLAY_WIDTH  = 32      # Display width in pixels.
DISPLAY_HEIGHT = 8       # Display height in pixels.
SPEED          = 20.0    # Scroll speed in pixels per second
SPEED_MS = SPEED / 1000.0           # Scroll speed in pixels/ms

# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
def clear():
    for i in range(0, NUMBER_PIXELS):
        matrix[i] = (0,0,0)
    matrix.write()

def write_pixel(x, y, value):
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottup
        if x % 2: 
            matrix[(x+1)*ROWS - y - 1] = value             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            matrix[x*ROWS + y] = value

def show():
    matrix.write()

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

def rainbow_index(counter):
    for x in range(0, COLS):
        for y in range(0, ROWS):
            # * PERCENT_COLOR_WHEEL
            write_pixel_color_param(x, y, wheel((x*COLOR_WHEEL_STEP + y*COLOR_WHEEL_STEP - counter*8) % 256))
    matrix.write()

def rainbow_delay(delay):
    for i in range(0,DISPLAY_WIDTH):
        rainbow_index(i)
        sleep(delay/100)

def write_pixel_color(x, y):
    global font_color
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottup
        if x % 2: 
            matrix[(x+1)*ROWS - y - 1] = font_color             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            matrix[x*ROWS + y] = font_color

def write_pixel_color_param(x, y, font_color):
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottup
        if x % 2: 
            matrix[(x+1)*ROWS - y - 1] = font_color             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            matrix[x*ROWS + y] = font_color

def fill(val):
    for i in range(0, NUMBER_PIXELS):
        matrix[i] = val
        
def scroll_text(message, counter):

    with bitmapfont.BitmapFont(DISPLAY_WIDTH, DISPLAY_HEIGHT, write_pixel_color) as bf:
        # Global state:
        pos = DISPLAY_WIDTH                 # X position of the message start.
        message_width = bf.width(message)   # Message width in pixels.
        last = ticks_ms()             # Last frame millisecond tick time.
        
        # Main loop:
        for i in range(0, message_width):
            # Compute the time delta in milliseconds since the last frame.
            current = ticks_ms()
            delta_ms = ticks_diff(current, last)
            last = current
            # Compute position using speed and time delta.
            pos -= SPEED_MS*delta_ms
            if pos < -message_width:
                pos = DISPLAY_WIDTH
            # Clear the matrix and draw the text at the current position.
            fill((0,0,0))
            bf.text(message, int(pos), 0)
            # Update the matrix LEDs.
            show()
            # Sleep a bit to give USB mass storage some processing time (quirk
            # of SAMD21 firmware right now).
            sleep_ms(20)

counter = 0
font_color = (10,10,10)
while True:
    font_color = (255,0,0)
    #scroll_text('Code Savvy Rocks!', counter)
    font_color = (0,255,0)
    #scroll_text('Code Savvy Rocks!', counter)
    font_color = (0,0,255)
    scroll_text('Code Savvy Rocks!', counter)
    counter += 1
    rainbow_delay(1)
    print(counter)
    if counter > DISPLAY_WIDTH:
        counter = 0
    