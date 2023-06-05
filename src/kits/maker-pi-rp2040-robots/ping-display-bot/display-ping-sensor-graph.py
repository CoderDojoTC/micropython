from machine import Pin, PWM
from utime import sleep, sleep_us, ticks_us

from  ssd1306 import SSD1306_SPI

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)

spi=machine.SPI(0, sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(13)
DC = machine.Pin(14)
RES = machine.Pin(15)
oled = SSD1306_SPI(128, 64, spi, DC, RES, CS)

# pins used on the Grove 4 connector
Trig = Pin(17, Pin.OUT)
Echo = Pin(16, Pin.IN, Pin.PULL_DOWN)

def CheckDistance():
    SpeedOfSoundInCM = 0.034
    Trig.low()
    sleep_us(2)
    Trig.high()
    sleep_us(10)
    Trig.low()
    exitLoop = False
    loopcount = 0
    while Echo.value() == 0 and exitLoop == False:
        loopcount = loopcount + 1
        delay_time = ticks_us()
        if loopcount > 3000:
            exitLoop == True
    while Echo.value() == 1 and exitLoop == False:
        loopcount = loopcount + 1
        receive_time = ticks_us()
        if loopcount > 3000:
            exitLoop == True
    if exitLoop == True:
        return (0)
    else: 
        return int(( (receive_time - delay_time) * SpeedOfSoundInCM) / 2)

oled.fill(0)
MAX_VALID_DISTANCE = 63
max_dist = 0
min_dist = 63
x = 0
while True:
    distance = CheckDistance()
    
    if distance > MAX_VALID_DISTANCE:
        distance = MAX_VALID_DISTANCE
    if distance > max_dist:
        max_dist = distance
    if distance < min_dist:
        min_dist = distance
    # oled.fill(0)
    range = max_dist - min_dist
    oled.pixel(x, distance, 1)
    if x < 126:
        x += 1
    if x > 125:
        oled.scroll(-1,0)
    
    # oled.text(str(distance), x*10, 0, 1)
    oled.show()
    print(distance, min_dist, max_dist, range, x)
    sleep(.1)