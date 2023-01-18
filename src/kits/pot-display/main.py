# Display Test
# Pin order GND, VCC, Clock, Data, Reset, DC, CS
from machine import Pin, ADC
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
display.fill(0)
display.text('running', 0, 10)
display.show()
sleep(.5)
display.fill(0)
display.show()

pot = ADC(26)

x=0
while True:
    # just get the top 6 bits 0-63
    pot_val = pot.read_u16() >> 10
    y = HEIGHT - pot_val - 1
    print(x,y)
    display.pixel(x, y, 1)
    display.show()
    if x > WIDTH - 3:
        display.scroll(-1, 0)
        # print('scrolling')
    else:
        x += 1
    sleep(.1)