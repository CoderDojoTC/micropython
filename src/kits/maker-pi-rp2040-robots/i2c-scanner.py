import machine

I2C0_SDA_PIN = 0
I2C0_SCL_PIN = 1
I2C1_SDA_PIN = 2
I2C1_SCL_PIN = 3
i2c0=machine.I2C(0,sda=machine.Pin(I2C0_SDA_PIN), scl=machine.Pin(I2C0_SCL_PIN), freq=400000)
i2c1=machine.I2C(1,sda=machine.Pin(I2C1_SDA_PIN), scl=machine.Pin(I2C1_SCL_PIN), freq=400000)

print('Scanning I2C bus 0.')
devices = i2c0.scan() # this returns a list of devices

device_count = len(devices)

if device_count == 0:
    print('No i2c device found on bus 0.')
else:
    print(device_count, 'devices found.')

for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))

print('Scanning I2C bus 1.')
devices = i2c1.scan() # this returns a list of devices

device_count = len(devices)

if device_count == 0:
    print('No i2c device found on bus 1.')
else:
    print(device_count, 'devices found.')

for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))