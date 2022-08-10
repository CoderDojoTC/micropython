# create a web get request and test the response
import requests
import sys
import json
import time
import secrets

base = 'http://api.openweathermap.org/data/2.5/forecast?units=imperial&'
location = '5037649' # twin cities
url = base + 'id=' + location + '&appid=' + secrets.appid

print('url: ' + url)

response = requests.get(url)
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    print(url)
    sys.exit()

# Our response data in JSON format
jd = response.json()

date_time_int = int(jd['list'][0]['dt'])
timezone = int(jd['city']['timezone'])
print('date time int', date_time_int, 'timezone:', timezone)

print('City:', response.json() ['city']['name'])

""" 
for i in range(0, 12):
    print('temp:', response.json() ['list'][i]['main']['temp'])
    print('feels like:', response.json() ['list'][i]['main']['feels_like'])
    print(response.json() ['list'][i]['weather'][0]['description'])
    print('DateTime:', response.json() ['list'][i]['dt_txt'])
    print() 
"""
for i in range(0, 16):
    localtime = int(jd['list'][i]['dt']) + timezone
    print(time.gmtime(localtime), ' ', sep='', end='')
    print()

for i in range(0, 16):
    print(jd['list'][i]['dt_txt'][5:13], ' ', sep='', end='')
print()
for i in range(0, 16):    
    print(round(jd['list'][i]['main']['temp']), '      ', end='')