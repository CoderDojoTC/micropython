import utime
from machine import Pin

# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler

BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail

button1 = machine.Pin(BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This function gets called every time the button is pressed.  The parameter "pin" is used to tell
# which pin is used
def button_pressed_handler(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # print(pin)
        # this is a hack but I can't get the pin ID parameter without vars() or attr()
        pin_num = int(str(pin)[4:6])
        # this works as long as one of the buttons is this one
        if pin_num == BUTTON_PIN_1:
            button_presses +=1
        else:
            button_presses -=1
        last_time = new_time

# now we register the handler function when the button is pressed
button1.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
button2.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# This is for only printing when a new button press count value happens
old_presses = 0
while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        print(button_presses)
        builtin_led.toggle()
        old_presses = button_presses