import ntptime, network
from machine import RTC
from utime import sleep, sleep_ms, time, localtime, mktime
import ssd1306

import config
# wifi_ssid =
# wifi_pass =

led = machine.Pin('LED', machine.Pin.OUT)

SCL=machine.Pin(2) # SPI CLock
SDA=machine.Pin(3) # SPI Data
spi=machine.SPI(0, sck=SCL, mosi=SDA)

RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

# US Central
timeZone = -6
# try one of these
ntptime.host = 'us.pool.ntp.org' #'time.nist.gov' #'pool.ntp.org'
ntptime.timeout = 10

# global variable for holding the current time array year, month, day, hour, minute, second
current_time = [] * 8

def wifiConnect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.config(pm = 0xa11140) # disables wifi sleep mode
    if not wifi.isconnected():
        wifi.connect(config.wifi_ssid, config.wifi_pass)
        print('Connecting..', end='')
        max_wait = 10
        while max_wait > 0:
            if wifi.status() < 0 or wifi.status() >= 3: break
            sleep_ms(1000)
            print('.', end='')
            max_wait -= 1
        print()
        if wifi.status() != 3: print('Could not connect to wifi!')
    # print('Connected: ',wifi.isconnected(),'\nIP: ',wifi.ifconfig()[0])
    sleep_ms(100)
    return wifi

# daylight savings time
def dst():
    year, weekday = localtime()[0], localtime()[6]
    dst_start = mktime((year, 3, (8 - weekday) % 7 + 8, 2, 0, 0, 0, 0))
    dst_end = mktime((year, 11, (1 - weekday) % 7 + 1, 2, 0, 0, 0, 0))
    return dst_start <= time() < dst_end

maxtries = 5
timetries = 0
timeset = False

def setRTC():
    global maxtries, current_time, timetries, timeset
    while not timeset and timetries < maxtries:
        timetries += 1
        try:
            ntptime.settime() # update time from ntp server
            timeset = True
        except:
            print(f'NTP update attempt # {timetries} of {maxtries} failed!', 'Retrying in 15 seconds..' if timetries < maxtries else 'Check connection/config.')
            if timetries < maxtries: sleep_ms(15000)
        if timeset:
            sleep_ms(200)
            rtc = RTC()
            tz_offset = (timeZone + 1) * 3600 if dst() else timeZone * 3600
            #tz_offset = timeZone * 3600 # without daylight savings
            myt = localtime(time() + tz_offset)
            current_time = myt
            rtc.datetime((myt[0], myt[1], myt[2], myt[6], myt[3], myt[4], myt[5], 0))
            sleep_ms(200)
            dtime = rtc.datetime()
            timestr = '%2d:%02d%s' %(12 if dtime[4] == 0 else dtime[4] if dtime[4] < 13 else dtime[4] - 12, dtime[5], 'am' if dtime[4] < 12 else 'pm')
            datestr = f'{dtime[1]}/{dtime[2]}/{dtime[0] % 100}'
            # print('Time set to:', timestr, datestr)
            print(timestr, datestr)
            return True
    print('ERROR! Unable to update time from server!')
    return False

def update():
    success = False
    wifi = wifiConnect()
    sleep_ms(100)
    if wifi.isconnected():
        success = setRTC()
        sleep_ms(100)
    return wifi, success

def timeStrFmt():
    hour = current_time[3]
    if hour > 12:
        hour = hour - 12
        am_pm = ' pm'
    else: am_pm = ' am'
    # format minutes and seconds with leading zeros
    minutes = "{:02d}".format(current_time[4])
    seconds = "{:02d}".format(current_time[5])
    return str(hour) + ':' + minutes + ':' + seconds + am_pm

def dateStrFmt():
    return  str(current_time[1]) + '/' + str(current_time[2]) + '/' + str(current_time[0])

def update_clock(timeStr, dateStr):
    oled.fill(0)
    oled.text(timeStr, 10, 10, 1)
    oled.text(dateStr, 10, 20, 1)
    oled.show()

def update_wifi_status():
    oled.fill(0)
    oled.text('n: ' + config.wifi_ssid , 0, 0, 1)
    oled.text('tries: ' + str(timetries), 0, 10, 1)
    if timeset:
        oled.text('Connection OK', 0, 20, 1)
    else:
        oled.text('CONNECTION ERROR', 0, 20, 1)
    oled.text('host: ' + ntptime.host, 0, 30, 1)
    oled.show()

second_counter = 0
minute_counter = 0
hour_counter = 0
update()
update_wifi_status()
sleep(3)

# run this loop every second
while True:
    update_clock(timeStrFmt(), dateStrFmt())
    # print(localtime())
    print(dateStrFmt(), timeStrFmt())
    led.toggle()
    sleep(1)
    # check the time server every hour
    if second_counter > 59:
        second_counter = 0
        if minute_counter > 59:
            minute_counter = 0
            if hour_counter > 23:
                # get a new time from the network time server
                update()
                hour_counter = 0
            else:
                hour_counter += 1
        else:
            minute_counter += 1
    else:
        second_counter += 1
        current_time[5] += 1
        
