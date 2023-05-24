# I2C Scanner
import machine
from time import sleep
from ssd1306 import SSD1306_I2C
sda=machine.Pin(2)
scl=machine.Pin(3)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

WIDTH=128
HEIGHT=64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

delay = 3
while True:
    oled.fill(0)
    oled.text("Rect fill test", 0, 0)
    oled.text("white on black", 0, 10)
    oled.show()
    sleep(delay)
    
    oled.fill(1)
    oled.text("Rect fill test", 0, 0, 0)
    oled.text("black on white", 0, 10, 0)
    oled.show()
    sleep(delay)


    oled.fill(0)
    oled.text("rect(x,y,wid,ht)", 0, 0, 1)
    oled.rect(10,10, WIDTH-20, HEIGHT-20, 1)
    oled.show()
    sleep(delay)
    
    oled.fill(1)
    oled.text("rect(x,y,wid,ht)", 0, 0, 0)
    oled.rect(10,10, WIDTH-20, HEIGHT-20, 0)
    oled.show()
    sleep(delay)


    oled.fill(0)
    oled.text("fill_rect(x,y,w,h)", 0, 0, 1)
    oled.fill_rect(10,10, WIDTH-20, HEIGHT-20, 1)
    oled.show()
    sleep(delay)
    
    oled.fill(1)
    oled.text("fill_rect(x,y,w,h)", 0, 0, 0)
    oled.fill_rect(10,10, WIDTH-20, HEIGHT-20, 0)
    oled.show()
    sleep(delay)
    

    oled.fill(0)
    oled.text("hline(x,y,w)", 0, 0, 1)
    oled.hline(10,20, WIDTH-20, 1)
    oled.show()
    sleep(delay)
 
    oled.fill(1)
    oled.text("hline(x,y,w)", 0, 0, 0)
    oled.hline(10,20, WIDTH-20, 0)
    oled.show()
    sleep(delay)


    oled.fill(1)
    oled.text("vline(x,y,h)", 0, 0, 0)
    oled.vline(int(WIDTH/2),10, HEIGHT-20, 0)
    oled.show()
    sleep(delay)
    
    oled.fill(0)
    oled.text("vline(x,y,h)", 0, 0, 1)
    oled.vline(int(WIDTH/2),10, HEIGHT-20, 1)
    oled.show()
    sleep(delay)