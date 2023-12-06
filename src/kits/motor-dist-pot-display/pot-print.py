from machine import Pin, Timer, PWM, ADC
from utime import sleep
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side.
pot = ADC(26)

def read_pot_u8():
    return pot.read_u16() >> 8

counter = 0
while True:
    pot_value = pot.read_u16() # read the 8 bit value from the pot
    print(pot_value)
    # print("pot_value:", delay)
    high_bits = pot_value >> 9
    led.toggle()
    sleep(.1)
    counter += 1