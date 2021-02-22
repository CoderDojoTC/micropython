# Adding A Display to Your Project

## Concepts

### Framebuffers
A framebuffer is a copy of the display that is resident within the microcontroller.  It must be as large as the display.  For a 128X64 monochrome display this would be 128 * 64 = 8192 bits or 1,024 bytes (1K).

Memory requirements

### Basic Draw Functions
For our beginning labs we will just do some basic drawing. We will start out with just three functions: fill, text and show.

|Function|Description|Parameters|
|--------|-----------|----------|
|fill|Fill the display with white or black|0=black and 1=white|
|text|Draw text|String, x (horizontal from left edge) and y (vertical from the top)Example: Draw "Hello World" 40 over and 10 down.  oled.text("Hello World!", 40, 10)|
|show|Show the display|Send the current frame buffer to the display.  You must do this after you make and changes to the Framebuffer.

### Full list of Drawing Functions

Every drawing library might have slightly different functions.  But we can quickly see the functions that we want by using the dir() function on the SSD1306_I2C class.

```py
from ssd1306 import SSD1306_I2C
print(dir(SSD1306_I2C))
```
This returns the following list:

```py
['__class__', '__init__', '__module__', '__name__', '__qualname__', '__bases__', '__dict__', 'blit', 'fill', 'fill_rect', 'hline', 'invert', 'line', 'pixel', 'rect', 'scroll', 'text', 'vline', 'init_display', 'write_cmd', 'show', 'poweroff', 'poweron', 'contrast', 'write_data']
```
Technically, these are called methods of the SSD1306_I2C class.  The ones that begin and end with double underscores are class methods for creating new object instances.  The rest of the items on the list are the drawing functions.

The following are relevant for the SSD1306_I2C display.

|Function|Description|Example|
|--------|-----------|-------|
|blit|
|fill|Fill|Fill with black (0) or white(1)|
|fill_rect|Fill a rectangle||
|hline|Draw a horizontal line||
|invert|invert the display||
|line|draw a line at any angle||
|pixel|Draw a single point on the screen||
|rect|Draw an empty rectangle||
|scroll|Scroll the display||
|text|Write text at a point||
|vline|Draw a Vertical Line|vline(y0, x, y1, 1)|
|init_display|Initialize the display||
|write_cmd|Write a command to the display||
|show|Update the display from the frame buffer||
|poweroff|||
|poweron|||
|contrast|||
|write_data|||

128X64 Example
### Interfaces

### I2C

Pros: Simple four wire interface

|Pin|Purpose|Description|
|---|-------|-----------|

### SPI

Example: 128X64 pixel monochrome displays

## Types of Displays

### Summary Table

|Display Type|Cost|Links|Notes|
|------------|----|-----|-----|

### LCD

### OLED

### TFT Displays