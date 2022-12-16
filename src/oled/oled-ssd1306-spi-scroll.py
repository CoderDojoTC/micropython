import machine
import ssd1306
from time import sleep

WIDTH = 128
HEIGHT = 64
SCK=machine.Pin(2)
SDL=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDL)
CS = machine.Pin(0)
DC = machine.Pin(1)
RES = machine.Pin(4)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

counter = 0
print('dispaying text...')
while True:
    for i in range(HEIGHT - 10):
        oled.text(str(counter), 0, i, 1)
        for j in range(WIDTH):
            oled.scroll(1,0)
            oled.show()
        print(counter, '.', sep="", end="")
        counter += 1;
    
    

    
    