# Rotary NeoPixel

This project has a rotary encoder and a button.  Spinning the rotary encoder changes the pixel index.  Pressing the knob of the encoder changes the color.   Pressing the button changes the pattern.

## Circuit

We connect the two ends of the rotary (A and B) to pins 14 and 15.  We connect the center pin to the 3.3v rail of the breadboard.

Next, we connect the rotary button and the other button to pins 16 and 17 and to the 3.3v rail.

All the buttons use PULL.DOWN option when they are configured.

## Sample Code

We use the rotary.py library

```py
from machine import Pin
from rotary import Rotary

ENCODER_A = 15
ENCODER_B = 14
SWITCH = 17
rotary = Rotary(ENCODER_A, ENCODER_B, SWITCH)
```

You can change the order of A and B to match the turn direction.

## Full Source Code

```py
from machine import Pin
from rotary import Rotary
from utime import sleep, ticks_ms
from neopixel import NeoPixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 12

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# GPIO Pins 16 and 17 are for the encoder pins. 18 is the button press switch.
ENCODER_A = 15
ENCODER_B = 14
SWITCH = 17
rotary = Rotary(ENCODER_A, ENCODER_B, SWITCH)

button_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
mode = 0 # mode to display
mode_names = ['dot', 'hole', 'compare', 'chase', 'rainbow']

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button
def button_pressed_handler(pin):
    global button_presses, last_time, mode
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200: 
        mode +=1
        last_time = new_time
    # make mode 0 or 1
    mode = mode % 5
    print('mode=', mode, mode_names[mode])
# now we register the handler function when the button is pressed
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

val = 0 # value of the LED strip index set by the rotary know

red = (255, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet)
color_count = len(colors)


# this function is called whenever the rotory is changed
def rotary_changed(change):
    global val, button_press, color_index
    if change == Rotary.ROT_CW:
        val = val + 1
    elif change == Rotary.ROT_CCW:
        val = val - 1      
    elif change == Rotary.SW_PRESS:
        print('PRESS')
        # button_press = 1
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')
        color_index += 1
        color_index = color_index % (color_count - 1)
    val = val % NUMBER_PIXELS
    print(val) 
    
rotary.add_handler(rotary_changed)

color_index = 0
color = red
while True:
    if mode == 0:
        for i in range(0, NUMBER_PIXELS):
            if i == val:
                strip[i] = color
            else:
                strip[i] = (0,0,0)
    elif mode == 1:
        for i in range(0, NUMBER_PIXELS):
            if i == val:
                strip[i] = (0,0,0)
            else:
                strip[i] = color
    elif mode == 2:
        for i in range(0, NUMBER_PIXELS):
            if i > val:
                strip[i] = (0,0,0)
            else:
                strip[i] = color
    elif mode == 3:
        for i in range(0, NUMBER_PIXELS):
            if (i-val) % 3:
                strip[i] = (0,0,0)
            else:
                strip[i] = color    
    elif mode == 4:
        # if the val + offset is larger than the number of pixels we need to do a modulo
        strip[val     % (NUMBER_PIXELS)] = violet
        strip[(val+1) % (NUMBER_PIXELS)] = indigo
        strip[(val+2) % (NUMBER_PIXELS)] = blue
        strip[(val+3) % (NUMBER_PIXELS)] = green
        strip[(val+4) % (NUMBER_PIXELS)] = yellow
        strip[(val+5) % (NUMBER_PIXELS)] = orange
        strip[(val+6) % (NUMBER_PIXELS)] = red
        # turn off the rest
        strip[(val+7) % (NUMBER_PIXELS)] = (0,0,0)
        strip[(val+8) % (NUMBER_PIXELS)] = (0,0,0)
        strip[(val+9) % (NUMBER_PIXELS)] = (0,0,0)
        strip[(val+10) % (NUMBER_PIXELS)] = (0,0,0)
        strip[(val+11) % (NUMBER_PIXELS)] = (0,0,0)
    strip.write()
    # print('color index', color_index)
    color = colors[color_index]
```
