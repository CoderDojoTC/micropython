# from https://github.com/rlangoy/uPy_APDS9960
from machine import Pin, I2C
import ssd1306
from time import sleep,sleep_ms
from APDS9960LITE import APDS9960LITE

#Init I2C Buss on RP2040
sda=Pin(12)
scl=Pin(13)
i2c=I2C(0, sda=sda, scl=scl, freq=400000)

print(i2c)
# create the driver
apds9960=APDS9960LITE(i2c)
apds9960.als.enableSensor()           # Enable Light sensor
sleep_ms(25)                          # Wait for readout to be ready

# display
WIDTH = 128
ONE_THIRD_WIDTH = int(WIDTH/3)
HEIGHT = 64
clock=Pin(2)
data=Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)
spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

def update_display(red, green, blue):
    oled.fill(0)
    # scale red, green and blue to the height
    red = int(red*4)
    green = int(green*4)
    blue = int(blue*3)
    
    oled.fill(0)
    # rect_fill(x, y, width, height)
    oled.fill_rect(0, HEIGHT - red, ONE_THIRD_WIDTH, red, 1)
    oled.fill_rect(ONE_THIRD_WIDTH, HEIGHT - green, ONE_THIRD_WIDTH, green, 1)
    oled.fill_rect(ONE_THIRD_WIDTH * 2, HEIGHT - blue, ONE_THIRD_WIDTH, blue, 1)
    oled.text(str(red), 0, 56, 0)
    oled.text(str(green), ONE_THIRD_WIDTH, 56, 0)
    oled.text(str(blue), ONE_THIRD_WIDTH*2, 56, 0)
    oled.show()

while True:
    # print(apds9960.als.ambientLightLevel,'', end='')
    red = apds9960.als.redLightLevel
    green = apds9960.als.greenLightLevel
    blue = apds9960.als.blueLightLevel
    update_display(red, green, blue)
    sleep(.05)