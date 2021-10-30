import machine
from utime import sleep
import ssd1306

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=200000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

counter = 0;
while True:
    oled.fill(0)
    oled.show()
    oled.text('CoderDojo Rocks!', 0, 0, 1)
    oled.text(str(counter), 0, 57, 1)
    oled.show()
    counter += 1;
    sleep(1)
    
