import machine
import ssd1306

WIDTH = 128
HEIGHT = 64

SCK=machine.Pin(2)
SDL=machine.Pin(3)

spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDL)

RES = machine.Pin(14)
DC = machine.Pin(15)
CS = machine.Pin(13)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

while True:
    for i in range(HEIGHT - 10):
        oled.text('Hello Dan', 0, i, 1)
        for j in range(WIDTH):
            oled.scroll(1,0)
            oled.show()

    
    