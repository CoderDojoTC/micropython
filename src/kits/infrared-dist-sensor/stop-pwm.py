from machine import Pin, PWM
from utime import sleep

SENSOR_PIN = 0
sensor = machine.Pin(SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)

led = Pin(25, Pin.OUT)

# corner of the lower right
SPEAKER_PIN = 16
speaker = PWM(Pin(SPEAKER_PIN))
speaker.duty_u16(0)