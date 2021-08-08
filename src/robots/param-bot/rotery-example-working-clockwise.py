# The MIT License (MIT)
# Copyright (c) 2021 Mike Teachman
# https://opensource.org/licenses/MIT
# https://raw.githubusercontent.com/miketeachman/micropython-rotary/master/Examples/example_simple.py
# example for MicroPython rotary encoder

import sys
if sys.platform == 'esp8266' or sys.platform == 'esp32':
    from rotary_irq_esp import RotaryIRQ
elif sys.platform == 'pyboard':
    from rotary_irq_pyb import RotaryIRQ
    print('found pyboard')
elif sys.platform == 'rp2':
    from rotary_irq_rp2 import RotaryIRQ
    print('found Raspberry Pico')
else:
    print('Warning:  The Rotary module has not been tested on this platform')

import time


r = RotaryIRQ(pin_num_clk=17,
              pin_num_dt=16,
              min_val=0,
              max_val=10,
              reverse=True,
              range_mode=RotaryIRQ.RANGE_WRAP)

val_old = r.value()
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)

    time.sleep_ms(50)
