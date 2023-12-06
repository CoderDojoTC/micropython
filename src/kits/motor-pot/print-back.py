from machine import PWM, Pin, ADC
from utime import sleep
led = Pin(25, Pin.OUT)
pot = ADC(26)
MAX = 65025
HALF = MAX // 2
FOR_PIN = 16
REV_PIN = 17
fwd = PWM(Pin(FOR_PIN))
rev = PWM(Pin(REV_PIN))
fwd.freq(50)
rev.freq(50)
while True:
    potVal = pot.read_u16()
    if pot_value > HALF:
        forward.duty_u16((potVal-HALF)*2)
        reverse.duty_u16(0)
    else:
        forward.duty_u16(0)
        reverse.duty_u16((HALF-potVal)*2)
    sleep(.1)
    led.toggle()
