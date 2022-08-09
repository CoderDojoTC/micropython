# create a web get request and test the response
import requests
import sys
import json
import time
import secrets

base = 'http://api.openweathermap.org/data/2.5/forecast'
location = '524901' # twin cities
url = base + '?id=' + location + '&APPID=' + secrets.appid

print('url: ' + url)

response = requests.get(url)
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    print(url)
    sys.exit()

print(response.json() ['list'][0]['weather'][0]['description'])