# from NikoKun
# https://www.reddit.com/r/raspberrypipico/comments/11r9yck/raspberry_pi_pico_micropython_is_missing_several/
import ntptime, network
from machine import RTC
from utime import sleep_ms, time, localtime, mktime
import secrets

timeZone = -6
ntptime.host = 'us.pool.ntp.org' #'time.nist.gov' #'pool.ntp.org'
ntptime.timeout = 5

def wifiConnect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    #wifi.config(pm = 0xa11140) # disables wifi sleep mode
    if not wifi.isconnected():
        wifi.connect(secrets.SSID, secrets.PASS)
        print('Connecting..', end='')
        max_wait = 10
        while max_wait > 0:
            if wifi.status() < 0 or wifi.status() >= 3: break
            sleep_ms(1000)
            print('.', end='')
            max_wait -= 1
        print()
        if wifi.status() != 3: print('Could not connect to wifi!')
    print('Connected: ',wifi.isconnected(),'\nIP: ',wifi.ifconfig()[0])
    sleep_ms(100)
    return wifi

def dst():
    year, weekday = localtime()[0], localtime()[6]
    dst_start = mktime((year, 3, (8 - weekday) % 7 + 8, 2, 0, 0, 0, 0))
    dst_end = mktime((year, 11, (1 - weekday) % 7 + 1, 2, 0, 0, 0, 0))
    return dst_start <= time() < dst_end

def setRTCtime():
    timeset = False
    timetries = 0
    while not timeset and timetries < 5:
        timetries += 1
        try:
            ntptime.settime() # update time from ntp server
            timeset = True
        except:
            print('NTP update attempt #',timetries,'of 5 failed, retrying in 5 seconds..' if timetries < 5 else 'failed! Check connection/config.')
            if timetries < 5: sleep_ms(5000)
    if timeset:
        sleep_ms(100)
        rtc = RTC()
        tz_offset = (timeZone + 1) * 3600 if dst() else timeZone * 3600
        #tz_offset = timeZone * 3600 # without daylight savings
        myt = localtime(time() + tz_offset)
        rtc.datetime((myt[0], myt[1], myt[2], myt[6], myt[3], myt[4], myt[5], 0))
        sleep_ms(200)
        dtime = rtc.datetime()
        timestr = '%2d:%02d%s' %(12 if dtime[4] == 0 else dtime[4] if dtime[4] < 13 else dtime[4] - 12, dtime[5], 'AM' if dtime[4] < 12 else 'PM')
        datestr = f'{dtime[1]}/{dtime[2]}/{dtime[0] % 100}'
        print('Time set to:',timestr,datestr)
        return True
    print('Unable to update time.')
    return False


def update():
    wifi = wifiConnect()
    sleep_ms(100)
    if wifi.isconnected():
        success = setRTCtime()
        sleep_ms(100)
        wifi.disconnect() # If wifi is needed later,
        wifi.active(False) # comment these line out.
        if success: return True
    return False

if __name__ == '__main__':
    update()