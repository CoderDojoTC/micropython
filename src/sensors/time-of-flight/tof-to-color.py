# convert a time-of-flight reading to a color using the wheel() function
# make a game of keeping it in a color range like blue
from machine import Pin,PWM
import VL53L0X
from neopixel import NeoPixel
from time import sleep

sda=Pin(26) # Grove connector 6
scl=Pin(27) # Colors on ToF sensor are RBYW (red, black, yello white)
i2c_tof=machine.I2C(1, sda=sda, scl=scl, freq=400000)

# Time of Flight Parameters as global variables
# You many need to adjust these a bit
ZERO_DIST = 40
# created dynamically if we get a lower value
zero_dist = ZERO_DIST
min_raw_distance = ZERO_DIST
# this might vary based on the ambient light around the sensor
MAX_DIST = 1000
max_raw_distance = 1000
SCALE_FACTOR = .9

# the two on-board NeoPixels
NUMBER_PIXELS = 2
NEOPIXEL_PIN = 18

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)    

# get the normalized time-of-flight distance in centimeters
# Needs to be calibrated with ZERO_DISTANCE and SCALE_FACTOR
def get_distance_cm():
    global zero_dist, scale_factor
    tof_distance = tof.read()
    if tof_distance > MAX_DIST:
        return tof_distance
    # if our current time-of-flight distance is lower than our zero distance then reset the zero distance
    if tof_distance < zero_dist:
        zero_dist = tof_distance
    return  int((tof_distance - zero_dist) * SCALE_FACTOR)
    
# startup
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_tof)
tof.start()

valid_distance = 0

# loop forever
def main():
    global max_raw_distance, min_raw_distance
    while True:
        # read a raw distance
        distance = tof.read()
        # print('raw distance', distance)
        if distance < MAX_DIST:
            print(distance, end='')
        else: print(0, end='')
        if distance > max_raw_distance:
            max_raw_distance = distance
        if distance < min_raw_distance:
            min_raw_distance = distance# wrap around 255 using modulo 255 to get the remainder
        mod_distance = distance % 255
        
        # print('mod distance', distance)
        print(', ', mod_distance)
        if distance < max_raw_distance:
            strip[0] = wheel(mod_distance)
            strip[1] = wheel(mod_distance)
            strip.write()
        else:
            strip[0] = (0,0,0)
            strip[1] = (0,0,0)
            strip.write()
        sleep(.1)
        

# This allows us to stop the sound by doing a Stop or Control-C which is a keyboard intrrupt
print('Running Time of Flight To Color')

try:
    main()
except KeyboardInterrupt:
    print('Got interupt')
finally:
    # Optional cleanup code
    print('Powering down time of flight sensor')
    tof.stop()

    