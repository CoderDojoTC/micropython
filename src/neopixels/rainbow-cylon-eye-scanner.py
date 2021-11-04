from utime import sleep
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 25
STATE_MACHINE = 0
LED_PIN = 0

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

# Color RGB values
red = (255, 0, 0)
off = (0,0,0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (255, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet)

# set to be 1 to 100 for percent brightness
strip.brightness(100)

def draw_eye_7(r, g, b):
    for i in range(6, NUMBER_PIXELS): 
        strip.set_pixel(i, (r, g, b))
        # step back from the current to 6 back halfing the intensity each time
        for j in range(0,7):
            strip.set_pixel(i-j, (int(r/pow(2,j)), int(g/pow(2,j)), int(b/pow(2,j))))
        if i > 6: strip.set_pixel(i-7, (0,0,0))
        strip.show()
        sleep(delay)
        strip.set_pixel(i, off)
    for i in range(NUMBER_PIXELS-6, 0, -1):
        strip.set_pixel(i, (r, g, b)) 
        for j in range(7,0):
            strip.set_pixel(i+j, (int(r/pow(2,j)), int(g/pow(2,j)), int(b/pow(2,j))))
        if i < NUMBER_PIXELS-7: strip.set_pixel(i+7, (0,0,0))
        strip.show()
        sleep(delay)

def draw_rainbow():
    for i in range(0, NUMBER_PIXELS-7):
        strip.set_pixel(i, violet)
        strip.set_pixel(i+1, indigo)
        strip.set_pixel(i+2, blue)
        strip.set_pixel(i+3, green)
        strip.set_pixel(i+4, yellow)
        strip.set_pixel(i+5,orange)
        strip.set_pixel(i+6, red)
        if i > 6: strip.set_pixel(i-7, (0,0,0))
        strip.show()
        sleep(delay)
        strip.set_pixel(i, off)
    for i in range(NUMBER_PIXELS-7, 1, -1):
        strip.set_pixel(i, red)
        strip.set_pixel(i+1, orange)
        strip.set_pixel(i+2, yellow)
        strip.set_pixel(i+3, green)
        strip.set_pixel(i+4, blue)
        strip.set_pixel(i+5, indigo)
        strip.set_pixel(i+6, violet)
        if i < NUMBER_PIXELS-7: strip.set_pixel(i+7, (0,0,0))
        strip.show()
        sleep(delay)

# delay = .031

delay = .06
color_index = 0
while True:
    draw_rainbow()
    draw_eye_7(255,0,0)
    draw_eye_7(255,60,0)
    draw_eye_7(255,255,0)
    draw_eye_7(0,255,0)
    draw_eye_7(0,0,255)
    draw_eye_7(0,255,255)
    draw_eye_7(75,30,130)
    draw_eye_7(255,0,255)
    draw_eye_7(255,255,255)