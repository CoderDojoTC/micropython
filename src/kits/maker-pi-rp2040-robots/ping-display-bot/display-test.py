from machine import Pin
from  ssd1306 import SSD1306_SPI

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)

spi=machine.SPI(0, sck=spi_sck, mosi=spi_tx)

CS = machine.Pin(13)
DC = machine.Pin(14)
RES = machine.Pin(15)
oled = SSD1306_SPI(128, 64, spi, DC, RES, CS)

oled.text('Hello World!', 0, 0, 1)
oled.show()
