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
import mfrc522
from os import uname


def uidToString(uid):
	mystring = ""
	for i in uid:
		mystring = "%02X" % i + mystring
	return mystring
    
def do_read():

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(sck=18,mosi=23,miso=19,rst=22,cs=21)
	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to read from address 0x08")
	print("")

	try:
		while True:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:
        
				(stat, uid) = rdr.SelectTagSN()
        	
				if stat == rdr.OK:
					print("Card detected %s" % uidToString(uid))
				else:
					print("Authentication error")

	except KeyboardInterrupt:
		print("Bye")
```

## References

* [Dan J Perron Driver](https://github.com/danjperron/micropython-mfrc522/blob/master/mfrc522.py)
* [Microcontrollers Lab Tutorial](https://microcontrollerslab.com/raspberry-pi-pico-rfid-rc522-micropython/)