import machine
from utime import sleep

# setup the first LED as an output signal
first_led = machine.Pin(0, machine.Pin.OUT)

while True:
    first_led.toggle()
    # wait for 1/2 second
    sleep(.5)