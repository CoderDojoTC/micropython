import machine
from utime import sleep
from ssd1306 import SSD1306_I2C

POT_PIN_1 = 26
POT_PIN_2 = 27
POT_PIN_3 = 28

adc_1 = machine.ADC(POT_PIN_1)
adc_2 = machine.ADC(POT_PIN_2)
adc_3 = machine.ADC(POT_PIN_3)

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

def read_pot(adc):
    return int(adc.read_u16()) >> 8

while True:
    oled.fill(0)
    oled.text("CoderDojo Robot", 0, 0)
    oled.text("P1:", 0, 20)
    oled.text(str(read_pot(adc_1)), 40, 20)
    oled.text("P2:", 0, 35)
    oled.text(str(read_pot(adc_2)), 40, 35)
    oled.text("P3:", 0, 50)
    oled.text(str(read_pot(adc_3)), 40, 50)
    oled.show()
    sleep(.1)

