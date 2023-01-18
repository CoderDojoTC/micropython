# from https://github.com/rlangoy/uPy_APDS9960
import machine
from time import sleep,sleep_ms
from APDS9960LITE import APDS9960LITE

#Init I2C Buss on RP2040
sda=machine.Pin(12)
scl=machine.Pin(13)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

print(i2c)
# create the driver
apds9960=APDS9960LITE(i2c)
print('done crearing the driver')
print(apds9960)
apds9960.prox.enableSensor()    # Enable Proximit sensing
print('enable the sensor')

#apds9960.powerOn(True)
#print(apds9960.statusRegister())

while True:
    
        sleep(.1) # wait for readout to be ready
        print(apds9960.prox.proximityLevel)   #Print the proximity value