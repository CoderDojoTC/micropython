from machine import Pin
import ssd1306
import utime

WIDTH  = 128
HEIGHT = 64

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
oled.text("MicroPython", 0, 10, 1)
oled.text("128X64 OLED", 0, 20, 1)
oled.text("SPI SSD1306", 0, 30, 1)
oled.text("$4 + $17", 0, 40, 1)
oled.text("Dan McCreary", 0, 50, 1)
oled.show()

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.high()
    utime.sleep(0.5)
    led_onboard.low()
    utime.sleep(0.5)
