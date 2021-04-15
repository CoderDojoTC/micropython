# Play Tones Using the PWM

Since we will be using the sleep function many times, we will import it by name from the Micropthon time library like this:

```python
from utime import sleep
```

Now, instead of putting ```utime.sleep(.5)``` we can just reference sleep directly like this:

```python
sleep(.5)
```

This will pause for 1/2 a second.  This is how long we wait for a tone to stay on or go off.  The nice thing about this menthod is that our code is a little smaller.  However, you can't run other functions in the utime library.  So if you want to add them later you will need to import them also, just like we did for the sleep function.

## Lab 1: Play A Single Tone

```python
from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))
# set the duty cycle to be 50%
speaker.duty_u16(1000)
speaker.freq(1000) # 50% on and off
sleep(1) # wait a second
speaker.duty_u16(0)
# turn off the PWM circuits off with a zero duty cycle
speaker.duty_u16(0)
```

!!! Note
    The tone will keep sounding until you turn the speaker duty to 0.  This shows you that the circuitry that is generating the sound is independent of the main CPU.

## Experiments

1. Try changing the frequency for the first lab.  This is the line ```speaker.freq(1000)``` and rerunning the program.  Try using values from 10 to 10000.  What values seem the loudest to your ear?
2. What happens if you comment out the last line that sets the duty cycle to be 0?  Make sure to set it back to zero again or the tone will continue playing until the device is powered off.