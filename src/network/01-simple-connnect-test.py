import network
import secrets
from utime import sleep

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # power up the WiFi chip
print('Waiting for wifi chip to power up')
sleep(3) # wait three seconds for the chip to power up and initialize
wlan.connect(secrets.SSID, secrets.PASSWORD)
print('Waiting for access point to log us in.')
sleep(2)
if wlan.isconnected():
  print('Success! We have connected to your access point!')
  print('Try to ping the device at', wlan.ifconfig()[0])
else:
  print('Failure! We have not connected to your access point!  Check your secrets.py file for errors.')