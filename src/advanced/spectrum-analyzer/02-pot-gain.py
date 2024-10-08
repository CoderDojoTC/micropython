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
