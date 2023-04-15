from machine import Pin
from utime import sleep
import hcsr04

TRIGGER_PIN = 14 # Connect the white Grove connector wire next to the 5volt on the ping sensor
ECHO_PIN = 15 # Connect the yellow Grove connector wire next to the GND on the ping sensor

ping_sensor = hcsr04.HCSR04(TRIGGER_PIN, ECHO_PIN)

def avg_dist(num):   
    total_val = 0
    for i in range(0,num):
        total_val += ping_sensor.distance_cm()
        sleep(.02)
    return round(total_val/num, 3)

while True:
    distance_cm = avg_dist(10)
    print(distance_cm)
    sleep(.05)
