from machine import PWM, Pin, ADC
from utime import sleep

# this is the built-in LED on the Pico
led = Pin(25, Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side
pot = ADC(26)

# Motor Setup
# motors just barely turn at this power level
MAX = 65025
# lower right pins with USB on top
FOR_PIN = 16
REV_PIN = 17


forward = PWM(Pin(FOR_PIN))
reverse = PWM(Pin(REV_PIN))
forward.freq(50)
reverse.freq(50)

while True:
    pot_value = pot.read_u16()
    print('pot value:', pot_value)
    forward.duty_u16(pot_value)
    reverse.duty_u16(0)
    sleep(.1)
    
