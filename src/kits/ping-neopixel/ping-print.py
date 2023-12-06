# Sample code to test HC-SR04 Ultrasonice Ping Sensor
# Connect GND to any GND pin on the Pico
# Connnect VCC to VBUS or 5 Volt power

from machine import Pin, Timer
from utime import sleep, sleep_us, ticks_us
from hcsr04 import HCSR04

TRIGGER_PIN = 16 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 17 # One up from bottom left corner

sensor = HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN)


while True:
    print("Distance:", sensor.distance_cm(), "cm")
    sleep(.1)
