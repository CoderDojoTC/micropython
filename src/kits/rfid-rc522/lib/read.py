# pico_read.py
# https://github.com/danjperron/micropython-mfrc522/blob/master/Pico_example/Pico_read.py
# rdr = mfrc522.MFRC522(sck=SCK_PIN,mosi=MOSI_PIN,miso=MISO_PIN,rst=RST_PIN,cs=21)from mfrc522 import MFRC522
from mfrc522 import MFRC522
import config

# Implicit read from config file
SCK_PIN = config.SCK_PIN
MISO_PIN = config.MISO_PIN
MOSI_PIN = config.MOSI_PIN
RESET_PIN = config.RESET_PIN

import utime

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
    
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)   
# reader = MFRC522(spi_id=0, sck=SCK_PIN, miso=MISO_PIN, mosi=MOSI_PIN, cs=1, rst=RESET_PIN)

print("")
print("Please place card on reader")
print("")

PreviousCard = [0]

try:
    while True:

        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        #print('request stat:',stat,' tag_type:',tag_type)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if uid == PreviousCard:
                continue
            if stat == reader.OK:
                print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid),"little",False)).upper(),reader.tohexstring(uid)))
                defaultKey = [255,255,255,255,255,255]
                reader.MFRC522_DumpClassic1K(uid, Start=0, End=64, keyA=defaultKey)
                print("Done")
                PreviousCard = uid
            else:
                pass
        else:
            PreviousCard=[0]
        utime.sleep_ms(50)                

except KeyboardInterrupt:
    pass