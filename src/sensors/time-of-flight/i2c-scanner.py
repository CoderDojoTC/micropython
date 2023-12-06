import machine
sda=machine.Pin(0) # row one on our standard Pico breadboard
scl=machine.Pin(1) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl)
print('i2c result:', i2c)
address = i2c.scan()
print('Scan result:', address)
decimal = address[0]
hex = hex(decimal)
print('The VL53L0X has expected values of decimal 41 and hex 0x29')
print("Device found at decimal: ", i2c.scan(), decimal, hex)
if (decimal == 41):
    print('PASS')
else:
    print('FAIL')
