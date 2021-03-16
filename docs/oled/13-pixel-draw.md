# Sample Pixel-Based Drawing Program

Code example provided by Jim Tannenbaum.

```py
from machine import Pin, SPI, ADC
import ssd1306
import time
 
# Takes an input number value and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def scaled(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((int(value) - istart) / (istop - istart)))
 
# Define the pins for SPI Clock and Transmit
spi_sck = Pin(2)
spi_tx = Pin(3)
spi = SPI(0, baudrate=100000, sck=spi_sck, mosi=spi_tx)
 
# Define the pins for Chip Select, DC (Command), and Reset
CS = Pin(1)
DC = Pin(4)
RES = Pin(5)
 
oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)
 
# Turn all pixels off
oled.fill(0)
oled.show()
 
# Provide info to user
oled.text('Etch-A-Sketch', 0, 0, 1)
oled.text('Hit the reset', 0, 20, 1)
oled.text('button to clear', 0, 30, 1)
oled.text('the screen', 0, 40, 1)
oled.show()
 
# Define the pin for the reset button
resetButton = Pin(14, Pin.IN, Pin.PULL_DOWN)
 
# Wait unti the user hits the button to clear the screen and start drawing
while resetButton.value() != 1:
    time.sleep(.25)
    
oled.fill(0)
oled.show()
 
# Define the Horizontal and Vertical inputs from the Rheostats
vert = ADC(26)
horiz = ADC(27)
 
# Calculate where to start the line
x = newX = scaled(vert.read_u16(), 0, 65536, 0, 128)
y = newY = scaled(horiz.read_u16(), 0, 65536, 0, 64)
 
# Loop forever
# Draw the line, look for a reset to clear the screen, and get the new end points for the line
while True:
    oled.line(x, y, newX, newY, 1)
    x = newX
    y = newY
    if resetButton.value():
        oled.fill(0)
    oled.show()
    time.sleep(.2)
    newX = scaled(vert.read_u16(), 0, 65536, 0, 128)
    newY = scaled(horiz.read_u16(), 0, 65536, 0, 64)
```