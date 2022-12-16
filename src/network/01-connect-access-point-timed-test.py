import network
import secrets
from utime import sleep, ticks_ms, ticks_diff

start = ticks_ms() # start a millisecond counter

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print("Waiting for connection...")
    counter = 0
    while not wlan.isconnected():
        sleep(1)
        counter += 1
        print(counter, '.', sep='', end='')

print('Connected to', secrets.SSID)
print('Total connect milliseconds:', ticks_diff(ticks_ms(), start))