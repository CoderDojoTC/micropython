# Getting Your MAC Address

## What is a MAC Address?
Every device that works with Ethernet and WiFi must have a [Wikipedia Page on MAC Address](https://en.wikipedia.org/wiki/MAC_address).

A MAC address (media access control address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, Wi-Fi, and Bluetooth.

!!! Note
    The MAC address has nothing to do with the Apple Macintosh or Mac OS.  They just use the same name to mean different things.

Understanding how devices use MAC addresses is essential to understanding how networks work and debugging them.

The MAC address is six bytes or "octets".  The first three octets are assigned to the organization that created the device.  The second three octets are assigned by the organization that created the device.  See the [Wikipedia Page on MAC Address](https://en.wikipedia.org/wiki/MAC_address) for more information.  If you run this on your Pico W the first octets should be similar.

Here are the two MAC addresses for two different Pico W devices that were purchase together:

```
28:cd:c1:1:35:54
28:cd:c1:1:35:58
```

Because they were purchased together, their MAC address are very similar and only differ in the last few bits.  A MAC address often can give clues about the origins of packets on your network.

## Getting the MAC/Ethernet Access

You can get the device MAC/Ethernet address and test the roundtrip time between the RP2040 and the WiFi chip using the MAC address function.

```python
import network
from utime import sleep, ticks_us, ticks_diff

print('Getting MAC/Ethernet Address for this device.')

start = ticks_us() # start a millisecond counter
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # this line powers up the chip - it takes about 2.5 seconds

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
```

First Time After Power On Results:
```
Getting MAC/Ethernet Address for this device.
Time in microseconds: 2584424
Hex byte array: b'(\xcd\xc1\x015X' length: 6
28:cd:c1:1:35:58
```

Note that it takes about 2.5 seconds just to power on the chip before we get the MAC address.

Subsequent Times
```
Getting MAC/Ethernet Address for this device.
Time in microseconds: 211
Hex byte array: b'(\xcd\xc1\x015X' length: 6
28:cd:c1:1:35:58
```

!!! Note
    We must add the ```wlan.active(True)``` line to this code.  If we don't do this, the wifi device will not be powered up and we can't get the MAC address.  The function will return all zeros.


I ran this program on my Pico W and I got times of between 214 and 222 microseconds.  This shows you that it takes about 100 microseconds to send a request from the RP2040 to the CYW43439 WiFi chip and about 100 milliseconds to return the results.  This time lag represents some of the key performance limitations in using the Pico W for high-performance networking.