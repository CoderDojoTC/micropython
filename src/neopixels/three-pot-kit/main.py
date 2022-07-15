% this kit assumes we have three POTs hooked to pins 26, 27 and 28 of the Picl
from machine import ADC, Pin
from utime import sleep
from neopixel import NeoPixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 12
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# this is the built-in LED on the Pico which we toggle on and off to show sampling
led = Pin(25, Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side
pot1 = ADC(26)
pot2 = ADC(27)
pot3 = ADC(28)

MAX_DELAY = .5 # seconds

# global variables
delay = .1

# repeat forever
while True:
    # we have the POTs wired backwards so we subtract to get the value
    pot_value1 = 255 - (pot1.read_u16() >> 8) # read the value from the pot and shift 6 bits
    pot_value2 = 255 - (pot2.read_u16() >> 8)
    pot_value3 = 255 - (pot3.read_u16() >> 8)
    print("pot_values:", pot_value1, pot_value2, pot_value3)
    
    # update the strip with our new values
    for i in range(NUMBER_PIXELS):
        strip[i] = (pot_value3, pot_value2, pot_value1)
    strip.write()
    
    sleep(delay)
    led.toggle()
