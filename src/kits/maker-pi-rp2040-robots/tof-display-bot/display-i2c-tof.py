import machine
import VL53L0X
from time import sleep
from ssd1306 import SSD1306_I2C

# setup the 1st I2C interface

# this is the servo data pin in the corner of the Cytron RP2040
OLED_RESET = machine.Pin(15, machine.Pin.OUT)
# optional set to low
OLED_RESET.low()
# optional delay here to keep it low
sleep(0.01)
OLED_RESET.high()

i2c_oled = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
print (i2c_oled.scan())
oled = SSD1306_I2C(128, 64, i2c_oled)
# oled.text('CoderDojo Rocks!', 0, 0)
# oled.text('128x64 i2C', 0, 20)
# oled.show()

sda=machine.Pin(26) # lower right pin
scl=machine.Pin(27) # one up from lower right pin
i2c_tof=machine.I2C(1, sda=sda, scl=scl, freq=400000)
print(i2c_tof)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_tof)
tof.start()

counter = 0
while True:
    oled.fill(0)
    oled.text('CoderDojo Rocks!', 0, 0)
    oled.text(str(counter), 0, 10)
    distance = tof.read()
    oled.text(str(distance), 0, 20)
    oled.show()
    sleep(.1)
    counter += 1

