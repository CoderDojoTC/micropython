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
# 0 - all off
# 1 - upper right on
# 2 - upper left on
# 3 - top half on
# 4 - lower left on
# 5 - lower left and upper right on
# 6 - left side on
# 7 - lower right off - rest on
# 9 - right side on
# 10 - upper left and lower right are on
# 11 - all but lower left are on
# 12 - lower half on
# 13 - all but upper left are on
# 14 - all but upper right are on
# 15 - all four are on

while True:
    # x, y, major-axis, minor-axis
    for i in range(0, 16):
        oled.fill(0)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, HALF_WIDTH-1, HALF_HEIGHT-1, ON, FILL, i)
        oled.text(str(i), 0, 53, 1)
        oled.show()
        sleep(1)
    for i in range(0, 16):
        oled.fill(0)
        oled.ellipse(HALF_WIDTH, HALF_HEIGHT, HALF_WIDTH-1, HALF_HEIGHT-1, ON, NO_FILL, i)
        oled.text(str(i), 0, 53, 1)
        oled.show()
        sleep(1)