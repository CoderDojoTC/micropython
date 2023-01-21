from machine import Pin
from utime import sleep

RIGHT_SENSOR_PIN = 2
LEFT_SENSOR_PIN = 4

right_sensor = Pin(RIGHT_SENSOR_PIN)
left_sensor = Pin(LEFT_SENSOR_PIN)

while True:
    r = right_sensor.value()
    l = left_sensor.value()
    print("r", r, "l=", l)
    if r == 0:
        print("right over white")
    if l == 0:
        print("left over white")
    sleep(.2)
    
