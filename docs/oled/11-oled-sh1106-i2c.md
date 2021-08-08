# OLED SSD1306 I2C Examples

We use small OLED displays in many of our labs because:

1. They are **inexpensive** (around $4).
2. They are **easy to connect** via SPI.  Just four wires: GND, VCC, Clock and Data.
3. They have a **large area** to display feedback.  Most of them are 128X64 pixels.
4. Once you get the drivers installed (not always easy) they are **easy to program**.  You only need to initialize the device and run the oled.fill(), oled.text() and oled.show() functions.
5. OLEDs, unlike LCDs, have **high contrast over a large range of input voltages**.  This means that as your batteries slowly discharge, your OLEDs will keep their high-quality contrast.
6. There is plenty of **sample code and tutorials** available.


The first step is to find out what type of display graphics chip is used in your OLED.





## SH1106 Example

```py
from machine import Pin, I2C
import sh1106

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

display.fill(0)
display.text('CoderDojo', 0, 0, 1)
display.show()

print('done')
```

## Counter Example
In this example we will updated the display 50 times with a 1/10th of a second pause between each refresh.  A counter will cycle from 1 to 50.

```py
import machine
import utime
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

for i in range(1, 51): # count 1 to 50
    oled.fill(0) # clear to black
    oled.text('CoderDojo Rocks!', 0, 0, 1) # at x=0, y=0, white on black
    oled.text(str(i), 40, 20, 1) # move 30 pixels horizontal and 20 down from the top
    oled.show() # update display
    utime.sleep(0.1) #wait 1/10th of a second

print('done')
```

## Animated Box
This draws a title and four lines around a drawing area.  It then draws boxes that move to the right.

```py
from machine import Pin, I2C
import sh1106
import utime

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

## note that we can only draw from 0 to 62
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

display.fill(0) # clear to black
display.text('CoderDojo Rocks', 0, 0, 1) # at x=0, y=0, white on black
# line under title
display.hline(0, 9, 127, 1)
# bottom of display
display.hline(0, 30, 127, 1)
# left edge
display.vline(0, 10, 32, 1)
# right edge
display.vline(127, 10, 32, 1)

for i in range(0, 118):
    # box x0, y0, width, height, on
    display.fill_rect(i,10, 10, 10, 1)
    # draw black behind number
    display.fill_rect(10, 21, 30, 8, 0)
    display.text(str(i), 10, 21, 1)
    display.show() # update display
    # utime.sleep(0.001)

print('done')
```

## Bounce on the SH1106 Display using I2C

This example is a ball that bounces around the inside of a border rectangle.  Is similar to other bounce examples with the exception that you can't draw on the last row of pixels.

```py
import machine
import utime
# from ssd1306 import SSD1306_I2C
import sh1106

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl)
# Screen size
width=128
height=64 # we could make this be 63 but the init method should use the full value
# oled = SSD1306_I2C(width, height, i2c)
oled = sh1106.SH1106_I2C(width, height, i2c, machine.Pin(4), 0x3c)

oled.fill(0) # clear to black

# note that OLEDs have problems with screen burn it - don't leave this on too long!
def border(width, height):
    oled.hline(0, 0, width - 1, 1) # top edge
    oled.hline(0, height - 2, width - 1, 1) # bottom edge
    oled.vline(0, 0, height - 1, 1) # left edge
    oled.vline(width - 1, 0, height - 1, 1) # right edge

# ok, not really a circle - just a square for now
def draw_ball(x,y, size, state):
    if size == 1:
        oled.pixel(x, y, state) # draw a single pixel
    else:
        for i in range(0,size): # draw a box of pixels of the right size
            for j in range(0,size):
                oled.pixel(x + i, y + j, state)
    # TODO: for size above 4 round the corners

border(width, height)

ball_size = 5
current_x = int(width / 2)
current_y = int(height / 2)
direction_x = 1
direction_y = -1
# delay_time = .0001

# oled.line(0, height-2, width-1, height-2, 1)

# Bounce forever
while True:
    draw_ball(current_x,current_y, ball_size,1)
    oled.show()
    # utime.sleep(delay_time)
    draw_ball(current_x,current_y,ball_size,0)
    # reverse at the edges
    # left edge test
    if current_x < 2:
        direction_x = 1
    # right edge test
    if current_x > width - ball_size -2:
        direction_x = -1
    # top edge test
    if current_y < 2:
        direction_y = 1
    # bottom edge test
    if current_y > height - ball_size - 3:
        direction_y = -1
    # update the ball
    current_x = current_x + direction_x
    current_y = current_y + direction_y
    

print('done')
```

## SH1106 References

1. [Robert HH SH1106 Driver GitHub](https://github.com/robert-hh/SH1106/blob/master/sh1106.py)