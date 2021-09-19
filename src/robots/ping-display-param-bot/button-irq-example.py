import machine
from utime import sleep, sleep_us, ticks_ms
# Micropython two button press handler lab
# Wire two momentary press buttons from pins 14 and 15 through the 3.3v rail
# The buttons will increment and decrement a function_value variable

# lower left on pico
UP_BUTTON_PIN = 14
DOWN_BUTTON_PIN = 15

# the lower right coner has a wire that goes throuh 3.3v
up_irq = machine.Pin(UP_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
down_irq = machine.Pin(DOWN_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

function_value = 0

last_time = 0
# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global function_value, last_time
    new_time = ticks_ms()
    # print(pin)
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        if '14' in str(pin):
            function_value +=1
        else:
            function_value -=1
        last_time = new_time

# now we register the handler function when the button is pressed
up_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
down_irq.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

print('Running two button button press handeler lab')
current_function_value = function_value
while True:
    # only print on change
    if current_function_value != function_value:
        print('function vale:', function_value)
        current_function_value = function_value