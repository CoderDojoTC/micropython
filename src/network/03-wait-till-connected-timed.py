import network
import secrets
from utime import sleep, ticks_ms, ticks_diff

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

start = ticks_ms() # start a millisecond counter

if not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print("Waiting for connection...")
    while not wlan.isconnected():
        sleep(.1)
        print("Waiting")

delta = ticks_diff(ticks_ms(), start)
print("Connect Time:", delta)
print(wlan.ifconfig())