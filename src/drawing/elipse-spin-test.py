from machine import Pin
from utime import sleep, ticks_us
from array import array
import framebuf
import ssd1306

WIDTH = 128
# bit shifting only works when the numbers are a power of 2
HALF_WIDTH = WIDTH >> 1
QUARTER_WIDTH = HALF_WIDTH >> 1
HEIGHT = 64
HALF_HEIGHT = HEIGHT >> 1
QUARTER_HEIGHT = HALF_HEIGHT >> 1
ONE_THIRD_HEIGHT = int(HEIGHT/3)

# draw readability
ON = 1
OFF = 0
NO_FILL = 0
FILL = 1

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# quadrant text

# 1 - upper right on
# 2 - upper left on
# 4 - lower left on
# 8 - lower right on

while True:
    index = 0
    for i in range(0, 4):
        index = 2**i
        oled.fill(0)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, HALF_WIDTH-1, HALF_HEIGHT-1, ON, FILL, index)
        oled.text(str(index), 0, 54, 1)
        oled.show()
        sleep(.05)