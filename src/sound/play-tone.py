from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))
# set the duty cycle
speaker.duty_u16(1000)
speaker.freq(1000) # 1 Kilohertz
sleep(1) # wait a second
speaker.duty_u16(1000)
# turn off the PWM 
speaker.duty_u16(0)