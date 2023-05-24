# I2C Scanner
import machine
import time

sda=machine.Pin(2) # row one on our standard Pico breadboard
scl=machine.Pin(3) # row two on our standard Pico breadboard
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

# i2c.scan() returns a list of devices that have been found
# i2c.scan()[0] is the first device found
device_id = i2c.scan()
print("Device list:", device_id)

if device_id[0] == 60:
    print("Found I2C OLED Display at 60")
else:
    print("No display found.  Check your wiring.")


