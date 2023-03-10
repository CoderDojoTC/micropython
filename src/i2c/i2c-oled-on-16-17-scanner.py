import machine
sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

# i2c.scan() returns a list of devices that have been found
# i2c.scan()[0] is the first device found
device_id_list = i2c.scan()
for device_id in device_id_list:
    print("Found I2C Device at:", device_id)
    
print("Device found at decimal", device_id)

if device_id_list[0] == 41:
    print("TEST PASS!")
    print("We have found an Time of Flight Sensor using pins 16 and 17 for SDA and SCL.")
    print("Your SDA and SCL lines are connected correctly.")
else:
    print("No device found at decimal 60")
    print("TEST FAIL")
