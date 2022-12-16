import network
import secrets
from utime import sleep

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print("Waiting for connection...")
    while not wlan.isconnected():
        time.sleep(.1)
        print("Waiting")

ac_list = wlan.scan()
for name in ac_list:
    print(name)
