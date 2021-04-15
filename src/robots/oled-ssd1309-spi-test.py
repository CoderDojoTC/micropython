from machine import Pin
import ssd1306
import utime

WIDTH  = 128
HEIGHT = 64

# default is data on GP7 and clock on GP6


CS = machine.Pin(1)
SCL = machine.Pin(2)
SDA = machine.Pin(3)
DC = machine.Pin(4)
RES = machine.Pin(5)
spi=machine.SPI(0, sck=SCL, mosi=SDA)
print(spi)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

oled.fill(0)
oled.text("CoderDojo Rocks!", 0, 0, 1)
oled.text("MicroPython Robt", 0, 10, 1)
oled.text("128X64 OLED", 0, 20, 1)
oled.text("L293 Motor Drive", 0, 30, 1)
oled.text("3 IR Dist Sensors", 0, 40, 1)
oled.text("$25", 0, 50, 1)
oled.show()
