import network
import secrets
from utime import sleep, ticks_us, ticks_diff

print('Getting Mac Address for device.')

start = ticks_us() # start a millisecond counter
wlan = network.WLAN(network.STA_IF)
mac_addess = wlan.config('mac')
print('Time in microseconds:', ticks_diff(ticks_us(), start))
print(mac_addess)

