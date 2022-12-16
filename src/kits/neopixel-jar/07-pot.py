from machine import ADC
from utime import sleep
pot = ADC(26) 
while True:
    # shift the reading 8 bits to the right
    val = pot.read_u16() >> 8
    print(val)
    sleep(.2)