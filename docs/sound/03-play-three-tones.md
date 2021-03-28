# Play Three Tones
In this lesson we will play three consecutive tones.  Each tone will have a specific time on and we will put a time between the tones.

```python
from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

speaker.duty_u16(1000)
speaker.freq(300) # 1 Kilohertz
sleep(.5) # wait a 1/4 second
speaker.duty_u16(0)
sleep(.25)

speaker.duty_u16(1000)
speaker.freq(800)
sleep(.5)
speaker.duty_u16(0)
sleep(.25)

speaker.duty_u16(1000)
speaker.freq(400)
sleep(.5)

# turn off the PWM 
speaker.duty_u16(0)
```

## Using Variables

We can also put the time each tone stays on and the space between the tones into variables so it is easier to modify the values in a single place.

```python
# set the time each tone will be on
ONTIME = .5
# the time between the tones
OFFTIME = .100
```

## Three Tones With Variables

```python
from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

# the time each tone will be on
ON_TIME = .25
# the time between the tones
OFF_TIME = .1

# Low tone
speaker.duty_u16(1000)
speaker.freq(300)
sleep(ON_TIME)
speaker.duty_u16(0)
sleep(OFF_TIME)

# High tone
speaker.duty_u16(1000)
speaker.freq(800)
sleep(ON_TIME)
speaker.duty_u16(0)
sleep(OFF_TIME)

# Medium tone
speaker.duty_u16(1000)
speaker.freq(400)
sleep(ON_TIME)

# turn off the PWM 
speaker.duty_u16(0)
```

## Experiments

1. Change the ON_TIME in the above program.  What is the shortest time that you can still hear?
2. Change the order of the Low, High, Medium around.  What is the most pleasing to your ears?
3. What order would you suggest for the start of a game and what order would you like for a "Game Over" sound?