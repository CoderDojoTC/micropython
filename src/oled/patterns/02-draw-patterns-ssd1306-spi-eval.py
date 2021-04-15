import machine
import ssd1306
import time

WIDTH = 128
HEIGHT = 64
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

my_function = '((x-128) * 64) % (y-128)'

start = time.ticks_ms()

oled.fill(0) # clear display
for x in range(WIDTH):
    for y in range(1, HEIGHT):
        if eval(my_function):
           oled.pixel(x,y,0)
        else:
            oled.pixel(x,y,1)

end = time.ticks_ms()
duration = str(end - start)
oled.text(my_function, 0, 44, 1)
oled.text('ms:', 0, 54, 1)
oled.text(duration, 30, 54, 1)
oled.show()

print(duration, ' milliseconds')
print('done')
    