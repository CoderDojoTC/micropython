# Ping Display Bot

This robot uses the Cytron Maker Pi RP2040 and has a 128x64 OLED on an SPI port.

The first four wires of the OLED are on Grove 2 and the Ping Sensor is on Grove 4.
The last three pins of the OLED are on the servo signal ports 13, 14 and 15 (CS, DC and RES)


The configuration is as follows:

```py
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0, sck=spi_sck, mosi=spi_tx)

CS = machine.Pin(13)
DC = machine.Pin(14)
RES = machine.Pin(15)
oled = SSD1306_SPI(128, 64, spi, DC, RES, CS)

# pins used on the Grove 4 connector
Trig = Pin(17, Pin.OUT)
Echo = Pin(16, Pin.IN, Pin.PULL_DOWN)
```

## Standard Cytron Maker Pi RP2040 Ports

