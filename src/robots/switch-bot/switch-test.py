from machine import Pin
from time import sleep

# GPIO is the internal built-in LED
led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)

# input on the lower left of the Pico using a built-in pull-down resistor to keep the value from floating
middle_switch = Pin(7, Pin.IN, Pin.PULL_DOWN) 
right_switch = Pin(28, Pin.IN, Pin.PULL_DOWN)
left_switch = Pin(27, Pin.IN, Pin.PULL_DOWN)


while True:
    if middle_switch.value(): # if the value changes
        led0.on()
        print('middle')
    else: led0.off()

    if right_switch.value(): # if the value changes
        led1.on()
        print('right')
    else: led1.off()
    
    if left_switch.value(): # if the value changes
        led2.on()
        print('left')
    else: led2.off()
    sleep(.1)