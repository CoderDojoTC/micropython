# Wireless

![Raspberry Pi Pico W](../img/pico-w.png)

One June 30th, 2022 the [Raspberry Pi Foundation announced](https://www.raspberrypi.com/news/raspberry-pi-pico-w-your-6-iot-platform/) the availability of the Raspberry Pi Pico W.  This $6 microprocessor now supports WiFi and with a software upgrade it may also support Bluetooth.

The Pico W supports 802.11n wireless networking.  For MicroPython, we can use a MicroPython library built around the [lwip](https://savannah.nongnu.org/projects/lwip/) TCP/IP stack.  This stack is accessible using the MicroPython [network](https://docs.micropython.org/en/latest/library/network.html#) functions.

## Compatibility with Prior Code

The Pico W code is very similar to prior versions of the Pico with a few small exceptions.  One of these is the fact that we must now use a symbolic label called an **alias* such as ```Pin("LED")``` instead of ```Pin(25)``` to access the LED pin, not a hardwired PIN number.  This allows us to keep our code more portable as the underlying hardware changes.

```python
from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
```

See the new [Sample Blink]
(https://github.com/raspberrypi/pico-micropython-examples/blob/master/blink/blink.py) code on the Raspberry Pi Examples site.

## Getting the New Pico W Image

I had to download a brand new image for the Pico W runtime from [the Raspberry Pi Foundation Software Site](https://githubdatasheets.raspberrypi.com/soft/micropython-firmware-pico-w-290622.uf2)

After I downloaded the new image and ran a Reset on Thonny I got the following prompt:

```sh title="reset shell prompt"
MicroPython v1.19.1-88-g74e33e714 on 2022-06-30; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> 
```

Note that the "Pico W" is mention in the prompt.

## Sample Code

We will store the name of our local WiFi network we wish to connect to and the password for that name in a file called secrets.py.  This is called you WiFi "access point" and the variable name to store the name is called the ```SSID``.  We will need to make sure we never save this file into a public GitHub repo by adding this file to our .gitignore file.

### Setting Up Your WIFI Secrets.py
secrets.py:
```python
SSID = "MY_WIFI_NETWORK_NAME"
PASSWORD = "MYWIFIPASSWORD"
```

By importing the secrets.py file you can then reference your network name like this:

```py
print('Connecting to WiFi Network Name:', secrets.SSID)
```

## Testing Your Connection

```python title="test-access-point-connection.py"
import network
import secrets
from utime import sleep

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
sleep(1) # wait a second to wait for a connection
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
```

Returns:

```
Connecting to WiFi Network Name: MY_WIFI_NETWORK_NAME
True
```

If the value is ```False``` you should check the name of the network and the password and that you are getting a strong WiFi signal where you are testing.

## Waiting for a Valid Access Point Connection
Sometimes we want to keep checking if our access point is connected before we begin using our connection.  To do this we can create a while loop and continue in the loop while we are not connected.

```py title="time-access-point-connection.py"
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
```

This code also supports a timer that will display the number of milliseconds for the access point to become valid.  The first time after you power on, this may take several seconds.  After you are connected the connection will be cached and the time will be 0 milliseconds.

## Testing HTTP GET

The following example was taken from [Tom's Hardware](https://www.tomshardware.com/how-to/connect-raspberry-pi-pico-w-to-the-internet)

```py title="test-http-get.py"
import network
import secrets
from utime import sleep, ticks_ms, ticks_diff
import urequests

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

start = ticks_ms() # start a millisecond counter

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

delta = ticks_diff(ticks_ms(), start)

number = astronauts['number']
print('There are', number, 'astronauts in space.')
for i in range(number):
    print(i+1, astronauts['people'][i]['name'])
    
print("HTTP GET Time in milliseconds:", delta)
```

Returns:

```
There are 10 astronauts in space.
1 Oleg Artemyev
2 Denis Matveev
3 Sergey Korsakov
4 Kjell Lindgren
5 Bob Hines
6 Samantha Cristoforetti
7 Jessica Watkins
8 Cai Xuzhe
9 Chen Dong
10 Liu Yang
HTTP GET Time in milliseconds: 786
```

## Getting a JSON Document with SHTTP GET

```python
import network
import secrets
import time
import urequests
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
my_ip = urequests.get("https://api.myip.com/").json()
print(im_pi)
```

## Listing the Functions in Your Network Library
The network library provided by the Raspberry Pi Foundation for the Pico W is new an may change as new functions are added.  To get the list of functions in your network library you can use the Python help(network) at the prompt or use the ```dir()``` function.

### Network Help

```
help(network)
object <module 'network'> is of type module
  __name__ -- network
  route -- <function>
  WLAN -- <class 'CYW43'>
  STAT_IDLE -- 0
  STAT_CONNECTING -- 1
  STAT_WRONG_PASSWORD -- -3
  STAT_NO_AP_FOUND -- -2
  STAT_CONNECT_FAIL -- -1
  STAT_GOT_IP -- 3
  STA_IF -- 0
  AP_IF -- 1
```

### Network dir() Function
```python
import network
function_list = dir(network)

for function in function_list:
    print(function)
```

Returns:

```
__class__
__name__
AP_IF
STAT_CONNECTING
STAT_CONNECT_FAIL
STAT_GOT_IP
STAT_IDLE
STAT_NO_AP_FOUND
STAT_WRONG_PASSWORD
STA_IF
WLAN
route
```

## Urequest
It is easy to communicate with non-SSL protected HTTP protocols sites using the urequest function.  It supports the standard GET, POST, PUT and DELETE functions.

```
help(urequests)
object <module 'urequests' from 'urequests.py'> is of type module
  head -- <function head at 0x2000b740>
  post -- <function post at 0x2000ba80>
  delete -- <function delete at 0x2000bbb0>
  get -- <function get at 0x2000b750>
  __file__ -- urequests.py
  Response -- <class 'Response'>
  patch -- <function patch at 0x2000baf0>
  put -- <function put at 0x2000ba90>
  usocket -- <module 'lwip'>
  __name__ -- urequests
  request -- <function request at 0x2000bb80>
  ```