# static rainbow 
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
PERCENT_COLOR_WHEEL = round(255/NUMBER_PIXELS)

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

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
        
while True:
    for i in range(0, NUMBER_PIXELS):
        color_index = round(i*PERCENT_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        strip[i] = color
        strip.write()
        sleep(.1) # time between pixel draws
    sleep(1) # time at the end of the rainbow draw
    erase()
