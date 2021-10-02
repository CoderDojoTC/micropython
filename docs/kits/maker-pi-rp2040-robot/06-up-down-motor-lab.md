# Up Down Motor Speed Lab

In this lab, we will make the motor speed change as the mode changes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/32BwKwWviZs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```py
# Motor Setup
# motors just barely turn at this power level
MIN_POWER_LEVEL = 10000
MAX_POWER_LEVEL = 65025
POWER_STEP = int((MAX_POWER_LEVEL - MIN_POWER_LEVEL) / 10)
# lower right pins with USB on top
RIGHT_FORWARD_PIN = 8
RIGHT_REVERSE_PIN = 9
LEFT_FORWARD_PIN = 11
LEFT_REVERSE_PIN = 10

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

def drive_speed(power_level):
    right_forward.duty_u16(power_level)
    left_forward.duty_u16(power_level)
```

In the main we have:

```py
power_level = MIN_POWER_LEVEL + mode * POWER_STEP
# turn off the motor if we are at mode 0
if mode == 0: power_level = 0
drive_speed(power_level)
```

## Full Program

```py
# Mode Up/Down Lab
# Change a mode using the buttons on the Maker Pi RP2040 board
# Changes the NeoPixel color and the blue GPIO status LEDs
import time
from machine import Pin, PWM
# We are using a MicroPython NeoPixel library from here: https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

BUZZER_PORT = 22
buzzer = PWM(Pin(BUZZER_PORT))

NUMBER_PIXELS = 2
STATE_MACHINE = 0
NEOPIXEL_PIN = 18

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, NEOPIXEL_PIN, "GRB")

# have up to 13 that we can use
blue_led_pins = [0,1,2,3,4,5,6,7,16,17,26,27,28]
number_leds = len(blue_led_pins)
led_ports = []
# create a list of the port pin object instances
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

# Color RGB values as tuples - needs some Gamma corrections
red = (255, 0, 0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
cyan = (0, 255, 255)
lightgreen = (100, 255, 100)
white = (128, 128, 128) # not too bright
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'cyan', 'lightgreen', 'white')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet, cyan, lightgreen, white)

# set to be 1 to 100 for percent brightness
strip.brightness(100)

# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler

# Motor Setup
# motors just barely turn at this power level
MIN_POWER_LEVEL = 10000
MAX_POWER_LEVEL = 65025
POWER_STEP = int((MAX_POWER_LEVEL - MIN_POWER_LEVEL) / 10)
# lower right pins with USB on top
RIGHT_FORWARD_PIN = 8
RIGHT_REVERSE_PIN = 9
LEFT_FORWARD_PIN = 11
LEFT_REVERSE_PIN = 10

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

def drive_speed(power_level):
    right_forward.duty_u16(power_level)
    left_forward.duty_u16(power_level)

mode = 0 # the default mode on powerup and reset
mode_count = len(color_names)
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# Give our pins some logical names
next_mode_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
previous_mode_pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global mode, last_time, power_level
    new_time = time.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in str(pin):
            mode +=1
            # power_level += POWER_STEP
        else:
            mode -=1
            # power_level -= POWER_STEP
        # wrap around to first mode
        if mode >= mode_count: mode = 0
        if mode < 0: mode = mode_count - 1
        last_time = new_time

def set_blue_led_mode(mode):
    global num_colors
    for i in range(0, num_colors):
        if i == mode:
            led_ports[i].high()
        else:
            led_ports[i].low()

# Register the handler function when either button is pressed
next_mode_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
previous_mode_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# non-linear increase is frequency - note that some are lowder
tone_freq = [100, 150, 210, 280, 350, 450, 580, 750, 850, 950, 1000]
def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
    
# This is for only printing when a new button press count value happens
old_mode = -1

power_level = MIN_POWER_LEVEL
print('found ', mode_count, ' modes.')
while True:
    # only print on change in the button_presses value
    if mode != old_mode:
        print('new mode:', mode, color_names[mode], tone_freq[mode], power_level)
        # get the color mode
        color = colors[mode]
        strip.set_pixel(0, color)
        strip.set_pixel(1, color)
        strip.show()
        set_blue_led_mode(mode)
        playtone(tone_freq[mode])
        time.sleep(.2)
        bequiet()
        power_level = MIN_POWER_LEVEL + mode * POWER_STEP
        # turn off the motor if we are at mode 0
        if mode == 0: power_level = 0
        drive_speed(power_level)
        old_mode = mode
```