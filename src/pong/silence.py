from machine import Pin, PWM

SPEAKER_PIN = 16
# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))
speaker.duty_u16(0)