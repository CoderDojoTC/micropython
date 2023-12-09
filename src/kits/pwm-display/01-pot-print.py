from machine import Pin, ADC
from utime import sleep
POT_PIN = ADC(26)

while True:
    print(POT_PIN.read_u16())
    sleep(.1)