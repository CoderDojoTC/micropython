from machine import ADC, Pin, PWM
from time import sleep

EXTERNAL_LED_PIN = 18
ADC_PIN = 26

POT_PIN = ADC(ADC_PIN)
pwm = PWM(Pin(EXTERNAL_LED_PIN))

pwm.freq(50)

while True:
    potVal = POT_PIN.read_u16()
    pwm.duty_u16(potVal)
    sleep(0.01)



