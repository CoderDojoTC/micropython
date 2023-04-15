# spin foward slow to fast
from machine import Pin, PWM
from time import sleep

# this is the built-in LED on the Pico W
led = Pin('LED', Pin.OUT)

FORWARD_PIN = 16
#REVERSE_PIN = 17

MAX_POWER = 65025

forward = PWM(Pin(FORWARD_PIN))
#reverse = PWM(Pin(REVERSE_PIN))

delay = .05
def main():
    while True:
        for i in range(0,  MAX_POWER, 1024):
            forward.duty_u16(i)
            print(i)
            led.toggle()
            sleep(delay)
        for i in range(MAX_POWER, 0, -1024):     
            forward.duty_u16(i)
            print(i)
            led.toggle()
            sleep(delay)
try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    forward.duty_u16(0)
    #reverse.duty_u16(0)