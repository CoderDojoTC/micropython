# Four Digit LED Display

You can purchase 4-digit LED displays on eBay for about $2 each.

![](./../img/4-digit-led-display.png)

![](./img/../../../img/4-digit-7-segment-colon.png)

```py
from machine import Pin
from time import sleep
import tm1637

DIO_PIN = 0
CLK_PIN = 1

DELAY = 0.5

tm = tm1637.TM1637(clk=Pin(CLK_PIN), dio=Pin(DIO_PIN))

# all segments off
tm.write([1, 2, 3, 4])
```