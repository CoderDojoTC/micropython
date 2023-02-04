# Timing Drawing Speed

If you are writing a video game and want fast drawing times for objects on the screen, there are several different algorithms you can try.  You can use the MicroPython ```time_us``` function to
record the time before and after you call a drawing function and return the difference
to get an idea of the time saved in different versions of your drawing functions.

## Sample Function Timer Code

## Sample Function Code

```py
from utime import ticks_us

start = ticks_us()
my_function()
end = ticks_us()
print('Execution time in microseconds:', end - start)
```

MicroPython also supports the ```ticks_cpu()``` function which could return a smaller granularity
for precise time measurements.  However, on the Raspberry Pi implementation, the results are exactly
the same as the ```ticks_us()``` function.

## Comparing Two Circle Drawing Algorithms

In the following code, we compare two circle drawing algorithms.

1. **Row Scanner Method** - this method scans each pixel in the square around the circle and turns it on if the pixel is within a distance range.  It must calculate the distance of each pixel and compare
2. that distance to both the inside and outside distances.  The time-consuming operations are to calculate the squares of the x and y distances.
3. **Point Draw Method** - this method walks around the circle and for each degree, it draws a single pixel at the edge of the circle.  Each point uses the ```sine()``` and ```cosine()``` functions to calculate the x and y distance from the center of the circle to that point.

For small circles, it is very inefficient to calculate all 360 points.  Scanning all the points in a 5X5 grid only takes 25 calculations.  However, the larger the circle becomes, the more points there are to calculate in the row scanner method.  A 20X20 circle will need to run the distance calculation 400 times.

```py
from utime import sleep, ticks_cpu, ticks_us
import math
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)

WIDTH = 128
HEIGHT = 64
clock=Pin(2)
data=Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# 
def fast_circle(x, y, r, color):
    # draw points around a circle skiping every 4th one
    for theta in range(0, 360, 2):
        # we can save 5% of the time by only doing this once
        radians = math.radians(theta)
        x_pos = int(x + r * math.cos(radians))
        y_pos = int(y + r * math.sin(radians))
        # check if we are within range
        #if 0 <= x_pos < 128 and 0 <= y_pos < 64:
        # we can cut another 5% by not doing these checks
        oled.pixel(x_pos, y_pos, color)

def circle(x, y, r, color):
    diameter1 = (r - 0.5) ** 2
    diameter2 = (r + 0.5) ** 2
    x_min = max(0, int(x - r))
    x_max = min(128, int(x + r + 1))
    y_min = max(0, int(y - r))
    y_max = min(64, int(y + r + 1))

    for y_pos in range(y_min, y_max):
        for x_pos in range(x_min, x_max):
            if ((x_pos - x) ** 2 + (y_pos - y) ** 2 >= diameter1) and ((x_pos - x) ** 2 + (y_pos - y) ** 2 <= diameter2):
                oled.pixel(x_pos, y_pos, color)


start = ticks_us()
circle(32, 32, 10, 1)
end = ticks_us()
print('Standard scanner circle draw time in cpu ticks', end - start)
oled.show()
sleep(1)
start = ticks_us()
fast_circle(96, 32, 10, 1)
end = ticks_us()
print('Fast draw time in cpu ticks', end - start)
oled.show()
```

!!! Challenge
    1. Write a program that compares drawing speed for various sizes of circles.
    2. Modify the circle function to use the most efficient algorithm
    3. If you have a small circle, how many points do you need to not make the circle appear broken?  Try changing the number of points calculated in the line ```for theta in range(0, 360, 2):``.  Can you dynamically change the number of points skipped as the circle becomes smaller?
    4. Can you add a parameter to the circle function that only draws every 3rd point?