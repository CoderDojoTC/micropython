from machine import ADC, Pin
from utime import sleep, ticks_ms
from neopixel import NeoPixel

NUMBER_PIXELS = 60
LED_PIN = 0
POT_PIN = 26
pot = ADC(POT_PIN)

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)
# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler

mode = 0 # the count of times the button has been pressed
colors = 15 # the number of colors we will show
color_step = 255 // colors # step around the color wheel
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper
# left and the lower right goes to the 3.3 rail
button_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 300: 
        mode +=1
        last_time = new_time
        if mode >= colors:
            mode = 0

# now we register the handler function when the button is pressed
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

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
# This is for only printing when a new button press count value happens

old_mode = 0
while True:
    # only print on change in the button_presses value
    current_color = wheel(int(mode * color_step))
    if mode != old_mode:
        print(mode, current_color)
        builtin_led.toggle()
        old_mode = mode
    pot_value = pot.read_u16() >> 10 # 0 to 64
    percent = pot_value / 64
    # print(pot_value, percent)
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (int(current_color[0]*percent), int(current_color[1]*percent), int(current_color[2]*percent))
    strip.write()
    sleep(.05)
        
