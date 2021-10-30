from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
AUDIO_LEFT_PIN = 18
AUDIO_RIGHT_PIN = 19

# create a Pulse Width Modulation Object on this pin
left_speaker = PWM(Pin(AUDIO_LEFT_PIN))
# set the duty cycle to be 50%
left_speaker.duty_u16(1000)
left_speaker.freq(1000) # 50% on and off
sleep(1) # wait a second
left_speaker.duty_u16(0)
# turn off the PWM circuits off with a zero duty cycle
left_speaker.duty_u16(0)
sleep(1)

# create a Pulse Width Modulation Object on this pin
right_speaker = PWM(Pin(AUDIO_RIGHT_PIN))
# set the duty cycle to be 50%
right_speaker.duty_u16(1000)
right_speaker.freq(1000) # 50% on and off
sleep(1) # wait a second
right_speaker.duty_u16(0)
# turn off the PWM circuits off with a zero duty cycle
right_speaker.duty_u16(0)