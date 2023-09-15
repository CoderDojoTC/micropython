import machine
import utime
import ssd1306
from utime import sleep, localtime
led = machine.Pin('LED', machine.Pin.OUT)

SCL=machine.Pin(2) # SPI CLock
SDA=machine.Pin(3) # SPI Data
spi=machine.SPI(0, sck=SCL, mosi=SDA)

RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

def timeStrFmt():
    hour = localtime()[3]
    if hour > 12:
        hour = hour - 12
        am_pm = ' pm'
    else: am_pm = ' am'
    # format minutes and seconds with leading zeros
    minutes = "{:02d}".format(localtime()[4])
    seconds = "{:02d}".format(localtime()[5])
    return str(hour) + ':' + minutes + ':' + seconds + am_pm

def dateStrFmt():
    return  str(localtime()[1]) + '/' + str(localtime()[2]) + '/' + str(localtime()[0])

def update_display(timeStr, dateStr):
    oled.fill(0)
    oled.text(timeStr, 10, 10, 1)
    oled.text(dateStr, 10, 20, 1)
    oled.show()

counter = 0
while True:
    update_display(timeStrFmt(), dateStrFmt())
    print(localtime(), dateStrFmt(), timeStrFmt(), counter)
    led.toggle()
    counter += 1
    sleep(1)
    

