# Display Scroll

## Prompt

```linenums="0"
The display is a bit slow. Can you rewrite the plot\_signal\_with\_gain function so that the scroll() function is used to move the display to the left by one pixel?
```

### ChatGPT GPT-4 Response

To make the display update faster and to create a scrolling effect that moves the waveform to the left by one pixel, you can modify the `plot_signal_with_gain` function to use the `scroll()` method of the SSD1306 library. This will shift the entire display content to the left by one pixel, and then you can plot the new data point at the right edge of the display. Here's how you can implement this:

```python
def plot_signal_with_gain():
    # Scroll the display content to the left by one pixel
    display.scroll(-1, 0)

    # Read gain control (potentiometer) value
    gain_value = gain.read_u16() + 1  # Adding 1 to avoid division by zero

    # Read from ADC (sound input)
    val = sound.read_u16()

    # Adjust the sound value based on the gain
    adjusted_val = min(((val * gain_value) >> 16), 65535)  # Ensure the adjusted value does not exceed ADC's max value

    # Scale the adjusted value to fit the OLED height
    y = int((adjusted_val / 65535) * HEIGHT)
    # Invert y to plot correctly on the OLED
    y = HEIGHT - y

    # Since we've scrolled, we only need to update the last column (x = WIDTH - 1)
    # Clear the last column first (optional, depending on the desired visual effect)
    for clear_y in range(HEIGHT):
        display.pixel(WIDTH - 1, clear_y, 0)

    # Draw the new data point at the right edge of the display
    display.pixel(WIDTH - 1, y, 1)

    # Update the display with the new data
    display.show()
```

In this updated function, the display is scrolled left by one pixel at the beginning of each update cycle using `display.scroll(-1, 0)`. This creates room to draw the new data point at the far right edge (`WIDTH - 1`) of the display. The loop that clears the last column before drawing the new point is optional and can be adjusted or removed depending on the visual effect you're aiming for.

Remember, while `scroll()` improves the visual fluidity by creating a continuous scrolling effect, the update rate can still be limited by the display's physical refresh rate and the speed at which your MicroPython script can run. Experiment with the `utime.sleep(0.1)` delay at the end of the main loop to find a balance between smoothness and speed that works for your specific application.