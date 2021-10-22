import machine
from utime import sleep

POT_PIN_1 = 26
POT_PIN_2 = 27
POT_PIN_3 = 28

adc_1 = machine.ADC(POT_PIN_1)
adc_2 = machine.ADC(POT_PIN_2)
adc_3 = machine.ADC(POT_PIN_3)

# return only the top 8 bits by sifting the 16 bit value right 8 bits
def read_pot(adc):
    return int(adc.read_u16()) >> 8

while True:
    print(read_pot(adc_1), read_pot(adc_2), read_pot(adc_3))
    sleep(.5)
    