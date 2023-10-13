# RFIG Reader RC-522

The RC-522 is a popular RFID reader that has strong support in the MicroPython
community.

## Pinout

![](./rc522-pinout.png)

|NAME|PICO GPIO|COLOR|
|----|---------|-----|
|SDA|1|Yellow|
|SCK|2|Orange|
|MOSI|4|Purple|
|MISO|3|Blue|
|IRQ|7|Brown|
|GND|GND|Black|
|RST|0|Green|
|3.3V|3.3v Out|Red|

### Wires at the RC522
![](./rc522-wires.pngrc522-wires)

### Wires at the Pico

## Config File

Place this in the config.py

```py
# reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)
SPI_ID = 0
RESET_PIN = 0 # Green OUT
SDA_PIN = 1 # Yellow OUT but used a Chip Select CS 
SCK_PIN = 2 # Orange OUT clock going from Pico to RC522
MISO_PIN = 3 # Blue 
MOSI_PIN = 4 # Purple
IRQ_PIN = 7 # Brown, OUT but not used in the reader demo

# GND is Black
# Red goes to 3.3v out

```

## Reader

```py
from mfrc522 import MFRC522
import utime


def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
    
              
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

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
```

## References

* [Dan J Perron Driver](https://github.com/danjperron/micropython-mfrc522/blob/master/mfrc522.py)
* [Microcontrollers Lab Tutorial](https://microcontrollerslab.com/raspberry-pi-pico-rfid-rc522-micropython/)