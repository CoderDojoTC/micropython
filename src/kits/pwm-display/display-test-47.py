from machine import Pin
from utime import sleep
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)

WIDTH = 128
HEIGHT = 64
clock=Pin(2)
data=Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def update_display(counter):
    oled.fill(0)
    oled.text('Running', 0, 0)
    oled.text("Dan McCreary's", 0, 10)
    oled.text('Robot Lab 47', 0, 20)
    oled.text(str(counter), 0, 30)
    oled.show()

counter = 0
# repeat forever
while True:
    update_display(counter)
    led.toggle()
    sleep(.5)
    counter += 1