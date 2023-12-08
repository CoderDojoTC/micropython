from machine import Pin
from utime import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 28
LED_PIN = 12

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# one segment for the 6 parts of the H brige
# lower right, upper right, upper left, lower left, middle right, middle left
segments = [[0,4], [5,9], [10,14], [15,19], [20, 23], [24, 27]]
num_segments = len(segments)
# upper left, middle left, middle right, lower right
foward_segments = [2,4,5,0]
forward_directions = [1,1,1,-1]
forward_list = []
# upper right, middle right, middle left, lower left
reverse_segments = [1,5,4,3]
reverse_directions = [-1,-1,-1,1]
reverse_list = []

color_names = ["red", "orange", "yellow", "green", "indigo", "violet"]
red = (255, 0, 0)
lightred = (25, 0, 0)
off = (0,0,0)
orange = (120, 40, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
lightgreen = (0, 25, 0)
blue = (0, 0, 255)
lightblue = (0, 0, 25)
cyan = (255, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
colors = (red, orange, yellow, green, blue, indigo, violet)

def make_forward_list():
    seg_counter = 0
    for i in foward_segments:
        if forward_directions[seg_counter] > 0:
            for j in range(segments[i][0], segments[i][1]+1):
                forward_list.append(j)
        else:
            for j in range(segments[i][1], segments[i][0]-1, -1):
                forward_list.append(j)
        seg_counter += 1

def make_reverse_list():
    seg_counter = 0
    for i in reverse_segments:
        if reverse_directions[seg_counter] > 0:
            for j in range(segments[i][0], segments[i][1]+1):
                reverse_list.append(j)
        else:
            for j in range(segments[i][1], segments[i][0]-1, -1):
                reverse_list.append(j)
        seg_counter += 1

def forward():
    for i in forward_list:
        strip[i] = lightblue
        strip.write()
        sleep(delay)
        strip[i] = off

def reverse():
    for i in reverse_list:
        strip[i] = lightgreen
        strip.write()
        sleep(delay)
        strip[i] = off
 
delay = 0.2

make_forward_list()
print(forward_list)
make_reverse_list()
print(reverse_list)

while True:  
    forward()
    reverse()
   


