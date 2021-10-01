# press buttons to change the color of the NeoPixels
import utime
from machine import Pin
from neopixel import Neopixel

NUMBER_PIXELS = 2
STATE_MACHINE = 0
LED_PIN = 18
BUTTON_A_PIN = 20
BUTTON_B_PIN = 21
# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler
# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

# Color RGB values
red = (255, 0, 0)
orange = (125, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
white = (255, 255, 255)
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'indigo', 'violet', 'white')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, white)

# color index into colors list
neopixel_a = 0
neopixel_b = 0
# set to be 1 to 100 for percent brightness
strip.brightness(100)

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
button_a = machine.Pin(BUTTON_A_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(BUTTON_B_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global button_presses, last_time, num_colors, neopixel_a, neopixel_b
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        button_presses += 1
        if '20' in str(pin):
            neopixel_a +=1
            if neopixel_a > num_colors - 1:
                neopixel_a = 0 
        else:
            neopixel_b +=1
            if neopixel_b > num_colors - 1:
                neopixel_b = 0 
        last_time = new_time
    
# now we register the handler function when the button is pressed
button_a.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
button_b.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# This is for only printing when a new button press count value happens
old_presses = 0
print('Running NeoPixel Button Lab')
strip.set_pixel(0, (4,5,5))
strip.set_pixel(1, (4,5,5))
strip.show()

def main():
    global button_presses, old_presses, colors, neopixel_a, neopixel_b
    while True:
        # only print on change in the button_presses value
        if button_presses != old_presses:
            print(button_presses)
            print('NeoPixel A:', color_names[neopixel_a], 'index:', neopixel_a)
            print('NeoPixel B:', color_names[neopixel_b], 'index:', neopixel_b)
            strip.set_pixel(0, colors[neopixel_a])
            strip.set_pixel(1, colors[neopixel_b])
            strip.show()
            old_presses = button_presses

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Cleanup code
    print('Turning off NeoPixels')
    strip.set_pixel(0, (0,0,0))
    strip.set_pixel(1, (0,0,0))
    strip.show()
