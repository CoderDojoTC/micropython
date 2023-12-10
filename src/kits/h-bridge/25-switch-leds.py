# swith status with no debounce logic
from machine import Pin
from utime import sleep, ticks_ms
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

make_forward_list()
make_reverse_list()

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
                # for a dark room use lightblue
                strip[forward_list[i]] = blue
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
                strip[reverse_list[i]] = green
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

# Upper left, lower left, upper right, lower right
UL_PIN = 2
LL_PIN = 3
UR_PIN = 14
LR_PIN = 13

ul_switch = Pin(UL_PIN, Pin.IN, Pin.PULL_UP)
ll_switch = Pin(LL_PIN, Pin.IN, Pin.PULL_UP)
ur_switch = Pin(UR_PIN, Pin.IN, Pin.PULL_UP)
lr_switch = Pin(LR_PIN, Pin.IN, Pin.PULL_UP)

# get current values as global variables
ul = ul_switch.value()
ll = ll_switch.value()
ur = ur_switch.value()
lr = lr_switch.value()

# old values
ul_old = 0
ll_old = 0
ur_old = 0
lr_old = 0

last_time = 0
switch_counter = 0
# this function gets called every time the button is pressed
def switch_changed_handler(pin):
    global last_time, switch_counter, ul, ll, ur, lr
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        if 'GPIO2' in str(pin):
            if ul == 0:
                ul = 1
            else: ul = 0
        if 'GPIO3' in str(pin):
            if ll == 0:
                ll = 1
            else: ll = 0
        if 'GPIO14' in str(pin):
            if ur == 0:
                ur = 1
            else: ur = 0
        if 'GPIO13' in str(pin):
            if lr == 0:
                lr = 1
            else: lr = 0
        switch_counter +=1
        last_time = new_time

# now we register the handler function when the button is pressed
# https://docs.micropython.org/en/latest/library/machine.Pin.html
ul_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)
ll_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)
ur_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)
lr_switch.irq(trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), handler = switch_changed_handler)

delay = .2
old_switch_counter = 0
counter = 0
print('Startup:', ul, ll, ur, lr)
while True:
    
    if (not(ul) and not(lr) and not(ll) and not(ur) ):
        for i in range(0, 20):
            strip[i] = red
        strip.write()
        print('Double Short Circuit')

    elif (not(ul) and not(lr) and ll and ur ):
        print('Startup:', ul, ll, ur, lr)
        print('forward')
        draw_forward(delay)   

    elif (not(ll) and not(ur) and ul and lr):
        print('reverse')
        draw_reverse(delay)

    # short circuit left
    elif not(ul) and not(ll):
        print('short circuit left')
        print('Startup:', ul, ll, ur, lr)
        for i in range(10, 20):
            strip[i] = red
        strip.write()

    # short circuitright
    elif not(ur)and not(lr):
        print('short circuit right')
        print('Startup:', ul, ll, ur, lr)
        for i in range(0, 10):
            strip[i] = red
        strip.write()
        
    # only print on change in the button_presses value
    if old_switch_counter != switch_counter:
        # print('Switch counter: ', switch_counter)
        old_switch_counter = switch_counter
    
    if ul != ul_old:
        if ul == 0:
            print("Upper Left = On")
        else:
            print("Upper Left = Off")
            clear()
        ul_old = ul
        counter += 1
    
    if ll != ll_old:
        if ll == 0:
            print("Lower Left = On")
        else:
            print("Lower Left = Off")
            clear()
        ll_old = ll
        counter += 1
    
    if ur != ur_old:
        if ur == 0:
            print("Upper Right = On")
        else:
            print("Upper Right = Off")
            clear()
        ur_old = ur
        counter += 1
        
    if lr != lr_old:
        if lr == 0:
            print("Lower Right = On")
        else:
            print("Lower Right = Off")
            clear()
        lr_old = lr
