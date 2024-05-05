import machine
import utime
from machine import Pin, ADC, SPI
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

min=64000
def plot_signal():
    global min
    display.fill(0) # Clear the display
    old_x = 0
    old_y = HEIGHT // 2

    # For simplicity, we're plotting every other pixel
    for x in range(0, WIDTH):
        # Read from ADC (values will be from 0 to 4095)
        val = adc.read_u16()
        if val < min:
            min = val
        # print(val-min)
        # Scale the ADC value to fit the OLED height
        y = int(((val-min) / 500) * HEIGHT)
        # Invert y to plot correctly on the OLED
        y = HEIGHT - y
        # Draw a line from the last point to the new point
        display.line(old_x, old_y, x, y, 1)
        old_x, old_y = x, y

    display.show() # Update the display with the new data

while True:
    plot_signal()
    utime.sleep(0.1) # Small delay to reduce flickering

