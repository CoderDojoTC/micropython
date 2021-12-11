from machine import ADC, Pin
from utime import sleep
from ssd1306 import SSD1306_I2C

WIDTH  = 128 # oled display width
HEIGHT = 32  # oled display height

sda=machine.Pin(16) # bus 0 data
scl=machine.Pin(17) # bus 0 clock

# should be 400000, 1000 prints some text
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# this is the built-in LED on the Pico
led = Pin(25, Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side
pot = ADC(26)

MAX_DELAY = .5 # seconds

# global variables
delay = 0

def update_display(pot_value, delay):
    oled.fill(0)
    oled.rect(0, 0, WIDTH, HEIGHT, 1)
    oled.fill_rect(1, 1, pot_value, HEIGHT - 1, 1)
    oled.text(str(pot_value), 1, 1, 0)
    oled.text(str(delay), 1, 10, 1)
    oled.text(str(delay), 1, 20, 0)
    oled.show()

# repeat forever
while True:
    pot_value = pot.read_u16() >> 9 # read the value from the pot
    delay = round(pot_value/128 * MAX_DELAY, 3)
    update_display(pot_value, delay)
    print("delay:", delay)
    if delay > 0:
        print("frequency (toggles per second):", 1/delay)
    led.high() # turn on the LED
    sleep(delay) # leave it on for 1/2 second
    led.low() # Turn off the LED
    sleep(delay) # leave it off for 1/2 second
