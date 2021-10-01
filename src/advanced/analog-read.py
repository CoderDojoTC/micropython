# Copied from awonak https://gist.github.com/awonak/aa49c9ac2f339a4e62fbf4beeb50546d
# good example of bit shifting to get rid of the 4 least significant bits

from machine import Pin, ADC, PWM
from utime import sleep_ms, ticks_add, ticks_diff
from math import sqrt
import time


#DROP_LEAST_SIG_BITS = False
#SMPS_MODE = False
##StdDev: StdDev: 150.8483 Spread: 656

#DROP_LEAST_SIG_BITS = True
#SMPS_MODE = False
##StdDev: 136.7275 Spread: 672

#DROP_LEAST_SIG_BITS = False
#SMPS_MODE = True
##StdDev: 37.1131 Spread: 208

#DROP_LEAST_SIG_BITS = True
#SMPS_MODE = True
##StdDev: 38.12705 Spread: 208


a0 = ADC(28)
g23 = Pin(23, Pin.OUT)

if SMPS_MODE:
    g23.value(1)
else:
    g23.value(0)

_shift = 4

samples = [a0.read_u16()] * 100
_min = 65535
_max = 0


def stdev(samples):
    mean = sum(samples) / len(samples)
    dev = [(x-mean) ** 2 for x in samples]
    return sqrt(sum(dev) / len(samples))


deadline = ticks_add(time.ticks_ms(), 1000*30)

while ticks_diff(deadline, time.ticks_ms()) > 0:
    r = a0.read_u16()
    if DROP_LEAST_SIG_BITS:
        r = (r >> _shift) << _shift
    samples.append(r)
    del samples[0]
    d = stdev(samples)
    _min = min(r, _min)
    _max = max(r, _max)
    s = (_max - _min)
    print("A0: {}\tStdDev: {}\t Spread: {}".format(r, d, s))
    sleep_ms(50)
