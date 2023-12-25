from machine import Pin, Timer, PWM, ADC
from utime import sleep
import ssd1306

# this is the built-in LED on the Pico W
led = Pin('LED', Pin.OUT)

FORWARD_PIN = 18
REVERSE_PIN = 19

MAX_POWER = 65025

forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))
# these are often not needed
forward.freq(50) # 50 hertz
reverse.freq(50) # 50 hertz

# turn both motors off
forward.duty_u16(0)
reverse.duty_u16(0)

# ADC0 is GPIO 26.  Connect to row 10 the right side.
pot = ADC(26)

# global variables

# how often to read the pot and update the display 20 times per second
delay = .05

WIDTH = 128
HEIGHT = 64
SCK=machine.Pin(2)
SDL=machine.Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDL)

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

counter = 0
def main():
    global counter
    while True:
        pot_value = pot.read_u16() # read the 8 bit value from the pot
        forward.duty_u16(pot_value)
        print("pot_value:", delay)
        high_bits = pot_value >> 9
        # print("delay:", high_bits)
        update_display(counter, pot_value, high_bits)
        led.toggle()
        sleep(delay)
        counter += 1

# brief startup test
# forward.duty_u16(MAX_POWER)
# sleep(1)
# forward.duty_u16(0)

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    forward.duty_u16(0)
    reverse.duty_u16(0)