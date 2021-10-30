# Maker Pi RP2040 Collision Avoidance Robot With Ping Sensor

This robot works very similar to our standard CoderDojo Collision Avoidance Robot but all the pins are now configured to use the connections on the Maker Pi RP2040 board.

The board is mounted on a SmartCar Chassis and Grove Connector 4 is used to connect
the ultrasonic ping sensor.  Connect the Trigger on white and Echo on yellow.  The black should be connected to GND and the Red is connected to the VCC which on the 

The robot has an initial mode of 0, which will run the blue LEDs and change colors on the Neopixels.  By pressing the on-board button you will start the collision avoidance program.

## Robot Parameters

There are four different robot parameters you can adjust.  They change the speed and distance before the robot backs up.  You can also adjust the time the robots goes into reverse and the time it turns.

```py
POWER_LEVEL = 35000 # max is 
TURN_DISTANCE = 20 # distance in cm we decide to turn - try 20
REVERSE_TIME = .4 # how long we backup
TURN_TIME = .4 # how long we turn
```
## Full Source Code

```py
# Demo for Maker Pi RP2040 board using Ping sensor
from machine import Pin, PWM, Timer
import utime
import urandom
from neopixel import Neopixel

# Adjust these parameters to tune the collision avoidance behavior

POWER_LEVEL = 35000
TURN_DISTANCE = 20 # distance we decide to turn - try 20
REVERSE_TIME = .4 # how long we backup
TURN_TIME = .4 # how long we turn

# startup mode is 0 - motors off and LEDs flashing
# mode 1 is slow
# mode 2 is medium
# mode 3 is fast
mode = 0

# Use the Grove 4 Connector and put trigger on white and echo on yellow
TRIGGER_PIN = 16 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 17 # One up from bottom left corner

# Init HC-SR04P pins
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back

faster_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
slower_pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)

last_time = 0 # the last time we pressed the button

# This function gets called every time the button is pressed.  The parameter "pin" is not used.
def button_pressed_handler(pin):
    global mode, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # this should be pin.id but it does not work
        if '20' in str(pin):
            mode +=1
        else:
            mode -=1
        # deal with ends
        if mode > 4: mode = 2
        if mode < 0: mode = 0
        last_time = new_time

# now we register the handler function when the button is pressed
faster_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
slower_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# Piezo Buzzer is on GP22
buzzer=PWM(Pin(22))

MAX_POWER_LEVEL = 65025

MAX_DISTANCE = 100 # ignore anything above this

# Motor Pins are A: 8,9 and B: 10,11
RIGHT_FORWARD_PIN = 11
RIGHT_REVERSE_PIN = 10
LEFT_FORWARD_PIN = 9
LEFT_REVERSE_PIN = 8

# our PWM objects
right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))

# returns distance in cm
def ping():
    print('in ping')
    trigger.low()
    utime.sleep_us(2) # Wait 2 microseconds low
    trigger.high()
    utime.sleep_us(5) # Stay high for 5 miroseconds
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    print('echo is 1')
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print(distance)
    return int(distance)

def turn_motor_on(pwm):
   pwm.duty_u16(65025)

def turn_motor_off(pwm):
   pwm.duty_u16(0)

def forward():
    turn_motor_on(right_forward)
    turn_motor_on(left_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_reverse)

def reverse():
    turn_motor_on(right_reverse)
    turn_motor_on(left_reverse)
    turn_motor_off(right_forward)
    turn_motor_off(left_forward)

def turn_right():
    turn_motor_on(right_forward)
    turn_motor_on(left_reverse)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)

def turn_left():
    turn_motor_on(right_reverse)
    turn_motor_on(left_forward)
    turn_motor_off(right_forward)
    turn_motor_off(left_reverse)

def stop():
    turn_motor_off(right_forward)
    turn_motor_off(right_reverse)
    turn_motor_off(left_forward)
    turn_motor_off(left_reverse)

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs
# remove 16 and 17 since the are used for the ping sensor
blue_led_pins = [0, 1, 2, 3,  4,  5,  6,  7, 26, 27, 28]
# dist_scale =    [2, 4, 6, 8, 10, 13, 16, 20, 25, 35, 50, 75, 100]
dist_scale =    [2, 4, 6, 8, 10, 15, 20, 25, 50, 100, 150, 200, 300]

NUMBER_PIXELS = 2
STATE_MACHINE = 0
NEOPIXEL_PIN = 18

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, NEOPIXEL_PIN, "GRB")
strip.brightness(100)

number_leds = len(blue_led_pins)
led_ports = []
red = (255, 0, 0)
orange = (255, 60, 0) # Gamma corrected from G=128 to be less like yellow
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130) # purple?
violet = (138, 43, 226) # mostly pink
cyan = (0, 255, 255)
lightgreen = (100, 255, 100)
white = (128, 128, 128) # not too bright
pink = (255, 128, 128)
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'cyan', 'lightgreen', 'white')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet, cyan, lightgreen, white, pink)

# create a list of the ports
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

LED_DELAY = .08
def run_lights():
    for i in range(0, number_leds):
        led_ports[i].high()
        strip.set_pixel(0, colors[i])
        strip.set_pixel(1, colors[i])
        strip.show()
        utime.sleep(LED_DELAY)
        led_ports[i].low()
    # blue down
    for i in range(number_leds - 1, 0, -1):
        led_ports[i].high()
        strip.set_pixel(0, colors[i])
        strip.set_pixel(1, colors[i])
        strip.show()
        utime.sleep(LED_DELAY)
        led_ports[i].low()

def led_show_dist(in_distance):
    global number_leds
    for led_index in range(0, number_leds):
        if in_distance > dist_scale[led_index]:
            led_ports[led_index].high()
        else:
            led_ports[led_index].low()

def play_no_signal():
    playnote(100, 0.1)
    sound_off()

def play_turn():
    playnote(500, .1)
    sound_off()

def setfreq(frequency):
    buzzer.freq(frequency)

def playnote(frequency, time):
    buzzer.duty_u16(1000)
    setfreq(frequency)
    utime.sleep(time)
    
def sound_off():
    buzzer.duty_u16(0)

def rest(time):
    buzzer.duty_u16(0)
    utime.sleep(time)
    
def play_startup():
    playnote(600, .2)
    rest(.05)
    playnote(600, .2)
    rest(.05)
    playnote(600, .2)
    rest(.1)
    playnote(800, .4)
    sound_off()
    
valid_distance = 1
# loop forever
def main():
    global valid_distance
    print("running main()")
    
    play_startup()
    
    while True:
        if mode == 0:
            stop()
            run_lights()
        else:
            distance = ping()
            print('Distance:', distance)
            if distance > MAX_DISTANCE:
                # only print if we used to have a valid distance
                if valid_distance == 1:
                    print('no signal')      
                valid_distance = 0
            else:
                print(distance)
                if distance < TURN_DISTANCE:
                    play_turn()
                    # back up for a bit
                    reverse()
                    utime.sleep(REVERSE_TIME)
                    # half right and half left turns
                    if urandom.random() < .5:
                        turn_right()
                    else:
                        turn_left()
                    utime.sleep(TURN_TIME)
                    forward()
                else:
                    print('forward')
                    forward()
                valid_distance = 1
                led_show_dist(distance)
            utime.sleep(0.05)

# clean up

# This allows us to stop the sound and motors when we do a Stop or Control-C which is a keyboard interrupt
try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('turning off sound')
    buzzer.duty_u16(0)
    print('shutting motors down')
    stop()

```

## Experiments

1. Adjust the power level and the distance before turning.  See how these change the performance of the robot.
2. Adjust the angle of the ping sensor by gently heating the plexiglass holder.  How does this change the robot behavior?
3. Add additional modes that change the power and the turn distance.  You can have one mode for slow, one for medium and one for fast.
4. Change the Neopixel colors to indicate the distance to an object.
5. Change the pattern of the blue LEDs to indicate the distance to the object.