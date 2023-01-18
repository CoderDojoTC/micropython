# import MatrixBuffer

from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
ROWS = 8
COLS = 32
NUMBER_PIXELS = ROWS * COLS
# how many steps to get through the color wheel of 256 colors
COLOR_WHEEL_STEP = round(256/COLS)

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()

def write_pixel(x, y, value):
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottup
        if x % 2: 
            strip[(x+1)*ROWS - y - 1] = value             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            strip[x*ROWS + y] = value

def show():
    strip.write()

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

print('Color Wheel Step:', COLOR_WHEEL_STEP)
counter = 0
while True:
    for x in range(0, COLS):
        for y in range(0, ROWS):
            # * PERCENT_COLOR_WHEEL
            write_pixel(x, y, wheel((x*COLOR_WHEEL_STEP + y*COLOR_WHEEL_STEP - counter*8) % 256))
    strip.write()
    counter += 1
                   
    