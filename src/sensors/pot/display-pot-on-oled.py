from machine import Pin, Timer, PWM, ADC
from utime import sleep
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side.
pot = ADC(26)

MAX_DELAY = .5 # seconds

# global variables
delay = 0

WIDTH = 128
HEIGHT = 64
WIDTH = 128
HEIGHT = 64
SCK=machine.Pin(2)
SDL=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDL)

RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)
oled.poweron()

def update_display(counter, pot_value, high_bits):
    oled.fill(0)
    oled.text('CoderDojo PotLab', 0, 0)
    oled.fill_rect(0, 10, high_bits, 20, 1)
    
    oled.text('ADC Value:', 0, 35)
    oled.text(str(pot_value), 80, 35)
    
    oled.text('Display Val:', 0, 45)
    oled.text(str(high_bits), 95, 45)
    
    oled.text('Counter:', 0, 54)
    oled.text(str(counter), 65, 54)
    oled.show()

# return the 8 most significant bits of the ADC
def read_pot_u8():
    return pot.read_u16() >> 8


counter = 0
while True:
    pot_value = pot.read_u16() # read the 8 bit value from the pot
    print(pot_value)
    # print("pot_value:", delay)
    high_bits = pot_value >> 9
    # print("delay:", high_bits)
    update_display(counter, pot_value, high_bits)
    led.toggle()
    sleep(.1)
    counter += 1