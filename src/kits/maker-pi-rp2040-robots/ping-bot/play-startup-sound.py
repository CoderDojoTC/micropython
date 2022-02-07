from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 22

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

def sound_off():
    speaker.duty_u16(0)
    
def playtone(frequency):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    
def playnote(frequency, duration):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    sleep(duration)
    sound_off()
    
def rest(time):
    sound_off()
    sleep(time)
    
def play_startup():
    playnote(600, 0.2)
    rest(0.05)
    playnote(600, 0.2)
    rest(.05)
    playnote(600, 0.2)
    rest(0.1)
    playnote(800, 0.4)
    
def play_no_signal():
    playnote(300, 0.1)

def play_turn_right():
    playnote(500, 0.1)
    
def play_turn_left():
    playnote(700, 0.1)

play_startup()