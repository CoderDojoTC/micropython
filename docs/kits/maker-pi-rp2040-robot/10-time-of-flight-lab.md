# Time of Flight Distance Sensor Lab

In this lab we create a program that will show the distance measured by the Time-of-Flight sensor by printing the distance on the console and also displaying the distance on 11 blue LEDs.

First, make sure you have your driver for the Time-of-Flight sensor installed.

You can copy the code from [here](https://github.com/CoderDojoTC/micropython/blob/main/src/drivers/VL53L0X.py) and save it in the file VL53L0X.py.  Note the zero between the "L" and "X" in the file name, not the letter "O".

We use a non-linear distance scale as we get closer to an object.  We store the numbers of each LED and the distance it should change in a lists:

```py
blue_led_pins = [2, 3, 4,  5,  6,  7,  16, 17, 26, 27, 28]
dist_scale =    [2, 6, 10, 20, 30, 40, 50, 60, 80, 110, 150]
```

## Calibration

There are three numbers you can change when you calibrate the sensor:

```py
ZERO_DIST = 60 # The value of the sensor when an object is 0 CM away
MAX_DIST = 1200 # max raw distance we are able to read
SCALE_DIST = .3 # multiplier for raw to calibrated distance in CM
```

## Full Program

```py
# Demo for Maker Pi RP2040 board using the VL32L0X time of flight distance sensor
# Note the driver I used came from here: https://github.com/CoderDojoTC/micropython/blob/main/src/drivers/VL53L0X.py
# Perhaps derived from here: https://github.com/uceeatz/VL53L0X/blob/master/VL53L0X.py

# This demo makes the blue LEDs show the distance and prints the distance on the console
import machine
import time
import VL53L0X

sda=machine.Pin(0) # row one on our standard Pico breadboard
scl=machine.Pin(1) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
# print("Device found at decimal", i2c.scan())

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs which we can use 11
# The distance scale is non linear
# GP0 and GP1 will always be on since they are the I2C Data and Clock
blue_led_pins = [2, 3, 4,  5,  6,  7,  16, 17, 26, 27, 28]
dist_scale =    [2, 6, 10, 20, 30, 40, 50, 60, 80, 110, 150]
number_leds = len(blue_led_pins)
led_ports = []
delay = .05

# initial calibration parameters
ZERO_DIST = 60
MAX_DIST = 1200 # max raw distance we are able to read
SCALE_DIST = .3 # multiplier for raw to calibrated distance

# create a list of the ports
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c)


# get the normalized time-of-flight distance
def get_distance():
    global zero_dist, scale_factor
    tof_distance = tof.read()
    if tof_distance > MAX_DIST:
        return tof_distance
    # if our current time-of-flight distance is lower than our zero distance then reset the zero distance
    if tof_distance < ZERO_DIST:
        zero_dist = tof_distance
    return  int((tof_distance - ZERO_DIST) * SCALE_DIST)

# use the dist_scale to turn on LEDs
def led_show_dist(in_distance):
    global number_leds
    for led_index in range(0, number_leds):
        if in_distance > dist_scale[led_index]:
            led_ports[led_index].high()
        else:
            led_ports[led_index].low()

print('Using', number_leds, ' blue leds to show distance.')

# blue up
for i in range(0, number_leds):
    led_ports[i].high()
    time.sleep(delay)
    led_ports[i].low()
# blue down
for i in range(number_leds - 1, 0, -1):
    led_ports[i].high()
    time.sleep(delay)
    led_ports[i].low()
    
# start our time-of-flight sensor
tof.start()
# autocalibrate the minimum distance
min_distance = 1000


# loop forever
while True:
    raw_distance = get_distance()
    # recalibrate if we have a new min distance
    if raw_distance < min_distance:
        min_distance = raw_distance
    calibrated_distance = raw_distance - min_distance
    print(raw_distance, calibrated_distance)
    led_show_dist(calibrated_distance)
    time.sleep(0.05)

# clean up
tof.stop()

```

## References

[Kevin McAleer's GitHub Repo on the Vl53lx0](https://github.com/kevinmcaleer/vl53lx0)
[Kevin McAleer's 662 line driver](https://github.com/kevinmcaleer/vl53lx0/blob/master/vl53l0x.py) - I am not sure we need all 662 lines of code.
[Kevin McAleer's Time of Flight Test](https://github.com/kevinmcaleer/vl53lx0/blob/master/tof_test.py)