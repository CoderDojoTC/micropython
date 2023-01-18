from machine import Pin, Timer
import ssd1306
from utime import sleep
import framebuf

WIDTH = 128
HEIGHT = 64
CS = machine.Pin(6)
DC = machine.Pin(5)
SCK=machine.Pin(2)
SDA=machine.Pin(3)
RES = machine.Pin(4)


spi=machine.SPI(0,sck=SCK, mosi=SDA)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

oled.poweron()
sleep(.1)
oled.init_display()
sleep(.1)

counter = 0
while True:
    oled.fill(0)
    
    for i in range(0,63,8):
        oled.hline(0, i, WIDTH, 1)
    oled.hline(0, 63, WIDTH, 1)
    
    for i in range(0,127,8):
        oled.vline(i, 0, HEIGHT, 1)
        
    oled.vline(127, 0, HEIGHT, 1)
    
    # clear the region to draw the counter in
    oled.fill_rect(9,9,40,11,0)
    oled.text(str(counter), 10, 11, 1)
    
    oled.show()
    sleep(.05)
    print(counter)
    counter += 1