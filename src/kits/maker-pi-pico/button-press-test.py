import utime
from machine import Pin

# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler

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
    new_time = utime.ticks_ms()
    pin_string = str(pin)
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in pin_string:
            prog_mode += 1
            if prog_mode > 5:
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