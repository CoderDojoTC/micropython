from machine import Pin

builtin_led = Pin(25)
# Upper left swith
UL_PIN = 2
LL_PIN = 3
UR_PIN = 14
LR_PIN = 15

ul_switch = Pin(UL_PIN, Pin.IN, Pin.PULL_UP)
ll_switch = Pin(LL_PIN, Pin.IN, Pin.PULL_UP)
ur_switch = Pin(UR_PIN, Pin.IN, Pin.PULL_UP)
lr_switch = Pin(LR_PIN, Pin.IN, Pin.PULL_UP)

# old values
ul_val = 0
ll_val = 0
ur_val = 0
lr_val = 0
while True:
    # only print on change in the button_presses value
    
    new_ul_switch = ul_switch.value()
    if ul_val != new_ul_switch:
        if new_ul_switch == 0:
            print("Upper Right = On")
        else: print("Upper Right = Off")
        builtin_led.toggle()
        ul_val = new_ul_switch
    
    new_ll_switch = ll_switch.value()
    if ll_val != new_ll_switch:
        if new_ll_switch == 0:
            print("Lower Left = On")
        else: print("Lower Left = Off")
        builtin_led.toggle()
        ll_val = new_ll_switch
    
 
    new_ur_switch = ur_switch.value()
    if ur_val != new_ur_switch:
        if new_ur_switch == 0:
            print("Upper Right = On")
        else: print("Upper Right = Off")
        builtin_led.toggle()
        ur_val = new_ur_switch
        
    new_lr_switch = lr_switch.value()
    if lr_val != new_ll_switch:
        if new_lr_switch == 0:
            print("Lower Left = On")
        else: print("Lower Left = Off")
        builtin_led.toggle()
        ll_val = new_ll_switch        