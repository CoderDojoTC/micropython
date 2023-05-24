from machine import Pin
import time

# GPIO is the internal built-in LED.  It is an output pin.
led = Pin(25, Pin.OUT)
# The button is is an input and must have a pull up
button = Pin(24, Pin.IN, Pin.PULL_UP) 

while True:
    # the unpressed button.value() is normally high (True)
    if button.value():
        led.off()
    # when the button is pressed, value of the button is low (0) False we turn the LED on
    else:
        led.on()
        
