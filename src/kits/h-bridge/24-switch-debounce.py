# swith status with no debounce logic
from machine import Pin
from utime import sleep, ticks_ms

builtin_led = Pin(25)
# Upper left swith
UL_PIN = 2
LL_PIN = 3
UR_PIN = 14
LR_PIN = 13

ul_switch = Pin(UL_PIN, Pin.IN, Pin.PULL_UP)
ll_switch = Pin(LL_PIN, Pin.IN, Pin.PULL_UP)
ur_switch = Pin(UR_PIN, Pin.IN, Pin.PULL_UP)
lr_switch = Pin(LR_PIN, Pin.IN, Pin.PULL_UP)

# get current values as global variables
ul = ul_switch.value()
ll = ll_switch.value()
ur = ur_switch.value()
lr = lr_switch.value()

# old values
ul_old = 0
ll_old = 0
ur_old = 0
lr_old = 0

last_time = 0
switch_counter = 0
# this function gets called every time the button is pressed
def switch_changed_handler(pin):
    global last_time, switch_counter, ul, ll, ur, lr
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        if 'GPIO2' in str(pin):
            if ul == 0:
                ul = 1
            else: ul = 0
        if 'GPIO3' in str(pin):
            if ll == 0:
                ll = 1
            else: ll = 0
        if 'GPIO14' in str(pin):
            if ur == 0:
                ur = 1
            else: ur = 0
        if 'GPIO13' in str(pin):
            if lr == 0:
                lr = 1
            else: lr = 0
        switch_counter +=1
        last_time = new_time

# now we register the handler function when the button is pressed
# https://docs.micropython.org/en/latest/library/machine.Pin.html
ul_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)
ll_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)
ur_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)
lr_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)

old_switch_counter = 0
counter = 0
print('Startup:', ul, ll, ur, lr)
while True:
    # only print on change in the button_presses value
    if old_switch_counter != switch_counter:
        # print('Switch counter: ', switch_counter)
        old_switch_counter = switch_counter
    
    if ul != ul_old:
        if ul == 0:
            print("Upper Left = On")
        else: print("Upper Left = Off")
        builtin_led.toggle()
        ul_old = ul
        counter += 1
    
    if ll != ll_old:
        if ll == 0:
            print("Lower Left = On")
        else: print("Lower Left = Off")
        builtin_led.toggle()
        ll_old = ll
        counter += 1
    
    if ur != ur_old:
        if ur == 0:
            print("Upper Right = On")
        else: print("Upper Right = Off")
        builtin_led.toggle()
        ur_old = ur
        counter += 1
        
    if lr != lr_old:
        if lr == 0:
            print("Lower Right = On")
        else: print("Lower Right = Off")
        builtin_led.toggle()
        lr_old = lr
