import requests
import sys
import json
import time
import secrets

base = 'https://timeapi.io/api/Time/current/zone'
timeZone='America/Chicago'
url = base + '?timeZone=' + timeZone

response = requests.get(url)
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    print(url)
    sys.exit()

j = response.json()

#print(j)

date = j['date']

localtime = j['time']

print('The time in', timeZone, 'is', localtime , 'on', date)