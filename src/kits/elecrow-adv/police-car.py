from utime import sleep
from machine import Pin,PWM
Led_R = PWM(Pin(4))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(2))
buzzer = PWM(Pin(15))
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)
buzzer.duty_u16(1000)

def main():
    while True:
        buzzer.freq(750)
        Led_R.duty_u16(0)
        Led_G.duty_u16(0)
        Led_B.duty_u16(65535)
        sleep(.23)
        buzzer.freq(1550)
        Led_R.duty_u16(65535)
        Led_G.duty_u16(0)
        Led_B.duty_u16(0)
        sleep(.1)

try:
    main()
except KeyboardInterrupt:
    buzzer.duty_u16(0)
    print("sound off")