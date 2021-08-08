import machine, utime

# globals
button_presses = 0
last_time = 0 # the last time we pressed the button

# the lower right coner has a wire that goes throuh
count_input = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# this function gets called every time the button is pressed
def button_pressed_handler(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    if (new_time - last_time) > 200: # if it has been more that 1/5 of a second ago we have a new event
        button_presses +=1
        last_time = new_time

count_input.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

old_presses = 0
while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        print(button_presses)
        old_presses = button_presses