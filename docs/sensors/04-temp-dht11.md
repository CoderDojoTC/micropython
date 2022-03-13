# Sensing Temperature and Humidity with the DHT11 Sensor

## Sample Code

```py
from machine import Pin
import utime as time
from dht import DHT11, InvalidChecksum

DHT_PIN = 15
# this is a bit odd, since although it is an input, we need a pull down set
dhtSensor = DHT11(Pin(DHT_PIN, Pin.OUT, Pin.PULL_DOWN))

while True:
    temp = dhtSensor.temperature
    humidity = dhtSensor.humidity/100
    print("Temp: {}°C".format(temp),  "| Hum: {0:.1%}".format(humidity))
```

## References

* [Peppe80's Example](https://peppe8o.com/dht11-humidity-and-temperature-sensor-with-raspberry-pi-pico-and-micropython/)
* [Axel Örn Sigurðsson's DHT11 Driver](https://raw.githubusercontent.com/ikornaselur/pico-libs/master/src/dht11/dht.py)