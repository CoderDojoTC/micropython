from machine import Pin
import ssd1306
import utime

WIDTH  = 128
HEIGHT = 64

# default is data on GP7 and clock on GP6

SCL = machine.Pin(2)
SDA = machine.Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=SCL, mosi=SDA)
print(spi)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

oled.fill(0)
oled.text("Dan McCreary", 0, 0, 1)
oled.text("MicroPython Robt", 0, 10, 1)
oled.text("264K RAM!", 0, 20, 1)
oled.text("128X64 OLED", 0, 28, 1)
oled.text("ssd1306 SPI", 0, 36, 1)
oled.text("$4 + $17 = $21", 0, 45, 1)
oled.text("Dan McCreary", 0, 54, 1)
oled.show()
