import network
import secrets
from utime import sleep, ticks_ms, ticks_diff

ticks_diff(ticks_ms(), start)

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
print(wlan.config('mac'))
delta = ticks_diff(ticks_ms(), start)
print(delta)