from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from utime import sleep

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("CoderDojo Rocks!")
    sleep(1)
    lcd.clear()
    lcd.move_to(0, 1)
    lcd.putstr("CoderDojo Rocks!")
    sleep(1)