import machine
import ssd1306

WIDTH = 128
HEIGHT = 64
spi_sck=machine.Pin(17)
spi_tx=machine.Pin(16)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

while True:
    for i in range(HEIGHT - 10):
        oled.text('Hello Dan', 0, i, 1)
        for j in range(WIDTH):
            oled.scroll(1,0)
            oled.show()

    
    