import machine
import utime
from machine import Pin, ADC, SPI
# https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
import ssd1306

# OLED display width and height
WIDTH = 128
HEIGHT = 64

# SPI pins for OLED
clock = Pin(2) # SCL
data = Pin(3) # SDA
RES = Pin(4)
DC = Pin(5)
CS = Pin(6)

# Initialize SPI and OLED Display
spi = SPI(0, sck=clock, mosi=data)
display = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# Initialize ADC for GPIO26 (ADC0)
adc = ADC(Pin(26))



def plot_signal(new_val, min):
    # Scroll the display content to the left by one pixel
    display.scroll(-1, 0)
    y = HEIGHT - new_val//4
    if y > HEIGHT:
        y = HEIGHT
    if y < 0:
        y = 0

    for clear_y in range(HEIGHT):
        display.pixel(WIDTH - 2, y, 1)

    # Update the display with the new data
    # display.fill_rect(0, 54, 100, 63, 0)
    # display.text(str(min), 0, 54, 1)
    # display.text(str(new_val), 0, 54, 1)
    display.show()

min = 53000
avg = 50
display.fill(0)
while True:
    
    # add up the ave number of points
    val=0
    for i in range(0,avg):
        val += (adc.read_u16() - min)
    avg_val = val//avg
    
    # if the average val is negative, lower the minimum by that amoun
    if avg_val < 0:
        min += avg_val
    
    plot_signal(avg_val, min)
    # utime.sleep(0.1) # Small delay to reduce flickering

