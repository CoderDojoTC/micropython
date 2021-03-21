from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

def playtone(frequency):
    speaker.duty_u16(1000)
    speaker.freq(frequency)

def bequiet():
    speaker.duty_u16(0)

freq = 30

for i in range(64):
    print(freq)
    playtone(freq)
    sleep(0.3)
    freq = int(freq * 1.1)

speaker.duty_u16(0)