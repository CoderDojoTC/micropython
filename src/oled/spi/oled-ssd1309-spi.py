from machine import Pin
import ssd1306
import utime

WIDTH  = 128
HEIGHT = 64

# default is data on GP7 and clock on GP6
spi=machine.SPI(0)
print(spi)

CS = machine.Pin(3)
DC = machine.Pin(4)
RES = machine.Pin(5)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

while True:
    oled.fill(0)
    oled.text("Hello World!", 0, 0, 1)
    oled.show()
    oled.fill(1)
    oled.text("Hello World!", 0, 0, 0)
    oled.show()