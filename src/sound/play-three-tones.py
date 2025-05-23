from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 22

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

# the time each tone will be on
ON_TIME = .25
# the time between the tones
OFF_TIME = .1

speaker.duty_u16(1000)
speaker.freq(300)
sleep(ON_TIME)
speaker.duty_u16(0)
sleep(OFF_TIME)

speaker.duty_u16(1000)
speaker.freq(800)
sleep(ON_TIME)
speaker.duty_u16(0)
sleep(OFF_TIME)

speaker.duty_u16(1000)
speaker.freq(400)
sleep(ON_TIME)

# turn off the PWM 
speaker.duty_u16(0)