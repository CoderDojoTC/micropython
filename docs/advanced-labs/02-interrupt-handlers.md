# Interrupt Handlers in MicroPython

## What is an Interrupt Handler?
An Interrupt Handler (also called an ISR) is a special Python function that is called when specific events occur such as a button being pressed.  ISR are the preferred way to detect external events, as opposed to polling methods that are inconsistent and inefficient.

Imagine you have 10 friends each with a button at their home.  In the polling method you would need to drive to each of their houses and ask them "did the button get pressed"?  You would have to do this frequently in case the button was pressed and released too quickly.  This is a slow and painful process and takes a lot of CPU cycles.

An interrupt handler 
## Simple Button Press Example

```py
# Use an interrupt function count the number of times a button has been pressed
from machine import Pin
import micropython
import time

# global value
button_pressed_count = 0

# Interrupt Service Routine for Button Pressed Events - with no debounce
def button1_pressed(change):
    global button_pressed_count
    button_pressed_count += 1

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button1.irq(handler=button1_pressed, trigger=Pin.IRQ_FALLING)

button_pressed_count_old = 0
while True:
    if button_pressed_count_old != button_pressed_count:
       print('Button 1 value:', button_pressed_count)
       button_pressed_count_old = button_pressed_count
```

## Debounce Version

In this example, our 

```py
import machine, utime

# the lower right coner has a wire that goes throuh
count_input = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
presses = 0

def count_handler(pin):
    global presses
    # disable the IRQ during our debounce check
    count_input.irq(handler=None)
    presses +=1
    # debounce time - we ignore any activity diring this period 
    utime.sleep_ms(200)
    # reenable the IRQ
    count_input.irq(trigger=machine.Pin.IRQ_FALLING, handler = count_handler)

count_input.irq(trigger=machine.Pin.IRQ_FALLING, handler = count_handler)

old_presses = 0
while True:
    # only print on change
    if presses != old_presses:
        if presses > old_presses + 1:
            print('double counting in irq.  Fixing...')
            presses = old_presses + 1
        print(presses)
        old_presses = presses
```
## References
[MicroPython Documentation on Interrupt Handlers](https://docs.micropython.org/en/latest/reference/isr_rules.html)