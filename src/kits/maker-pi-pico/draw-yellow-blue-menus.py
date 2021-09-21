import machine
from machine import Pin
from utime import sleep, ticks_ms
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

# Screen size
width=128
height=64
oled = SSD1306_I2C(width, height, i2c)

prog_mode = 0
mode_value = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led_1 = machine.Pin(16, Pin.OUT)
builtin_led_2 = machine.Pin(17, Pin.OUT)

# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
mode_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
up_pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
down_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global mode_value, prog_mode, last_time
    new_time = ticks_ms()
    pin_string = str(pin)
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in pin_string:
            prog_mode += 1
            if prog_mode > 4:
                prog_mode = 0
        elif '22' in pin_string:
            mode_value +=1
            if mode_value > 5:
                mode_value = 5
        elif '21' in pin_string:
            mode_value -= 1
            if mode_value < 0:
                mode_value = 0
        else:
            print('ERROR: unknown pin')
        last_time = new_time
    

# now we register the handler function when the button is pressed
mode_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
up_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
down_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# This is for only printing when a new button press count value happens
old_mode = 0
old_presses = 0

def update_display():  
    oled.fill(0)
    # draw yellow border in top 17 lines
    oled.rect(0, 0, width-1, 16, 1)
    # draw blue border from 18 to 64
    oled.rect(0, 17, width-1, height-17, 1)
    draw_mode()
    oled.show()

def draw_mode():
    global prog_mode
    bar_width = int(width/5)
    start = prog_mode * bar_width
    oled.fill_rect(start, 1, bar_width, 16, 1)
    oled.text(str(prog_mode), start, 1, 0)
    oled.text('Value', 1, 18, 1)
    oled.text(str(mode_value), 1, 30, 1)
        
print('Progam Mode:', prog_mode, 'Value:', mode_value)
while True:
    # only print on change in the mode_value value
    if mode_value != old_presses:
        print('val:', mode_value)
        builtin_led_1.toggle()
        old_presses = mode_value
    if prog_mode != old_mode:
        print('prog mode:', prog_mode)
        builtin_led_2.toggle()
        old_mode = prog_mode
    update_display()
