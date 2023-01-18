import network
import ssd1306
import secrets
import urequests
from utime import sleep, ticks_ms, ticks_diff

# startup

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

WIDTH = 128
HEIGHT = 64
SCK=machine.Pin(2)
SDL=machine.Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDL)


oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)
oled.poweron()

def display_startup(counter):
    oled.fill(0)
    oled.text('Running startup', 0, 10, 1)
    oled.text('Connecting to', 0, 20, 1)
    oled.text(secrets.SSID, 0, 30, 1)
    oled.text(str(counter), 0, 40, 1)
    oled.show()
    
def display_status(counter):
    oled.fill(0)
    # display the network name
    oled.text('n:' + secrets.SSID, 0, 0, 1)

    # display the connection time
    oled.text('t:', 0, 10, 1)
    oled.text(str(connection_time)+ ' ms', 15, 10, 1)
    oled.show()

def display_weather():
    global weather, city, current_temp
    oled.fill(0)
    min = 120
    max = -50
    for i in range(0, 39):
        temp = round(weather['list'][i]['main']['temp'])
        if temp < min:
            min = temp
        if temp > max:
            max = temp
    min = round(min)
    max = round(max)
    temp_range_height = max - min
    graph_height = 54
    scale = graph_height/temp_range_height
    print('min/max/range/scale:', min, max, temp_range_height, scale)
    
    # display city name, current temp, min and max
    oled.text(city + ': ' + str(current_temp), 0, 0, 1)
    oled.text(str(min), 0, 57, 1) # bottom left corner
    oled.text(str(max), 0, 10, 1) # under top row
    
    max_points = 39
    
    # graph temps for the next n periods
    print('Date          Tmp TNx   Y  Y2  Del')
    for i in range(0, max_points):
        temp = round(weather['list'][i]['main']['temp'])
        x = i * 3 # scaled x
        y = 63 - round((temp - min)*scale)
        oled.pixel(x, y, 1)
        
        # now draw the next two points
        if i < max_points:
            temp_next = round(weather['list'][i+1]['main']['temp'])
            y_next = 63 - round((temp_next - min)*scale)
        y_delta = -round((y - y_next)/3) # a small positive or negative number
        
        print(weather['list'][i]['dt_txt'][0:13],
              '{: 3.3d}'.format(temp),
              '{: 3.3d}'.format(temp_next),
              '{: 3.3d}'.format(y),
              '{: 3.3d}'.format(y_next),
              '{: 3.3d}'.format(y_delta))
        
        # should be 1/3 of the way to the next point
        oled.pixel(x+1, y + y_delta, 1)
        # should be 2/3 of the way to the next point
        oled.pixel(x+2, y + 2*y_delta, 1)
    oled.show()
    
start = ticks_ms() # start a millisecond counter

if not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print("Waiting for connection...")
    counter = 0
    while not wlan.isconnected():
        sleep(1)
        print(counter, '.', sep='', end='', )
        counter += 1
        display_startup(counter)

delta = ticks_diff(ticks_ms(), start)
#print("Connect Time:", delta, 'milliseconds')
#print("IP Address:", wlan.ifconfig()[0])

base = 'http://api.openweathermap.org/data/2.5/forecast?units=imperial&'
location = '5037649' # twin cities
url = base + 'id=' + location + '&appid=' + secrets.appid
#print(url)

max_times = 39
#for i in range(0, max_times):    
    #print(' Temp: ', weather['list'][i]['main']['temp'])

while True:
    # globals: weather, city, current_temp
    weather = urequests.get(url).json()
    # print(weather)
    city = weather['city']['name']
    current_temp = round(weather['list'][0]['main']['temp'])
    display_weather()
    print('Going to sleep for one hour')
    sleep(3600) # sleep one hour