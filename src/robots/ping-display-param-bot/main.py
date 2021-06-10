# Sample code to test HC-SR04 Ultrasonice Ping Sensor
# Connect GND to any GND pin on the Pico
# Connnect VCC to VBUS or 5 Volt power

from machine import Pin, Timer
import machine
import ssd1306
import time

TRIGGER_PIN = 7
ECHO_PIN = 6

# Init HC-SR04 pins
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back

WIDTH = 128
HEIGHT = 64
clock=machine.Pin(2)
data=machine.Pin(3)

spi=machine.SPI(0,sck=clock, mosi=data)

CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)

oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def ping():
    trigger.low()
    time.sleep_us(2) # Wait 2 microseconds low
    trigger.high()
    time.sleep_us(5) # Stay high for 5 miroseconds
    trigger.low()
    while echo.value() == 0:
        signaloff = time.ticks_us()
    while echo.value() == 1:
        signalon = time.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

i = 0
while True:
    dist = ping()
    print("Distance:", dist, " cm")
    time.sleep(.25)
    oled.fill(0)
    oled.text('Hello Dan', 0, 0, 1)
    oled.text(str(dist), 0, 10, 1)
    oled.text(str(i), 0, 53, 1)
    oled.show()
    time.sleep(.1)
    i += 1