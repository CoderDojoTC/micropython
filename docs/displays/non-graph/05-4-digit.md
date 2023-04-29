# Four Digit LED Display

In this lesson, we will use a 4-digit LED display to create a clock that displays the time of day.  These clocks will use the **tm1637** library to communicate
with the four-digit display.  Some of these displays also have a "colon"
between the hour and minute digits that flashes every second.

You can purchase 4-digit LED displays on eBay for about $2 each.

![](../img/4-digit-led-display.png)
![](../img/4-digit-led-display-clock.png)

![](./img/../../../img/4-digit-7-segment-colon.png)

```py
from machine import Pin
from time import sleep
import tm1637

DIO_PIN = 0
CLK_PIN = 1

DELAY = 0.5

tm = tm1637.TM1637(clk=Pin(CLK_PIN), dio=Pin(DIO_PIN))

# all segments off
tm.write([1, 2, 3, 4])
```

## Clock

We can create a simple clock by using the ```localtime()``` function when the
programs first starts up and then we just update the time after the sleep() functions run for a second.  This also can updates the colon between the hours
and minutes.

![4 Digit Clock](../../img/4-digit-clock.png)

```py
# a simple clock that only grabs the time from the server on startup
import tm1637
from machine import Pin
from utime import sleep, localtime

tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))

now = localtime()
hour = now[3]
# use AM/PM
if hour > 12:
    hour = hour - 12
minute = now[4]
sec = now[5]
print(hour, ':', minute, ' ', sec, sep='')

# update from the first time
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
```

A more accurate version will access the new time from the server every minute.

## Accurate Clock
```py
# a more accurate clock that only grabs the time from the server once per minute
import tm1637
from machine import Pin
from utime import sleep, localtime

hour = 0
minute = 0
sec = 0

def update_time():
    global hour, minute, second
    now = localtime()
    hour = now[3]
    # use AM/PM
    if hour > 12:
        hour = hour - 12
    minute = now[4]
    sec = now[5]

tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))

update_time()
# loop every second
while True:
    tm.numbers(hour,minute,colon=True)
    sleep(0.5)
    tm.numbers(hour,minute,colon=False)
    sleep(0.5)
    sec = sec + 1
    if sec == 60:
        # get the new time from the host
        update_time()
        print(hour, ':', minute, ' ', sec, sep='')
        minute = minute + 1
        sec = 0
        if minute == 60:
            hour = hour + 1
            minute = 0
            if hour == 24:
                hour = 0
```

## References

* [Nerd Cave YouTube Tutorial](https://www.youtube.com/watch?v=D68XtvZlk00)
* [Mike Causer's GitHub Repo with TM-1637 driver](https://github.com/mcauser/micropython-tm1637)