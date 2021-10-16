# Eight Key Piano

In this lab we wire up eight momentary press buttons so that when each one is pressed it will play a different note.

To do this you will need:

1. A Raspberry Pi Pico
2. A standard size breadboard or two 1/2 breadboards
3. 8 momentary press buttons
4. A speaker or a [Piezo buzzer](https://en.wikipedia.org/wiki/Piezoelectric_speaker)
5. An optional sound amplifier

## The Play Tone Functions

We will use two Python functions, one for playing a tone of a given frequency and one for turning off the sound.

```py
def playtone(frequency):
    speaker.duty_u16(1000) # turn the PWM duty to 50%
    speaker.freq(frequency)
    builtin_led.high() # turn builtin LED on

def bequiet():
    speaker.duty_u16(0) # turn off the speaker PWM
    builtin_led.low() # turn builtin LED off
```

## Sample Code

```py
# play a tone durning button down
from machine import Pin, PWM
from utime import sleep, ticks_ms

SPEAKER_PIN = 22 # pass through a speaker and tie the other end to GND
speaker = PWM(Pin(SPEAKER_PIN))

builtin_led = machine.Pin(25, Pin.OUT)

# Connect these GP pins through a button to the +3.3 volt rail
button_pin_1 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_2 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_3 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_4 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_5 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_6 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_7 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin_8 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

def playtone(frequency):
    speaker.duty_u16(1000) # turn the PWM duty to 50%
    speaker.freq(frequency)
    builtin_led.high() # turn builtin LED on

def bequiet():
    speaker.duty_u16(0) # turn off the speaker PWM
    builtin_led.low() # turn builtin LED off

while True:
    if   button_pin_1.value() == 1:
        playtone(220) # A3
    elif button_pin_2.value() == 1:
        playtone(247) # B3
    elif button_pin_3.value() == 1:
        playtone(262) # C4
    elif button_pin_4.value() == 1:
        playtone(294) # D4
    elif button_pin_5.value() == 1:
        playtone(330) # E4
    elif button_pin_6.value() == 1:
        playtone(349) # F4
    elif button_pin_7.value() == 1:
        playtone(392) # G4
    elif button_pin_8.value() == 1:
        playtone(440) # A4
    else:
        bequiet()
```

## Sample Video