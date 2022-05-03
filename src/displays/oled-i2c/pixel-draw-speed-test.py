import machine
from utime import sleep, ticks_us
from ssd1306 import SSD1306_I2C
OLED_RESET = machine.Pin(15, machine.Pin.OUT)
OLED_RESET.low()
sleep(.1)
OLED_RESET.high()
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))

oled = SSD1306_I2C(128, 64, i2c)
oled.text('CoderDojo Rocks!', 0, 0)
oled.show()
print (i2c.scan())

# test the draw speed
# on the 133 Mhz RP2040 i get 27.7 milliseconds to draw a 128X64 display using I2C
# this is 128X64 = 8192 bits in 27.7 msec or 295.74 bits/msec = 300 kbits/sec
while True:
    # record the time we start drawing
    start_time = ticks_us()
    # draw a horizontal line 1 pixel at a time
    for i in range(0,127):
        oled.pixel(i, 11, 1)
        oled.show()
    for i in range(0,127):
        oled.pixel(i, 11, 0)
        oled.show()
    end_time = ticks_us()
    elapsed_time = end_time - start_time
    print('Total time in microseconds', elapsed_time)
    time_per_show = elapsed_time / 256
    print('Time per show:', time_per_show)
    
