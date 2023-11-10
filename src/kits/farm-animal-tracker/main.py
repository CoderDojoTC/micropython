# farm animal manager

from mfrc522 import MFRC522
import utime
import machine
from time import sleep
from ssd1306 import SSD1306_I2C

reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
# setup the display driver using the i2c interface
oled = SSD1306_I2C(128, 64, i2c)

def my_function(myCard):
    if myCard == "980505127":
        return "Animal-1"
    elif myCard == "1535192762":
        return "Animal-2"
    elif myCard == "2760850942":
        return "Animal-3"
    else:
        return "Unknown!"
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            oled.fill(0)
            oled.show()
            oled.text(str(card), 0, 0)
            oled.text(my_function(str(card)), 0, 15)
            oled.show()
            
            print("ID: "+str(card))
            print(my_function(str(card)))

    else:
        print("Waiting for animal.")
        oled.fill(0)
        oled.show()
        oled.text("Waiting for", 0, 0)
        oled.text("animal.", 0, 15)
        oled.show()
            
utime.sleep_ms(500)
