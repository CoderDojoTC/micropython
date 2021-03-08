# Pong
Using a low-cost OLED device you can write a pong game.  If you use a small 128X64 OLED the price can be around $12.

## Part list

|Part Name|Price|Link|Description|
|---------|-----|----|-----------|
|Raspberry Pi Pico|$4|[Microcenter](https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=raspberry+pi+pico&searchButton=search)|With 264K RAM it has plenty of room for storing the framebuffer|
|1/2 Size Solderless Breadboard|$2|link|400 tie breadboard|Used to mount the pico|
|128X64 OLED|$5|[eBay](https://www.ebay.com/itm/0-96-OLED-LCD-Display-Module-IIC-I2C-Interface-128x64-For-SSD1306-Prof/373470677081)|You can also get larger 2.42" displays for around $20|
|2 10K Potentiometers|$1.5 each|[eBay](https://www.ebay.com/itm/10K-OHM-Linear-Taper-Rotary-Potentiometer-10KB-B10K-Pot-With-Wire-Portable-H/303636919492)|You can purchase these in QTY 10 for less.  Use the part number B10K to narrow your search.|
|Clear Plastic Box|$4|[The Container Store](https://www.containerstore.com/s/clear-stackable-rectangle-containers-with-white-lids)|Shallow Narrow Stackable Rectangle Clear with Lids 8-1/4" x 3-1/2" x 1-7/8" h.  The link is to the white lids.|

![](img/raspberry-pi-pico.png)

Raspberry Pi Pico for $4.

![](img/oled-i2c.png)

OLED with I2C Interface.  Note the pins are VCC, GND, SCL (clock), SDA (data).

![](img/breadboard.png)

1/2 size 400 connector solderless breadboard

![](img/10k-pot.png)

10K potentiometer with pre-soldered connectors.  You will need two of these. You can use a male-to-male header to connect it to the breadboard.

## Connections

1. Connect the GND of the OLED to GND of the Pico
2. Connect the VCC of the OLED to 3V3 OUT (physical pin 36)
3. Connect the SDA (data) of the OLED to the Pico GP0 (physical pin 1 on the top left with USB up)
4. Connect the SCL (clock) of the OLED to GP1 (physical pin 2)
5. Connect the center tap of both potentiometers to ADC0 (GP26 - pin 31) and ADC1 (GP27 - pin 32)
6. Connect the outer connectors of the potentiometers to VCC and GND

## Getting the Right Python Libraries

To run this program, you will need a MicroPython display driver.  Our display in this example is the popular SSD1306 driver chip.  Your OLED might have a slightly different driver type.

Here is the line that must be customized for your display:

```
from ssd1306 import SSD1306_I2C
```

## Testing the OLED

This test will verify that your OLED connections are correct.

```py
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
WIDTH  = 128
HEIGHT = 64
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.text("CoderDojo Rocks",0,0)
oled.show()
```

## Drawing the Border

```
def border(width, height):
    oled.hline(0, 0, width - 1, 1) # top edge
    oled.hline(0, height - 2, width - 1, 1) # bottom edge
    oled.vline(0, 0, height - 1, 1) # left edge
    oled.vline(width - 1, 0, height - 1, 1) # right edge
```

[YouTube Video](https://www.youtube.com/watch?v=W6Yr9gv2dTQ)