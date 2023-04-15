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
apds9960.als.enableSensor()           # Enable Light sensor
sleep_ms(25)                          # Wait for readout to be ready

#apds9960.powerOn(True)
#print(apds9960.statusRegister())

while True:
    print(apds9960.als.ambientLightLevel,'', end='')
    print(apds9960.als.redLightLevel,'', end='')
    print(apds9960.als.greenLightLevel,'', end='')
    print(apds9960.als.blueLightLevel)
    sleep(.1)
