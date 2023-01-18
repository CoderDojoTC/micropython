from machine import SPI, Pin
import max7219
from utime import sleep
CLOCK_PIN = 2
DATA_PIN = 3
CS_PIN = 4
spi=SPI(0,baudrate=10000000, polarity=1, phase=0, sck=Pin(CLOCK_PIN), mosi=Pin(DATA_PIN))

cs = Pin(CS_PIN, Pin.OUT)

display = max7219.Matrix8x8(spi, cs , 4)

counter = 0
while True:
    # right justify in a field of 4 spaces
    print('{:>4}'.format(counter))
    # string, x, y, ?
    display.text('{:>4}'.format(counter),0,1,1)
    display.show()
    sleep(.2)
    display.fill(0)
    counter += 1
