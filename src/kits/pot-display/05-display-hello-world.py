# Display Test
# Pin order GND, VCC, Clock, Data, Reset, DC, CS
from machine import Pin
import ssd1306
from utime import sleep

WIDTH  = 128
HEIGHT = 64

SCL = machine.Pin(2)
SDA = machine.Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)
spi=machine.SPI(0, sck=SCL, mosi=SDA)
# print(spi)

display = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

counter = 0
while True:
    display.fill(0)
    display.text('Hello World!', 0, 0)
    display.text(str(counter), 0, 10)
    display.show()
    sleep(.5)
    counter += 1
    
