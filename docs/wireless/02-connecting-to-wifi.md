# Connecting to a WiFi Network

### Setting Up Your WIFI secrets.py
By convention, we put both our SSID and password in a python file called "secrets.py".  This file should never be checked into a public source code repository.  We can add ```secrets.py``` to the .gitignore file to make sure the secrets.py is never checked into GitHub and exposing your passwords to everyone.

```python
SSID = "MY_WIFI_NETWORK_NAME"
PASSWORD = "MY_WIFI_PASSWORD"
```

By importing the secrets.py file you can then reference your network name like this:

```py
print('Connecting to WiFi Network Name:', secrets.SSID)
```

### Testing Your WiFi Access Point Connection

Here is a very simple script to test see if your network name and password are correct.  This script may work, but as we will see, it is both slow and potentially unreliable.

```python
import network
import secrets
from utime import sleep

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # power up the WiFi chip
print('Waiting for wifi chip to power up...')
sleep(3) # wait three seconds for the chip to power up and initialize
wlan.connect(secrets.SSID, secrets.PASSWORD)
print('Waiting for access point to log us in.')
sleep(2)
if wlan.isconnected():
  print('Success! We have connected to your access point!')
  print('Try to ping the device at', wlan.ifconfig()[0])
else:
  print('Failure! We have not connected to your access point!  Check your secrets.py file for errors.')
```

Returns:

```
Connecting to WiFi Network Name: MY_WIFI_NETWORK_NAME
Waiting for wifi chip to power up...
Waiting for access point to log us in...
Success! We have connected to your access point!
Try to ping the device at 10.0.0.70
```

If the result is a ```Failure``` you should check the name of the network and the password and that you are getting a strong WiFi signal where you are testing.

Note that we are using the ```sleep()``` function to insert delays into our code.  However, the results may actually be faster or slower than our sleep times.  Our next step is to add logic that will test to see if the networking device is ready and if our local access point allows us to login correctly.

### Waiting for a Valid Access Point Connection

Sometimes we want to keep checking if our access point is connected before we begin using our connection.  To do this we can create a while loop and continue in the loop while we are not connected.

```python
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
    counter = 0
    while not wlan.isconnected():
        sleep(1)
        print(counter, '.', sep='', end='', )
        counter += 1

delta = ticks_diff(ticks_ms(), start)
print("Connect Time:", delta, 'milliseconds')
print('IP Address:', wlan.ifconfig()[0])
```

This code also supports a timer that will display the number of seconds for the access point to become valid in the console.  The first time after you power on, this may take several seconds.  After you are connected the connection will be cached and the time will be 0 milliseconds.

First run upon power on might take several seconds:
```
>>> %Run -c $EDITOR_CONTENT
Connecting to WiFi Network Name: MY_NETWORK_NAME
Waiting for connection...
0.1.2.3.Connect Time: 4640
IP Address: 10.0.0.70
```

The second and consecutive runs will use a cached connection.

```
>>> %Run -c $EDITOR_CONTENT
Connecting to WiFi Network Name: MY_NETWORK_NAME
Connect Time: 0 milliseconds
IP Address: 10.0.0.70
>>>
```

### Error Handling

```python

lan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
  if wlan.status() < 0 or wlan.status() >= 3:
    break
  max_wait -= 1
  print('waiting for connection...')
  time.sleep(1)

# Handle connection error
if wlan.status() != 3:
   raise RuntimeError('network connection failed')
else:
  print('connected')
  status = wlan.ifconfig()
  print( 'ip = ' + status[0] )
```

The full TCP/IP stack is running on your Pico W.  You should be able to ping the pico using the IP address returned by the status[0] of the wlan.ifconfig() function above.
