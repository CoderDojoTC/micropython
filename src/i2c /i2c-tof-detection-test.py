import machine

# Change these pin number to match your hardware setup
SDA_PIN = 16
SCL_PIN = 17
sda=machine.Pin(SDA_PIN) # row one on our standard Pico breadboard
scl=machine.Pin(SCL_PIN) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

# i2c.scan() returns a list of devices that have been found
# i2c.scan()[0] is the first device found

print("Using I2C SDA Pin:", SDA_PIN)
print("Using I2C SCL Pin:", SCL_PIN)
device_id_list = i2c.scan()
for device_id in device_id_list:
    print("Found I2C Device at:", device_id)
    
print("Device found at decimal", device_id)

if device_id_list[0] == 41:
    print("TEST PASS!")
    print("We have found an Time of Flight Sensor using pins 16 and 17 for SDA and SCL.")
    print("Your SDA and SCL lines are connected correctly.")
else:
    print("No Time of Flight device found at decimal 41 using these SDA and SCL pins.")
    print("TEST FAIL")
