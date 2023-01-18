from machine import Pin
from utime import sleep, ticks_ms

# note these are out-of-order to keep the wiring looking pretty
pin_ids = [12,13,14,15,21,20,19,18,17,16]
pin_count = len(pin_ids)
pins = []
mode_names = ["dot up", "dot down", "swip up", "swipe down", "chase up", "chase down"]
mode_count = len(mode_names)

# Sample Raspberry Pi Pico MicroPython button press example with a debounce delay value of 200ms in the interrupt handler

mode = 0 # the count of times the button has been pressed


builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
button_pin = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)

for i in range(0, pin_count):
    pins.append(machine.Pin(pin_ids[i], machine.Pin.OUT))

last_time = 0 # the last time we pressed the button
# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    # if it has been more that 1/2 of a second since the last event, we have a new event
    if (new_time - last_time) > 500: 
        mode +=1
        # print('new mode', mode)
        last_time = new_time
    if mode >= mode_count:
        mode = 0

# now we register the handler function when the button is pressed
button_pin.irq(trigger=machine.Pin.IRQ_RISING, handler = button_pressed_handler)

old_mode = -1
delay = .1
print('found ', mode_count, 'modes')
while True:
    
    if mode >= mode_count:
        mode_count = 0
    if mode != old_mode:
        print('new mode:', mode)
        print(mode_names[mode])
        builtin_led.toggle()
        old_mode = mode
    
    # dot up
    if mode == 0:
        for i in range(0, pin_count):
            pins[i].on()
            sleep(delay)
            pins[i].off()
    # dot down
    elif mode == 1:
        for i in range(pin_count-1, -1, -1):
            pins[i].on()
            sleep(delay)
            pins[i].off()
    # swipe up
    elif mode == 2:
        for i in range(0, pin_count):
            pins[i].on()
            sleep(delay)
        for i in range(0, pin_count):
            pins[i].off()
    # swipe down
    elif mode == 3:
        for i in range(pin_count-1, -1, -1):
            pins[i].on()
            sleep(delay)
        for i in range(pin_count-1, -1, -1):
            pins[i].off()
    elif mode == 4:
        for i in range(0, 4):
            for j in range(0, pin_count-1, 3):
                if i+j < 10:
                    pins[i+j].on()
            sleep(delay)
            for i in range(0, pin_count):
                pins[i].off()
    elif mode == 5:
        for i in range(0, 4):
            for j in range(0, pin_count, 3):
                tmp = pin_count - (i+j)
                if tmp >= 0 and tmp < pin_count:
                    pins[tmp].on()
            sleep(delay)
            for i in range(0, pin_count):
                pins[i].off()
