import network
import secrets
import time
import urequests
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
number = astronauts['number']
print('There are', number, 'astronauts in space.')
for i in range(number):
    print(astronauts['people'][i]['name'])