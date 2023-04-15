from machine import Pin
from rotary import Rotary
from neopixel import NeoPixel
from utime import sleep, ticks_ms

NEOPIXEL_PIN = 22
NUMBER_PIXELS = 24
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# GPIO Pins 16 and 17 are for the encoder pins. 22 is the button press switch.
# GPIO Pins 16 and 17 are for the encoder pins. 18 is the button press switch.
ENCODER_A = 16
ENCODER_B = 17
SWITCH = 18
rotary = Rotary(ENCODER_A, ENCODER_B, SWITCH)

brightness = 255
red = (brightness, 0, 0)
green = (0, brightness, 0)
blue = (0, 0, brightness)

# connect to one end of the button to this pin and the other to 3.3V
BUTTON_PIN = 15

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
button_pin = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
color_list = (RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)
current_color = 0
color_count = len(color_list)

last_time = 0
# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global current_color, last_time
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 100: 
        current_color += 1
        current_color = current_color % color_count
        draw_bar(val, width, color_list[current_color])
        last_time = new_time

# now we register the handler function when the button is pressed
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)


# value of the rotery encoder
val = 0
# width of the color band
width = 5

def rotary_changed(change):
    global val, width
    if change == Rotary.ROT_CW:
        val = val + 1
        val = val % NUMBER_PIXELS
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        val = val % NUMBER_PIXELS
        print(val)
    elif change == Rotary.SW_PRESS:
        width += 1
        width = width % 12
        draw_bar(val, width, color_list[current_color])
        print('new width:', width)
    elif change == Rotary.SW_RELEASE:
        pass
        # print('RELEASE')

rotary.add_handler(rotary_changed)

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

def draw_bar(start, width, color):
    global strip
    if start > 0:
        strip[start % NUMBER_PIXELS] = (0,0,0)
    end = start + width + 1
    for i in range(start+1, end):
        strip[i % NUMBER_PIXELS] = color
    if end < NUMBER_PIXELS:
        strip[end % NUMBER_PIXELS] = (0,0,0)
    strip.write()


current_val = 0
draw_bar(0, width, color_list[current_color], )
while True:
    # draw only on a change
    if val != current_val:
        print('drawing at', val, 'width=', width)
        draw_bar(val, width, color_list[current_color])
        current_val = val
