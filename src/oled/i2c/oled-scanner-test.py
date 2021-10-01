import machine
sda=machine.Pin(0) # row one on our standard Pico breadboard
scl=machine.Pin(1) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

# i2c.scan() returns a list of devices that have been found
# i2c.scan()[0] is the first device found
devices = i2c.scan()
print("Device found at decimal", devices)

first_device = devices[0]
if first_device == 60:
    print("TEST PASS")
else:
    print("No OLED device found at decimal 60.  Check connections.")
    print("TEST FAIL")
