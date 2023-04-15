from machine import Pin
from utime import sleep

SENSOR_PIN = 0
sensor = machine.Pin(SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    print(sensor.value())
    sleep(.1)