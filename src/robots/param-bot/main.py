# Sample code to test HC-SR04 Ultrasonice Ping Sensor
# Connect GND to any GND pin on the Pico
# Connnect VCC to VBUS or 5 Volt power

from machine import Pin, Timer
import machine
import ssd1306
import time
from rotary import Rotary
import micropython

# for error handlings
micropython.alloc_emergency_exception_buf(100)

# the builtin LED should be flashing when the main loop is running
led_onboard = machine.Pin(25, machine.Pin.OUT)

# momentary push buttons in the lower left corner
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Init HC-SR04 pins
TRIGGER_PIN = 7
ECHO_PIN = 6
trigger = Pin(TRIGGER_PIN, Pin.OUT) # send trigger out to sensor
echo = Pin(ECHO_PIN, Pin.IN) # get the delay interval back

# display setup
WIDTH = 128
HEIGHT = 64
HALF_HEIGHT = 32
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0,sck=clock, mosi=data)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# Rotary Encoder pins for A, B and Press Button
rotary = Rotary(16, 17, 22)

# Global Variables
# current program running
prog = 0
x = 0
val = 0
param1 = 0
param2 = 0

def rotary_changed(change):
    global val, x
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
    elif change == Rotary.SW_PRESS:
        print('Button pressed to clear screen')    
        x = -1
        val = 0
    x += 1
    print('in rotary_changed')
    return
    
rotary.add_handler(rotary_changed)

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

def myMain():
    i = 0
    prog = 0
    while True:
        led_onboard.toggle()
        oled.fill(0)
        dist = round(ping(), 2)
        print("Distance:", dist, " cm")
        oled.text('Param Bot', 0, 0, 1)
        oled.text('d=', 0, 10, 1)
        if dist < 100: 
            oled.text(str(dist), 20, 10, 1)
            
        oled.text('prog=', 0, 20, 1)
        oled.text(str(prog), 45, 20, 1)
        
        oled.text('val=', 0, 30, 1)
        oled.text(str(val), 40, 30, 1)
        
        oled.text('x=', 0, 40, 1)
        oled.text(str(x), 20, 40, 1)
        
        if button1.value():
            oled.text('b1=', 100, 10, 1)
            oled.text(str(button1.value()), 120, 10, 1)
     
        if button2.value():
            oled.text('b2=', 100, 20, 1)
            oled.text(str(button1.value()), 120, 20, 1)
            
        oled.text(str(i), 0, 53, 1)
        oled.show()
        time.sleep(.1)
        i += 1

# this is the main loop that will watch for control-C events
try:
    myMain()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('cleaning up')
    oled.fill(0)
    oled.show()