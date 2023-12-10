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

# draw every third pixel on
state = 2 # 0, 1 or 2
def draw_forward(delay):
    global state
    #print("fwd:", start)
    length = len(forward_list) + 2
    for i in range(0, length):
        # print(start, i, forward_list[i+start], not((i) % 3))
        if (i+state) < (length-1) and not((i+state) % 3):
            if i < length-2:
                strip[forward_list[i]] = lightblue
            # print("on: ", forward_list[i])
        else:
            if (i+state) < length-1:
                strip[forward_list[i]] = off
    strip.write()
    sleep(delay)
    if state == 0:
        state = 2
    else: state -= 1

state = 2
def draw_reverse(delay):
    global state
    #print("rev:", start)
    length = len(reverse_list)+2
    for i in range(0, length):
        #print(i+state)
        if not((i+state) % 3) and (i+state) < (length-1):
            if i < length-2:
                strip[reverse_list[i]] = lightgreen
        else:
            if (i+state) < length-1:
                strip[reverse_list[i]] = off
    strip.write()
    sleep(delay)
    if state == 0:
        state = 2
    else: state -= 1

def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = off
    strip.write() 

delay = .2

make_forward_list()
print(forward_list)
make_reverse_list()
print(reverse_list)

while True:
    for i in range(0, 40):
        draw_forward(delay)
    clear()
    for i in range(0, 40):
        draw_reverse(delay)
    clear()
   


