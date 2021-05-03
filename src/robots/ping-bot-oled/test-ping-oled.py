# Just test the ping sensor on the OLED display
from machine import Pin, PWM
from utime import sleep, sleep_us, ticks_us
import ssd1306

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)

width=128
height=64
oled = ssd1306.SSD1306_SPI(width, height, spi, DC, RES, CS)
led_onboard = machine.Pin(25, machine.Pin.OUT)

TRIGGER_PIN = 16 # With USB on the top, this pin is the bottom left corner
ECHO_PIN = 17 # One up from bottom left corner
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

def update_oled(dist, message):
    oled.fill(0)
    oled.text(str(dist), 0, 0, 1)
    oled.text(message, 0, 20, 1)
    oled.show()
    
while True:
    dist = ping()
    
    if dist < 15:
        update_oled(dist, "Turning")
        print(dist, "Turning")
    else:
        update_oled(dist, "Forward")
        print(dist, "Foward")
    sleep(.1)
    led_onboard.toggle()