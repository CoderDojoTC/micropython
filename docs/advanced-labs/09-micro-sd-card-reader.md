# Micro SD Card Reader

[Secure Digital](https://en.wikipedia.org/wiki/SD_card) (SD) is a non-volatile memory card format for use in portable devices such as cameras, MP3 players and portable devices.

On Microcontrollers SD cards are usually access through an [SPI interface](https://en.wikipedia.org/wiki/SD_card#Transfer_modes) although there are also devices that use I2C interfaces.

## Maker Pi Pico Connections

| GPIO Pin | SD Mode | SPI Mode |
| -------- | ------- | -------- |
| GP10     | CLK     | SCK      |
| GP11     | CMD     | SDI      |
| GP12     | DAT0    | SD0      |
| GP13     | DAT1    | X        |
| GP14     | DAT2    | X        |
| GP15     | CD/DAT3 | CSn      |

## Maker Pi Pico Example Code

### Pin Definitions


```py


# SD Mode Definitions
SDCARD_CLK = 10
SDCARD_CMD = 11
SDCARD_DAT0 = 12
SDCARD_DAT1 = 13
SDCARD_DAT2 = 14
SDCARD_CD_DAT3 = 15

# SPI Mode Definitions
SDCARD_SCK = 10
SDCARD_SDI = 11
SDCARD_SD0 = 12
SDCARD_X1 = 13
SDCARD_X2 = 14
SDCARD_CSn = 15
```

### Sample Code for SPI Mode


```py
import machine, os, sdcard

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(15, machine.Pin.OUT)
# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))
# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# OR this simpler initialization code should works on Maker Pi Pico too...
#sd = sdcard.SDCard(machine.SPI(1), machine.Pin(15))

os.mount(sd, '/sd')
# check the content
os.listdir('/sd')

# try some standard file operations
file = open('/sd/test.txt', 'w')
file.write('Testing SD card on Maker Pi Pico')
file.close()
file = open('/sd/test.txt', 'r')
data = file.read()
print(data)
file.close()
```

Results:

```
Testing SD card on Maker Pi Pico
```
## References

1. [MicroPython sdcard.py driver](https://docs.google.com/document/d/1JoHsZk5IipQPCLXWbZYpDKjGlnkyACOJ1[taUrKVsRg8/edit](https://github.com/micropython/micropython/blob/master/drivers/sdcard/sdcard.py)) - note there is no documentation on use with the RP2040 although there is example code for the pyboard and the ESP8266
1. [MicroPython.org Documentation](https://docs.micropython.org/en/latest/library/machine.SDCard.html)
2. [Raspberry Pi Pico Forum](https://forums.raspberrypi.com/viewtopic.php?t=307275)
3. [YouTube Video by Shawn Hymel](https://www.youtube.com/watch?v=u-vmsIr-s7w)
4. [Cytron Maker Pi Pico Datasheet](https://docs.google.com/document/d/1JoHsZk5IipQPCLXWbZYpDKjGlnkyACOJ1taUrKVsRg8/edit)