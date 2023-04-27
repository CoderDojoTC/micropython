from machine import Pin,ADC,PWM
from utime import sleep

photo = 0
LaserPin = 15
Led_R = PWM(Pin(11))
Led_G = PWM(Pin(12))
Led_B = PWM(Pin(13))
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)

def setup():
global Laser
global photo_ADC
photo_ADC = ADC(photo)
Laser = Pin(LaserPin,machine.Pin.OUT) Laser.value(0)

aim_time = 0

while True:
    Laser.value(1)
    Led_R.duty_u16(0)
    Led_G.duty_u16(65535)
    Led_B.duty_u16(0)
    print("time:",aim_time)
    sleep(0.1)
    aim_time += 0.1
    if photo_ADC.read_u16() < 15000:
        print("Aimed:",aim_time)
        aim_time = 0
        for i in range(10):
            Led_R.duty_u16(65535)
            Led_G.duty_u16(0)
            Led_B.duty_u16(0)
            sleep(0.1)
            Led_R.duty_u16(0)
    # Hit by a red laser, the light flashes
    # red light
    # blue light
    Led_G.duty_u16(0)
    Led_B.duty_u16(65535)
    sleep(0.1)
    sleep(2)
