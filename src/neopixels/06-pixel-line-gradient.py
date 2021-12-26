import machine, neopixel
from utime import sleep
from neopixel import Neopixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 72
strip = Neopixel(NUMBER_PIXELS, 0, NEOPIXEL_PIN, "GRB")
left = 0
max_index = NUMBER_PIXELS - 1
step = 3

delay=.001
while True:
    print('red to green')
    for i in range(0, 255, step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (255,0,0), (0,255,0))
        strip.show()
        sleep(delay)
    for i in range(255, 0, -step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (255,0,0), (0,255,0))
        strip.show()
        sleep(delay)
    
    print('green to blue')
    for i in range(0, 255, step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (0,255,0), (0,0,255))
        strip.show()
        sleep(delay)
    for i in range(255, 0, -step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (0,255,0), (0,0,255))
        strip.show()
        sleep(delay)
    
    print('blue to red')
    for i in range(0, 255, step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (0,0,255), (255,0,0))
        strip.show()
        sleep(delay)
    for i in range(255, 0, -step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (0,0,255), (255,0,0))
        strip.show()
        sleep(delay)

    print('yellow to purple')
    for i in range(0, 255, step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (255,125,0), (255,0,255))
        strip.show()
        sleep(delay)
    for i in range(255, 0, -step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (255,125,0), (255,0,255))
        strip.show()
        sleep(delay)
        
    print('orange to blue')
    for i in range(0, 255, step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (50,25,0), (0,0,255))
        strip.show()
        sleep(delay)
    for i in range(255, 0, -step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (50,25,0), (0,0,255))
        strip.show()
        sleep(delay)

    print('cyan to pink')
    for i in range(0, 255, step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (0,255,255), (50,0,0))
        strip.show()
        sleep(delay)
    for i in range(255, 0, -step):
        strip.brightness(i)
        strip.set_pixel_line_gradient(0, max_index, (0,255,255), (50,0,0))
        strip.show()
        sleep(delay)
        
    print('')