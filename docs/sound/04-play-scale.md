# Play a Scale
In this lesson, we will learn about how to automatically generate various pitches.  We will see that the spacing between lower pitches is different from the spacing between higher pitches.

Here is a program that plays a scale of notes from a starting frequency of 30 hertz to an upper frequency of around 10,000 hertz.  Note that

```python
from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

def playtone(frequency):
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    sleep(0.3)

def bequiet():
    speaker.duty_u16(0)

freq = 30

for i in range(64):
    print(freq)
    playtone(freq)
    freq = int(freq * 1.1)

# Turn off the PWM
speaker.duty_u16(0)
```

## New Frequency Spacing

When you run the prior example, note the frequencies printed to the console.  Are they evenly spaced?

Take a close look at the line that creates a new frequency:

```python
freq = int(freq * 1.1)
```

The effect of this line is to create a new frequency that is 10% higher than the prior frequency.

## Experiments

1. What happens if you change the frequency update to be ```freq = freq +100```

