# Sample code to test HC-SR04 Ultrasonice Ping Sensor
# Connect GND to any GND pin on the Pico
# Connnect VCC to VBUS or 5 Volt power

from machine import Pin, Timer
from neopixel import NeoPixel
from utime import sleep, sleep_us, ticks_us

NUMBER_PIXELS = 11
LED_PIN = 0
red = (50, 0, 0)
green = (0, 255, 0)

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)
TRIGGER_PIN = 16 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 17 # One up from bottom left corner

# Init HC-SR04 pins
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back

def ping():
    trigger.low()
    sleep_us(2) # Wait 2 microseconds low
    trigger.high()
    sleep_us(5) # Stay high for 5 miroseconds
    trigger.low()
    while echo.value() == 0:
        signaloff = ticks_us()
    while echo.value() == 1:
        signalon = ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

def avg_ping(samples):
    total = 0
    for i in range(0, samples+1):
        total += ping()
    return round(total / samples, 2)
        
while True:
    dist = avg_ping(5)
    # handle the no signal case
    if dist > 100:
        print("No signal")
        for i in range(0, NUMBER_PIXELS):
            if i == 0:
                strip[i] = red
            else:
                strip[i] = (0,0,0)
        strip.write()
    else:
        index = round(dist/5) # 5 cm per pixel
        if index > NUMBER_PIXELS:
            index = NUMBER_PIXELS-1
        print("Distance:", dist, " cm Index:", index)
        for i in range(0, NUMBER_PIXELS):
            if i < index:
                strip[i] = green
            else:
                strip[i] = (0,0,0)
        strip.write()
    sleep(.05)
