# Fade and LED in and Out 

In the prior Blink lab, we turned an LED on an off at different speeds.  But what if we want to slowly turn on our LED on and off?  In this lab we will show you how to dim your LED to any brightness level you want.

## Welcome to Pulse Width Modulation

![PWM Duty Cycle](../img/PWM-duty-cycle.png)

Although digital computers are good at quickly turning signals on and off, they don't really allow us to easily set an output to a given voltage level without complex circuits.  But there is an easier way to adjust the brightness of an LED!  We can quickly turn the signal to the LED on and off.  We can do this so quickly that you can't even see it flicker.  Controlling the amount of time a signal is on is all about controlling the width of the ON pulse.  That is why this is called Pulse Width Modulation or PWM for short.

With a PWM design there are two things we need to tell the microcontroller:

1. How often do you want a square wave to go on and off?
2. How wide should the on part of the pulse be (relative to the total width).  This is called the duty cycle.

The rate of change of the pulse is call the frequency.  You can set the frequency to be 1,000 changes per second, which is much faster than the human eye can detect.  This is done using the following line:

```py
pwm.freq(1000)
```

Note that we can slow the frequency way down and the dimming effect will still work.  As an experiment you can change the PWM frequency to around 20 and you will see a distinct flicker as the LED turns on.

Here is the sample program that will slowly dim the builtin LED that is on pin 25:

```
from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(1000)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)
	for duty in range(65025, 0, -1):
		pwm.duty_u16(duty)
		sleep(0.0001)
```

Note that the duty cycle starts at 0 (always off) and moves slowly up to 65,025 (always on).  It then does the reverse and slowly dims the LED and then repeats.  There is only a 1/10,000 of a delay between these changes so the LED will completely turn on in about six seconds before it starts to dim again.

## Suggested Exercises

1. Change the frequency from 1,000 to 500, 100, 50, 40, 30, 25, 20, and 10.  When can you just barley see it flicker?  What does this tell you about the human eye?
2. Can you add a delay so that the LED stays on at full brightness for one second before it starts to dim again?
3. Can you add a delay so that the LED is completely off for five seconds and then goes to full brightness and off in one second?
4. What lights in your home would you like to see slowly dim on and off?  How could you modify a light (safely) so that it slowly dimmed on and off.  Would PWM work with all lightbulb types such as tungsten filament bulbs that take a long time to heat up and cool down?
5. Can you hook up a set of red, green and blue LEDs program them to fade in and out to display all the colors of the rainbow (red, orange, yellow, green, blue, indigo and violet)?
6. When you stop the program does the LED stop changing brightness?  Does it retain the value that it had when you pressed the Stop function?  What does that tell you about how main CPU and the role of PWM?  Note that we will cover up doing "cleanup" events that stop all PWM activity in our [Interrupt Handlers Lab](../advanced-labs/02-interrupt-handlers.md)

## References

### Pulse With Modulation

1. [Wikipedia Article on Pulse With Modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation)