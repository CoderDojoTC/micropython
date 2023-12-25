from machine import Pin
from rotary import Rotary
from utime import sleep, ticks_ms
from neopixel import NeoPixel
import ssd1306


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
mode_names = ['moving dot', 'moving hole', 'swipe', 'theater chase', 'moving rainbow']

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


WIDTH  = 128
HEIGHT = 64

# default is data on GP7 and clock on GP6

CS = machine.Pin(6)
SCL = machine.Pin(2)
SDA = machine.Pin(3)
DC = machine.Pin(5)
RES = machine.Pin(4)
spi=machine.SPI(0, sck=SCL, mosi=SDA)
# print(spi)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS) # Init oled display

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
color_index = 0
color = red
colors =      (red,    orange,   yellow,   green,   blue,   cyan,   indigo,   violet,   white)
color_names = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'indigo', 'violet', 'white']
color_count = len(colors)

mode_names = ['dot', 'hole', 'less than', 'theater chase', 'moving rainbow']

# this function is called whenever the rotory is changed
def rotary_changed(change):
    global val, button_press, color_index, color
    if change == Rotary.ROT_CW:
        val = val + 1
    elif change == Rotary.ROT_CCW:
        val = val - 1      
    elif change == Rotary.SW_PRESS:
        print('Rotary knob pressed')
        # button_press = 1
    elif change == Rotary.SW_RELEASE:
        print('Rotary knob released')
        color_index += 1
        color_index = color_index % color_count
        color = colors[color_index]
    val = val % NUMBER_PIXELS
    print(val) 
    
rotary.add_handler(rotary_changed)

def update_display(color, pattern, index):
    oled.fill(0)
    oled.text('Color:', 0, 0)
    oled.text(str(color), 10, 11)
    oled.text('Pattern:', 0, 22)
    oled.text(str(pattern), 10, 33)
    oled.text('Index:', 0, 44)
    oled.text(str(index), 10, 55)
    oled.show() 


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
    color_name = color_names[color_index]
    mode_name = mode_names[mode]
    update_display(color_name, mode_name, val)
    