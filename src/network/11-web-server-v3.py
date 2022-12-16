# Code taken from https://www.cnx-software.com/2022/07/03/getting-started-with-wifi-on-raspberry-pi-pico-w-board/
import network
import socket
from time import sleep
import secrets

from machine import Pin

# Select the onboard LED
led = machine.Pin("LED", machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(False)
sleep(1)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
stateis = "LED is OFF"

html = """<!DOCTYPE html>
<html>
   <head>
     <title>Web Server On Pico W </title>
   </head>
  <body>
      <h1>Pico Wireless Web Server</h1>
      <p>State: %s</p>
      <a href="/light/on">Turn On</a>
      <a href="/light/off">Turn Off</a><br/>
      
      <a href="/led/red/on">Red LED On</a>
      <a href="/led/red/off">Red LED Off</a><br/>
      
      <a href="/led/green/on">Green LED On</a>
      <a href="/led/green/off">Green LED Off</a><br/>
      
      <a href="/led/blue/on">Blue LED On</a>
      <a href="/led/blue/off">Blue LED Off</a>
  </body>
</html>
"""

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
  if wlan.status() < 0 or wlan.status() >= 3:
    break
  max_wait -= 1
  print('waiting for connection...')
  sleep(1)

# Handle connection error
if wlan.status() != 3:
  raise RuntimeError('network connection failed')
else:
  print('We are connected to WiFI access point:', secrets.SSID)
  status = wlan.ifconfig()
  print( 'The IP address of the pico W is:', status[0] )

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
# print('addr:', addr)

s = socket.socket()
# this prevents the "OSError: [Errno 98] EADDRINUSE" error for repeated tests
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Got a sockert.  s:', s)

#if not addr:

print('going to run bind to addr on the socket')
s.bind(addr)

print('going to run listen(1) on socket')
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
  try:
    cl, addr = s.accept()
    # print('client connected from', addr)
    request = cl.recv(1024)
    # print(request)
    request = str(request)
    led_on = request.find('/light/on')
    led_off = request.find('/light/off')
    
    red_on = request.find('/led/red/on')
    red_off = request.find('/led/red/off')
    
    green_on = request.find('/led/green/on')
    green_off = request.find('/led/green/off')
    
    blue_on = request.find('/led/blue/on')
    blue_off = request.find('/led/blue/off')

    # print( 'led on = ' + str(led_on))
    # print( 'led off = ' + str(led_off))

    if led_on == 6:
      print("led on")
      led.value(1)
      stateis = "LED is ON"

    if led_off == 6:
        print("led off")
        led.value(0)
        stateis = "LED is OFF"
    
    if red_on == 6:
        print("red on")
    if red_off == 6:
        print("red off")

    if green_on == 6:
        print("green on")
    if green_off == 6:
        print("green off")

    if blue_on == 6:
        print("blue on")
    if blue_off == 6:
        print("blue off")
    
    # generate the we page with the stateis as a parameter
    response = html % stateis
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()

  except OSError as e:
    cl.close()
    s.close()
    print('connection closed')