# Get the Weather Forecast

## Open Weather

https://openweathermap.org/weather-data

## Open Weather API

https://openweathermap.org/api

## One Call API
https://openweathermap.org/api/one-call-3

### Add Your Account ID to secrets.py

```python
import network
import secrets
from utime import sleep, ticks_ms, ticks_diff
import urequests

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

start = ticks_ms() # start a millisecond counter

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

delta = ticks_diff(ticks_ms(), start)

number = astronauts['number']
print('There are', number, 'astronauts in space.')
for i in range(number):
    print(i+1, astronauts['people'][i]['name'])
    
print("HTTP GET Time in milliseconds:", delta)
```

Returns:

```
There are 10 astronauts in space.
1 Oleg Artemyev
2 Denis Matveev
3 Sergey Korsakov
4 Kjell Lindgren
5 Bob Hines
6 Samantha Cristoforetti
7 Jessica Watkins
8 Cai Xuzhe
9 Chen Dong
10 Liu Yang
HTTP GET Time in milliseconds: 786
```