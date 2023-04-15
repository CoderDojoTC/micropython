from machine import Pin, PWM
from utime import sleep

RIGHT_SENSOR_PIN = 2
LEFT_SENSOR_PIN = 4

right_sensor = Pin(RIGHT_SENSOR_PIN)
left_sensor = Pin(LEFT_SENSOR_PIN)

# speaker pin on the Cytron Maker Pi RP2040
SPEAKER_PIN = 22
# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))
# set the duty cycle
speaker.duty_u16(1000)

while True:
    r = right_sensor.value()
    l = left_sensor.value()
    print("r", r, "l=", l, end='')
    if r == 0 and l == 1:
        print("right over white")
        speaker.duty_u16(1000)
        speaker.freq(400)
    elif l == 0 and r == 1:
        print("left over white")
        speaker.duty_u16(1000)
        speaker.freq(500)
    else:
        # turn the speaker off
        speaker.duty_u16(0)
        print(' f')
    sleep(.3)
    
