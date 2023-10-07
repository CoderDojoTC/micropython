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

# global array of integers for holding the current date and time
# Values are year=[0], month[1], day[2], hour[3], minute[4], second[5]
current_time = [] * 7
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0

# display a string on the 128x64 OLED screen using 9 pixel height and 16 characters per line
def display_msg(in_str, chunk_size=16):
    print(in_str)
    oled.fill(0)
    if len(in_str) < chunk_size:
        oled.text(in_str, 0, 0)
    else:
        # create an array of the strings for each line
        a = [in_str[i:i+chunk_size] for i in range(0, len(in_str), chunk_size)]
        for i in range(0,len(a)):
            oled.text(a[i], 0, i*9)
    oled.show()

# Connect the the local Wifi access point
# get the wifi network name and password from the config.py file
def wifiConnect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.config(pm = 0xa11140) # disables wifi sleep mode
    if not wifi.isconnected():
        wifi.connect(config.wifi_ssid, config.wifi_pass)
        message = 'Connecting to ' + config.wifi_ssid
        display_msg(message)
        max_wait = 10
        while max_wait > 0:
            if wifi.status() < 0 or wifi.status() >= 3: break
            sleep_ms(1000)
            message = message + '.'
            display_msg(message + str(10-max_wait))
            max_wait -= 1
        print()
        if wifi.status() != 3:
            display_msg('Error: Could not connect to wifi!')
    display_msg('Connected IP: ' + wifi.ifconfig()[0])
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
    global maxtries, current_time, timetries, timeset, year, month, day, hour, minute, second
    while not timeset and timetries < maxtries:
        timetries += 1
        try:
            ntptime.settime() # update time from ntp server
            timeset = True
        except:
            error_msg = 'NTP update attempt' + str(timetries) + ' of ' + str(maxtries) + ' Check config.'
            display_msg(error_msg)
            if timetries < maxtries: sleep_ms(15000)
        if timeset:
            sleep_ms(200)
            rtc = RTC()
            tz_offset = (timeZone + 1) * 3600 if dst() else timeZone * 3600
            #tz_offset = timeZone * 3600 # without daylight savings
            myt = localtime(time() + tz_offset)
            print('myt: ', myt)
            current_time = myt
            year = myt[0]
            month = myt[1]
            day = myt[2]
            hour = myt[3]
            minute = myt[4]
            second = myt[5]
            rtc.datetime((myt[0], myt[1], myt[2], myt[6], myt[3], myt[4], myt[5], 0))
            print('Seconds in myt[5]', myt[5])
            sleep_ms(200)
            dtime = rtc.datetime()
            timestr = '%2d:%02d%s' %(12 if dtime[4] == 0 else dtime[4] if dtime[4] < 13 else dtime[4] - 12, dtime[5], 'am' if dtime[4] < 12 else 'pm')
            datestr = f'{dtime[1]}/{dtime[2]}/{dtime[0] % 100}'
            print('Time set to:', timestr, datestr)
            print(timestr, datestr)
            return True
    display_msg('ERROR! Unable to update time from server:' + ntptime.host)
    return False

# get an update of the time from the Network Time Protocol Server
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
    return   str(month) + '/' + str(day) + str(year)

def update_display(year, month, day, hour, minute, second):
    oled.fill(0)
    # no 12/24, leadering zero formatting or am/pm formatting
    # time_strs = str(hour) + ':' + str(minute) + ':' + str(second)
    # with formatting
    timestrf = '%2d:%02d:%02d %s' %(12 if hour == 0 else hour if hour < 13 else hour - 12, minute, second, 'am' if hour < 12 else 'pm')
    oled.text(timestrf, 10, 20, 1)
    
    date_str = str(month) + '/' + str(day) + '/' + str(year)    
    oled.text(date_str, 10, 40, 1)
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

def break_string_into_chunks(s, chunk_size=12):
    """Breaks a string into chunks of a specified size."""
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

led.on()
display_msg('Booting.')
sleep(.5)

display_msg('Updating from NTP.')
sleep(.5)
update()

display_msg('Updating from NTP.')
update_wifi_status()
sleep(1)

update_display(year, month, day, hour, minute, second)

# run this loop every second
while True:

    print('current  time:', year, month, day, hour, minute, second)
    update_display(year, month, day, hour, minute, second)
    led.toggle()
    sleep(1)
    second += 1
    
    # check the time server every hour
    if second > 59:
        second = 0
        if minute > 59:
            minute = 0
            # get a new time from the network time server at 2:47 am each night
            if (hour == 2) and (minute == 24):
                display_message('Syncing time server')
                update()
            if hour > 23:
                hour = 0
            else:
                hour += 1
        else:
            minute += 1
