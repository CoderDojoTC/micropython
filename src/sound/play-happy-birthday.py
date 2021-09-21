from machine import Pin, PWM
from utime import sleep

# Speaker is on GP18 on the Cytron Maker Pi Pico board
SPEAKER_PIN = 18

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

def playnote(frequency, duration):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    sleep(duration/1000)
    speaker.duty_u16(0)

def rest(duration):
    speaker.duty_u16(0)
    sleep(duration/1000)
    
name = 'Ann'

print('Ha', end='')
playnote(264, 250)
rest(.25) # quarter second rest
print('ppy ', end='')
playnote(264, 250)
rest(.125)
print('birth', end='')
playnote(297, 1000)
rest(.125)
print('day ', end='')
playnote(264, 1000)
rest(.125)
print('to ', end='')
playnote(352, 1000)
rest(.125)
print('you')
playnote(330, 2000)
rest(.25)

print('Ha', end='')
playnote(264, 250)
rest(.25)
print('ppy ', end='')
playnote(264, 250)
rest(.125)
print('birth', end='')
playnote(297, 1000)
rest(.125)
print('day ', end='')
playnote(264, 1000)
rest(.125)
print('to ', end='')
playnote(396, 1000)
rest(.125)
print('you')
playnote(352, 2000)
rest(.25)

print('Ha', end='')
playnote(264, 250)
rest(.125)
print('ppy ', end='')
playnote(264, 500)
rest(250/1000.0)
print('birth', end='')
playnote(440, 1000)
rest(.125)
print('day ', end='')
playnote(352, 1000)
rest(.125)
print('dear ', end='')
playnote(330, 1000)
print(name)
rest(.125)
playnote(297, 1000)

playnote(440, 1000)
rest(.125)

rest(.25)
print('Ha', end='')
playnote(466, 250)
rest(.25)
print('ppy ', end='')
playnote(466, 250)
rest(.125)
print('birth', end='')
playnote(440, 1000)
rest(.125)
print('day ', end='')
playnote(352, 1000)
rest(.125)
print('to ', end='')
playnote(396, 1000)
rest(.125)
print('you')
playnote(352, 2000)
rest(.125)

# turn off
speaker.duty_u16(0)

print('HAPPY BIRTHDAY ' + name + ' <3')