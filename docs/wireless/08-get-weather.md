# Get the Weather Forecast

This demo uses the free web service [Open Weather Map](http://openweathermap.org).

The Open Weather Map service returns the predicted temperatures and conditions (sun, cloudy, rain etc.) for three hour intervals for the next 40 intervals at your specified location.

You can see this using the UNIX curl command:

```sh
curl 'http://api.openweathermap.org/data/2.5/forecast?\
      units=imperial&\
      id=5037649&\
      appid=f2b1...'
```

In this example, we are asking it to use US standard Fahrenheit (imperial units) for the city with id 5037649 which is Minneapolis, MN in the USA.  You can use the Open Weather site to find the id for your city or specify the long and lat of the point you want to get weather forecasts for.  You can also use the [GeoNames](https://www.geonames.org/5037649/minneapolis.html) to find your city ID number.

## How to Use the Open Weather Map API

To use this service, you must register and get an API key.  You then put your key in the secrets.py file:

Content of secrets.py
```python
appid='f2b1...'
```

The secrets.py file is then imported into your program.  Make sure to put secrets.py into your .gitignore file so it will not be checked into your public GitHub repo.

The URL for the service is then created by concatenating the base URL, the city location ID and the application id:

```python
base = 'http://api.openweathermap.org/data/2.5/forecast?units=imperial&'
location = '5037649' # GeoNames ID for Minneapolis in Minnesota, USA
url = base + 'id=' + location + '&appid=' + secrets.appid
```

## Parsing the JSON file

The service returns a JSON file with the following format:

```json
{
    "cod": "200",
    "message": 0,
    "cnt": 40,
    "list": [
        {
            "dt": 1660078800,
            "main": {
                "temp": 80.83,
                "feels_like": 81.23,
                "temp_min": 80.83,
                "temp_max": 84.67,
                "pressure": 1019,
                "sea_level": 1019,
                "grnd_level": 988,
                "humidity": 47,
                "temp_kf": -2.13
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 6.08,
                "deg": 226,
                "gust": 6.38
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-08-09 21:00:00"
        }, 
        /* ...repeated 40 times */
        ,
    "city": {
        "id": 5037649,
        "name": "Minneapolis",
        "coord": {
            "lat": 44.98,
            "lon": -93.2638
        },
        "country": "US",
        "population": 0,
        "timezone": -18000,
        "sunrise": 1660043269,
        "sunset": 1660094963
    }
}
```

The bulk of the data is in the list structure with 40 items with a small set of data before and after the list.  The data about the HTTP status (200) and the count (40) is before the list and the data about the city is after the list.

Each block of data in the list JSON object contains data about the main data (temperature, min, max, pressure, humidity), cloud cover, wind speed and visibility.  It is up to you to decide what data you would like to display within this data.  Once you decide what data you want to access you can use JSON path statements to pull the right data out.  For example to get the main temperature for each time period you would run:

```python
# get the temp and humidity for the next 40 3-hour intervals
for i in range(0, 39):
    print('temp:', weather['list'][i]['main']['temp'], end='')
    print('humidity:', weather['list'][i]['main']['humidity'])
```

## Sample Output

Here is the output on the Thonny shell of the first 16 temperature values:

![Network Weather Results](../img/network-weather-results.png)

## Plotting the Forecast with Thonny Plot

Here is a plot of the temp and the "feels like" temp using the Thonny Plotter panel.

![Wireless Forecast Thonny Plot](../img/network-forecast-thonny-plot.png)

Each line has:

1. a label string
2. a colon
3. the numeric value 
   
for each value plotted.  There can be multiple values per line.

Here is that format:

```
Temperature: 63 Feels Like:  63.52
Temperature: 62 Feels Like:  62.56
Temperature: 70 Feels Like:  69.69
```

## Sample Code

```python
import network
import secrets
import urequests
from utime import sleep, ticks_ms, ticks_diff

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

start = ticks_ms() # start a millisecond counter

if not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print("Waiting for connection...")
    counter = 0
    while not wlan.isconnected():
        sleep(1)
        print(counter, '.', sep='', end='', )
        counter += 1

delta = ticks_diff(ticks_ms(), start)
print("Connect Time:", delta, 'milliseconds')
print("IP Address:", wlan.ifconfig()[0])

base = 'http://api.openweathermap.org/data/2.5/forecast?units=imperial&'
location = '5037649' # twin cities
url = base + 'id=' + location + '&appid=' + secrets.appid

weather = urequests.get(url).json()
print('City:', weather['city']['name'])
print('Timezone:', weather['city']['timezone'])

max_times = 16
# for i in range(0, 39):
for i in range(0, max_times):
    print(weather['list'][i]['dt_txt'][5:13], ' ', sep='', end='')
print()
for i in range(0, max_times):    
    print(round(weather['list'][i]['main']['temp']), '      ', end='')
    # print('feels like:', weather['list'][i]['main']['feels_like'])
    # print(weather['list'][i]['weather'][0]['description'])
    # print(weather['list'][i]['dt_txt'])
    
# print(weather)
```

## Displaying Predicted Temperatures in a Thonny Plot

Thonny has a [Plot object](https://github.com/thonny/thonny/blob/707e69ec3a567df5f82205c5a2ae0d79f186ed25/thonny/plugins/help/plotter.rst) that you can use to display the relative temperature for the next 40 3-hour cycles.

To do this, we only need to print out the temperatures each on a separate line:

```python
print()
for i in range(0, max_times):    
    print(round(weather['list'][i]['main']['temp']))
```