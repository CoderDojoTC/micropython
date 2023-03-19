import utime
from machine import Pin

# Sample two button Raspberry Pi Pico MicroPython example
# with a debounce delay value of 200ms in the interrupt handler
# https://www.coderdojotc.org/micropython/basics/03-button/

# these are the pins in the lower-left corner (USB on top)
BUTTON_PIN_A = 14
BUTTON_PIN_B = 15

button_presses = 0 # the count of times the button has been pressed.  A is +1, B is -1
last_time = 0 # the last time we pressed the button

# we toggle the builtin LED to get visual feedback
builtin_led = machine.Pin(25, Pin.OUT)

# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
button_a = machine.Pin(BUTTON_PIN_A, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(BUTTON_PIN_B, machine.Pin.IN, machine.Pin.PULL_DOWN)

# this is the interrupt callback handler
# get in and out quickly
def button_callback(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # print(pin)
        if '14' in str(pin):
            button_presses +=1
        else:
            button_presses -= 1
        last_time = new_time
    
# now we register the handler functions when either of the buttons is pressed
button_a.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_callback)
button_b.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_callback)

# This is for only printing when a new button press count value happens
old_presses = 0

print(button_presses)
while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        print(button_presses)
        builtin_led.toggle()
        old_presses = button_presses
