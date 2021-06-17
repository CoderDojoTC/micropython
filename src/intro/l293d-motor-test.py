from machine import Pin, PWM

import time
FORWARD_PIN = 16 # lower right corner
REVERSE_PIN = 17
POT_PIN = machine.ADC(26) # ADC0
MAX_POWER = 65025

forward_pwm = PWM(Pin(FORWARD_PIN))
reverse_pwm = PWM(Pin(REVERSE_PIN))

while True:
    val = POT_PIN.read_u16()
    print(val)
    forward_pwm.duty_u16(val)
    time.sleep(.1)