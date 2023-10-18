# data_read.py
from mfrc522 import MFRC522
import utime
import machine
from time import sleep
# from ssd1306 import SSD1306_I2C

reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

# i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
# setup the display driver using the i2c interface
# oled = SSD1306_I2C(128, 64, i2c)

print("Bring TAG closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    print(stat)
    if stat == reader.OK:
        
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
#             oled.fill(0)
#             oled.show()
#             oled.text(str(card), 0, 0)
#             oled.text("Line2", 0, 15)
#             oled.show()
    utime.sleep(1)