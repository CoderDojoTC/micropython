# OLED Bounce

In this lesson, we will draw a box around the edge of the display using the commands that draw horizontal and vertical lines: ```hline``` and ```vline```.  Then we will draw a ball that bounces off these edges.


## Draw a border

```py
import machine
import utime
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl)
# Screen size
width=128
height=64
oled = SSD1306_I2C(width, height, i2c)

oled.hline(0, 0, width - 1, 1) # top edge
oled.hline(0, height - 1, width - 1, 1) # bottom edge
oled.vline(0, 0, height - 1, 1) # left edge
oled.vline(width - 1, 0, height - 1, 1) # right edge
oled.show()
```

## Make a Ball Bounce Around Inside the Wall

```py
import machine
import utime
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl)
# Screen size
width=128
height=64
oled = SSD1306_I2C(width, height, i2c)

oled.fill(0) # clear to black

# note that OLEDs have problems with screen burn it - don't leave this on too long!
def border(width, height):
    oled.hline(0, 0, width - 1, 1) # top edge
    oled.hline(0, height - 1, width - 1, 1) # bottom edge
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

ball_size = 2
# start in the middle of the screen
current_x = int(width / 2)
current_y = int(height / 2)
# start going down to the right
direction_x = 1
direction_y = -1
# delay_time = .0001

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
    if current_y > height - ball_size - 2:
        direction_y = -1
    # update the ball
    current_x = current_x + direction_x
    current_y = current_y + direction_y
```

