import tm1637
from machine import Pin
from utime import sleep, localtime
tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))
now = localtime()
hour = now[3]
if hour > 12:
    hour = hour - 12
minute = now[4]
sec = now[5]
print(hour, ':', minute, ' ', sec, sep='')
while True:
    tm.numbers(hour,minute,colon=True)
    sleep(0.5)
    tm.numbers(hour,minute,colon=False)
    sleep(0.5)
    sec = sec + 1
    if sec == 60:
        minute = minute + 1
        sec = 0
        if minute == 60:
            hour = hour + 1
            minute = 0
            if hour == 24:
                hour = 0