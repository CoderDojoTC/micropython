# Use an interrupt function count the number of times a button has been pressed
from machine import Pin
import micropython
import time

# global value
button_pressed_count = 0

# The built-in LED
builtin_led = Pin(25, Pin.OUT)
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Interrupt Service Routine for Button Pressed Events - with no debounce
def button1_pressed(change):
    global button_pressed_count
    change.disable_irq()
    change.delay(50)
    if button1.value():
         button_pressed_count += 1
    change.enable_irq()

button1.irq(handler=button1_pressed, trigger=Pin.IRQ_FALLING )

# | Pin.IRQ_RISING
# call the handler function when the value drops from 3.3 to 0 volts on the button pin
# button1.irq(handler=button1_pressed, trigger=Pin.IRQ_FALLING )

button_pressed_count_old = 0
while True:
    if button_pressed_count_old != button_pressed_count:
       print('Button 1 value:', button_pressed_count)
       builtin_led.toggle()
       button_pressed_count_old = button_pressed_count
       