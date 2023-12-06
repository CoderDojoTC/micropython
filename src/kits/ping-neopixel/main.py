# Sample code to test HC-SR04 Ultrasonice Ping Sensor
# Connect GND to any GND pin on the Pico
# Connnect VCC to VBUS or 5 Volt power

from machine import Pin, Timer
from hcsr04 import HCSR04

from utime import sleep, sleep_us, ticks_us
from neopixel import NeoPixel

NUMBER_PIXELS = 12
LED_PIN = 0
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

onboard_led = Pin(25, Pin.OUT)

TRIGGER_PIN = 16 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 17 # One up from bottom left corner

MAX_DIST = 50

sensor = HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN)

# Will return a integer
def map(x, in_min, in_max, out_min, out_max):
    numerator = (x - in_min) * (out_max - out_min)
    denom = (in_max - in_min) + out_min
    if denom == 0:
        denom = .001
    return  int(numerator // denom)

min = MAX_DIST
max = 0
sleep(.1)

while True:
    dist = sensor.distance_cm()
    if dist > MAX_DIST:
        dist = MAX_DIST;
    if dist > max:
        max = dist
    if dist < min:
        min = dist
    print("min: ", min, " max: ", max)
    index = map(dist, min, max, 0, 11)
    print("Distance:", round(dist, 2), "cm", " index:", index)
    strip[index] = (255,0,255)
    strip.write()
    sleep(.1)
    onboard_led.toggle()
    strip[index] = (0,0,0)
