import network
import secrets
from utime import sleep, ticks_us, ticks_diff

print('Getting MAC/Ethernet Address for this device.')

start = ticks_us() # start a millisecond counter
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # power up the chip

# This returns a byte array of hex numbers
mac_addess = wlan.config('mac')
print('Time in microseconds:', ticks_diff(ticks_us(), start))
# each MAC address is 6 bytes or 48 bits
print("Hex byte array:", mac_addess, 'length:', len(mac_addess))

# This should be in hex per the Notational Conventions
# https://en.wikipedia.org/wiki/MAC_address#Notational_conventions
# b'(\xcd\xc1\x015X'
# 28:cd:c1:1:35:58
# format in MAC Notational Convention
for digit in range(0,5):
    print(str(hex(mac_addess[digit]))[2:4], ':', sep='', end = '')
print(str(hex(mac_addess[5]))[2:4] )