from machine import Pin # get the Pin function from the machine module
from time import sleep # get the sleep library from the time module

leds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 19, 16]
pins = []
delay = .05

for i in range(0, len(leds)):
    print(i, leds[i])
    pins.append(machine.Pin(leds[i], machine.Pin.OUT))

while True:
    for i in range(0, len(leds)):
        pins[i].high()
        sleep(delay)
        pins[i].low()
        
    for i in range(len(leds)-1, 0, -1):
        pins[i].high()
        sleep(delay)
        pins[i].low()