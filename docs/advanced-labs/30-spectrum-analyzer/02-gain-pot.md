# Adding A Gain Potentiometer.

## Prompt
The signal is very low on the display. I have added a Potentiometer on ADC1 which is on GPIO PIN 27. Can you please regenerate the entire program with sound on ADC0 and gain on ADC1. sound = ADC(Pin(26)) gain = ADC(Pin(27))


## ChatGPT-

Certainly! To adjust the signal's amplitude on the display based on the gain from a potentiometer connected to ADC1 (GPIO PIN 27), you can modify the program as follows. This updated script will use the value from the potentiometer to scale the audio signal from the microphone, making the waveform larger or smaller on the OLED display according to the potentiometer's position.

```python
import machine
import utime
from machine import Pin, ADC, SPI
import ssd1306

# OLED display width and height
WIDTH = 128
HEIGHT = 64

# SPI pins for OLED
clock = Pin(2)  # SCL
data = Pin(3)  # SDA
RES = Pin(4)
DC = Pin(5)
CS = Pin(6)

# Initialize SPI and OLED Display
spi = SPI(0, sck=clock, mosi=data)
display = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# Initialize ADC for sound input (GPIO26) and gain control (GPIO27)
sound = ADC(Pin(26))
gain = ADC(Pin(27))

def plot_signal_with_gain():
    display.fill(0)  # Clear the display
    old_x = 0
    old_y = HEIGHT // 2

    # Read gain control (potentiometer) value
    gain_value = gain.read_u16() + 1  # Adding 1 to avoid division by zero

    for x in range(0, WIDTH, 2):
        # Read from ADC (sound input)
        val = sound.read_u16()

        # Adjust the sound value based on the gain
        # Note: This scaling might need adjustment depending on your specific potentiometer and desired sensitivity
        adjusted_val = min(((val * gain_value) >> 16), 65535)  # Ensure the adjusted value does not exceed ADC's max value

        # Scale the adjusted value to fit the OLED height
        y = int((adjusted_val / 65535) * HEIGHT)
        # Invert y to plot correctly on the OLED
        y = HEIGHT - y
        # Draw a line from the last point to the new point
        display.line(old_x, old_y, x, y, 1)
        old_x, old_y = x, y

    display.show()  # Update the display with the new data

while True:
    plot_signal_with_gain()
    utime.sleep(0.1)  # Small delay to reduce flickering
```

In this script, the gain control (potentiometer) reading is used to adjust the amplitude of the sound signal before plotting it. The `gain_value` is read from ADC1 and is used to scale the audio signal from the microphone connected to ADC0. The line `adjusted_val = min(((val * gain_value) >> 16), 65535)` scales the microphone input based on the potentiometer's position, and the bit shift `>> 16` is used to keep the value within the 16-bit range of the ADC's output.

This method should help make the displayed signal more responsive to the potentiometer's adjustments, allowing you to visually enhance or reduce the waveform amplitude on the OLED display.