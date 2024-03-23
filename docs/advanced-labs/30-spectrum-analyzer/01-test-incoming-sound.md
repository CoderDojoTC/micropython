# Test Incoming Sound

## Prompt

```linenums="0"
OK, I now have a Raspberry Pi Pico and the OLED display hooked up.  I also have a microphone hooked up to ADC0 on port GPIO26.  How can I test that the signal is coming into the ADC?  Can you write a MicroPython program that displays the audio signal on the OLED?

I am using a ssd1306 and I use the following MicroPython:
```

```python
from machine import Pin
import ssd1306

WIDTH = 128
HEIGHT = 64

clock=Pin(2) #SCL
data=Pin(3) #SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
display = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)
# clear the display
display.fill(0)
# draw a diagonal line
display.line(0, 0, WIDTH, HEIGHT, 1)
```

## GPT-4 Reponse

To test that the signal is coming into the ADC (Analog-to-Digital Converter) on the Raspberry Pi Pico via GPIO26, and to display the audio signal on your SSD1306 OLED, you can use the following MicroPython script. This script will read the analog values from the microphone connected to GPIO26 and plot these values in real-time on the OLED display, creating a simple waveform visualization.

Note: Before running this script, ensure you have properly initialized and connected your microphone to GPIO26 (ADC0), and the OLED display is correctly wired for SPI communication as per your provided initialization.

```python
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

def plot_signal():
    display.fill(0) # Clear the display
    old_x = 0
    old_y = HEIGHT // 2

    # For simplicity, we're plotting every other pixel
    for x in range(0, WIDTH, 2):
        # Read from ADC (values will be from 0 to 4095)
        val = adc.read_u16()
        # Scale the ADC value to fit the OLED height
        y = int((val / 65535) * HEIGHT)
        # Invert y to plot correctly on the OLED
        y = HEIGHT - y
        # Draw a line from the last point to the new point
        display.line(old_x, old_y, x, y, 1)
        old_x, old_y = x, y

    display.show() # Update the display with the new data

while True:
    plot_signal()
    utime.sleep(0.1) # Small delay to reduce flickering
```

This script continuously reads the analog signal from the microphone and plots a simplified version of the waveform across the OLED display. Here's a breakdown of the plotting part:

-   The screen is cleared at the beginning of each frame with `display.fill(0)`.
-   We read a value from the ADC and scale it to fit the OLED's screen height.
-   We draw a line from the previous point to the current point to create a continuous waveform.
-   The display is updated with `display.show()` to visualize the waveform.

This example provides a basic way to visualize audio signals. The resolution and quality of the visualization can be further enhanced or adjusted according to your requirements.
