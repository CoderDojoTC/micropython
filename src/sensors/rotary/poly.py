from machine import Pin
from array import array
import ssd1306

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

oled.fill(0)
my_array = array('h', [30,10, 100,20, 50,60])
oled.poly(0,0, my_array, 1, 1)
oled.show()


