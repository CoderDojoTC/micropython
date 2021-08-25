# Two Button Press

We learned how to write code to monitor a button press in the [Button Lab](../../intro/03-button.md).

Recall we talked about how to remove the noise when a button is pressed:

![Debounce Transition](../../img/debounce-transition.png)

We did this by waiting for the transition to settle down to its new state.

```py
import utime
from machine import Pin

# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
faster_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
slower_pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in str(pin):
            button_presses +=1
        else:
            button_presses -=1
        last_time = new_time
    

# now we register the handler function when the button is pressed
faster_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
slower_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# This is for only printing when a new button press count value happens
old_presses = 0

while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        print(button_presses)
        builtin_led.toggle()
        old_presses = button_presses
```