# Extending Drawing Functions

Although there are several drawing functions available in most of the standard graphics libraries, most of them lack some basic shapes such as a circle.  To draw circles on your display, you will need to add new Python functions.  Here are some examples of these custom drawing functions.

## Circle

Here is a function to draw a circle at a given (x,y) point with a radius of r and fill indicator.

Here are the parameters for circle functions

1. X position of the circle center
2. Y position of the circle center
3. The radius of the circle in pixels
4. The color of the circle (1 for on and 0 for off.


```python
from math import sqrt

def draw_circle(cx, cy, r, color):
    diameter = r*2
    upper_left_x = cx - r
    upper_left_y = cy - r 
    # scan through all pixels and only turn on pixels within r of the center
    for i in range(upper_left_x, upper_left_x + diameter):
        for j in range(upper_left_y, upper_left_y + diameter):
            # distance of the current point (i, j) from the center (cx, cy)
            d = sqrt( (i - cx) ** 2 + (j - cy) ** 2 )
            if d < r:
                oled.pixel(i, j, color)

```

## Testing Circle Drawing

```py
from machine import Pin
from utime import sleep
from math import sqrt
import ssd1306

WIDTH = 128
HEIGHT = 64
clock=Pin(2) # SCL
data=Pin(3) # SDA
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def circle(cx, cy, r, color):
    diameter = r*2
    upper_left_x = cx - r
    upper_left_y = cy - r 
    # scan through all pixels and only turn on pixels within r of the center
    for i in range(upper_left_x, upper_left_x + diameter):
        for j in range(upper_left_y, upper_left_y + diameter):
            # distance of the current point (i, j) from the center (cx, cy)
            d = sqrt( (i - cx) ** 2 + (j - cy) ** 2 )
            if d < r:
                oled.pixel(i, j, color)

HALF_WIDTH = int(WIDTH/2)
HALF_HEIGHT = int(HEIGHT/2)
while True:
    for rad in range(1,HALF_HEIGHT+2):
        draw_circle(HALF_WIDTH, HALF_HEIGHT, rad, 1)
        oled.show()
        sleep(.1)
    sleep(3)
    oled.fill(1)
    for rad in range(1,HALF_HEIGHT+2):
        circle(HALF_WIDTH, HALF_HEIGHT, rad, 0)
        oled.show()
        sleep(.1)
    oled.fill(0)
    sleep(3)
```

## Drawing a Face
If we assume we have a 64x128 display we can call two circle functions to draw eyes

display.fill(0)  # Clear the display.
display.circle(32, 32, 10, 1) # draw the left eye