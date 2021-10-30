# I2C Scanner Test

How do we know that our connection to the distance sensor is wired correctly?  The quick way to test this is to run a program called the I2C scanner.  It will return a list of all the devices it finds on the I2C bus.

We first run the I2C scanner program to verify that the sensor is connected correct and is responding to the I2C bus scan.

```py
import machine
# Pins on the Grove Connector 1 on the Maker Pi RP2040 are GP0 and GP1
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("I2C device ID list:", i2c.scan())
```

This should return a list of the devices it finds.  If you just have the Time-of-Flight sensor it will look like this:

```
[41]
``

```py
device_id = i2c.scan()[0]
```

## Testing for the Time-of-Flight Sensor

```py
import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

# i2c.scan() returns a list of devices that have been found
# i2c.scan()[0] is the first device found
device_id = i2c.scan()[0]
print("Device found at decimal", device_id)

if device_id == 41:
    print("TEST PASS")
else:
    print("No device found at decimal 41")
    print("TEST FAIL")
```
