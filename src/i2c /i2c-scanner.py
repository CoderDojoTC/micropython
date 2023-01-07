# I2C Scanner
import machine
import time
import VL53L0X

sda=machine.Pin(26) # row one on our standard Pico breadboard
scl=machine.Pin(27) # row two on our standard Pico breadboard
i2c=machine.I2C(1, sda=sda, scl=scl, freq=400000)


# i2c.scan() returns a list of devices that have been found
# i2c.scan()[0] is the first device found
device_id = i2c.scan()[0]
print("Device found at decimal", device_id)

if device_id == 41:
    print("TEST PASS")
else:
    print("No device found at decimal 41")
    print("TEST FAIL")
