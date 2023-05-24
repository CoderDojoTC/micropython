import machine
import utime
from ssd1306 import SSD1306_I2C

sda=machine.Pin(2)
scl=machine.Pin(3)
i2c=machine.I2C(1,sda=sda, scl=scl)
# Screen size
width=128
height=64
oled = SSD1306_I2C(width, height, i2c)

oled.fill(0)

# ok, not really a circle - just a square for now
def draw_ball(x,y, size, state):
    if size == 1:
        oled.pixel(x, y, state) # draw a single pixel
    else:
        oled.ellipse(x, y, size, size, state, 1)
    # TODO: for size above 4 round the corners

#border
# oled.rect(0,0, width-1, height,-1, 1)

# start in the middle of the screen
current_x = int(width/2)
current_y = int(height/2)
# start going down to the right
direction_x = 1
direction_y = -1
# delay_time = .0001

# Bounce forever
while True:
    for ball_size in range(2,20):
        for i in range(0,100):
            draw_ball(current_x,current_y, ball_size, 1)
            oled.show()
            # utime.sleep(delay_time)
            draw_ball(current_x, current_y, ball_size, 0)

            # reverse at the edges
            # left edge test
            if current_x < ball_size:
                direction_x = 1
            # right edge test
            if current_x > width - ball_size -2:
                direction_x = -1
            # top edge test
            if current_y < ball_size:
                direction_y = 1
            # bottom edge test
            if current_y > height - ball_size - 2:
                direction_y = -1
            # update the ball
            current_x = current_x + direction_x
            current_y = current_y + direction_y
