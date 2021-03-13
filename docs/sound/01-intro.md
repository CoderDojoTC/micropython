# Introduction to Sound and Music in MicroPython

## How Microcontrollers Generate Sound

Microcontrollers are really great at generating digital outputs on their GPIO pins.  These digital signals that quickly switch between zero and a positive voltage like 3.3 or 5 volts.  However, they are not designed to create "analog" output of a continuous varying voltage.  However, we can use a technique called "Pulse Width Modulation" to simulate the various frequencies of sound using digital only outputs.

[Pulse Width Modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation) is the process of changing not the height of a electrical signal, but the width between the pulses of digital signals.  By changing the distance of the spaces between the digital signals we can generate a signal that will sound like it has a higher or lower frequency or pitch.

MicroPython provides a powerful library of tools for you to easily generate pulses of different shapes.  This is called the PWM library.  Will will use this in our sound and music programs.  Here is a sample of how this is called in our code:

```py
from machine import Pin, PWM
from utime import sleep
```

Note that we will also need to pause between notes, so will use the sleep library to pause execution of our sound generation.

## Connecting a Sound Device

There are several different ways that you can connect a sound device to you MicroController.  Here are three options:

1. A **Buzzer** - t