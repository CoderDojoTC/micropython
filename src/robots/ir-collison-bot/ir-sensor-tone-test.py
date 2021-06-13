from machine import Pin, PWM
from utime import sleep


left = Pin(8, Pin.IN, Pin.PULL_DOWN)
center = Pin(7, Pin.IN, Pin.PULL_DOWN)
right = Pin(6, Pin.IN, Pin.PULL_DOWN)

SPEAKER_PIN = 21
# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

def sound_off():
    speaker.duty_u16(0)
    
def left_tone():
    speaker.duty_u16(1000)
    speaker.freq(300) # 1 Kilohertz
    sleep(.5) # wait a 1/4 second
    sound_off()

def center_tone():
    speaker.duty_u16(1000)
    speaker.freq(800)
    sleep(.5)
    sound_off()

def right_tone():
    speaker.duty_u16(1000)
    speaker.freq(400)
    sleep(.5)
    sound_off()
    
def right_tone():
    speaker.duty_u16(1000)
    speaker.freq(800)
    sleep(.25)
    sound_off()

def forward_tone():
    speaker.duty_u16(1000)
    speaker.freq(400)
    sleep(.1)
    speaker.freq(900)
    sleep(.1)
    speaker.freq(1200)
    sleep(.1)
    sound_off()

# 0=stopped, 1=forward, 2=turing right, 3=turning left
drive_state = 0
while True:
    if left.value()==0:
        print('Left')
        left_tone()
        drive_state = 2
    if center.value()==0:
        print('Center')
        center_tone()
        drive_state = 0
    if right.value()==0:
        print('Right')
        right_tone()
        drive_state = 3
        
    # if (left.value()==1) and (center.value()==1) and (right.value()==1):
    if left.value() and center.value() and right.value():
        print('Go forward!')
        drive_state = 1
        forward_tone()
    sleep(.25)