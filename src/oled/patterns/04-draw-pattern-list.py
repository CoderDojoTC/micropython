import machine
import ssd1306
from utime import sleep, time

WIDTH = 128
HEIGHT = 64
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

equations = ['(x * y) & 24', '(x * y) & 47', '(x * y) & 64', 'x & y', 'x % y', '(x % y) % 4', '40 % (x % y+1)']

while True:
    for eqn in range(0, len(equations)):
        start = time()

        oled.fill(0) # clear display
        oled.text('calculating', 0, 0, 1)
        oled.text(equations[eqn], 0, 10, 1)
        oled.show()
        for x in range(WIDTH):
            for y in range(1, HEIGHT):
                if eval(equations[eqn]):
                   oled.pixel(x,y,0)
                else:
                    oled.pixel(x,y,1)
        oled.show()
        sleep(5)

        end = time()
        duration = str(end - start)
        print(equations[eqn])
        print(duration, ' seconds')

oled.text('done', 0, 0, 1)
oled.show()
print('done')
    