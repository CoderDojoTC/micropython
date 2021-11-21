import machine
from utime import sleep
from ssd1306 import SSD1306_I2C
import VL53L0X

POT_PIN_1 = 26
POT_PIN_2 = 27
POT_PIN_3 = 28

adc_1 = machine.ADC(POT_PIN_1)
adc_2 = machine.ADC(POT_PIN_2)
adc_3 = machine.ADC(POT_PIN_3)

I2C0_SDA_PIN = 0
I2C0_SCL_PIN = 1
I2C1_SDA_PIN = 2
I2C1_SCL_PIN = 3
i2c0=machine.I2C(0,sda=machine.Pin(I2C0_SDA_PIN), scl=machine.Pin(I2C0_SCL_PIN))
i2c1=machine.I2C(1,sda=machine.Pin(I2C1_SDA_PIN), scl=machine.Pin(I2C1_SCL_PIN), freq=400000)

oled = SSD1306_I2C(128, 64, i2c0)
tof = VL53L0X.VL53L0X(i2c1)
tof.start()

def read_pot(adc):
    return int(adc.read_u16()) >> 8

oled_blue_area = 16
col_2_start = 90
while True:
    oled.fill(0)
    oled.text("CoderDojo Robot", 0, 0)
    oled.text("Frwd Power:", 0, oled_blue_area)
    oled.text(str(read_pot(adc_1)), col_2_start, oled_blue_area)
    oled.text("Turn Dist:", 0, oled_blue_area + 12)
    oled.text(str(read_pot(adc_2)), col_2_start, oled_blue_area + 12)
    oled.text("Turn Time:", 0, oled_blue_area + 24)
    oled.text(str(read_pot(adc_3)), col_2_start, oled_blue_area + 24)
    oled.text("Dist:", 0, oled_blue_area + 36)
    oled.text(str(tof.read()), col_2_start, oled_blue_area + 36)
    oled.show()
    sleep(.1)

