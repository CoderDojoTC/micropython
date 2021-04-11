# OLED Patterns

In this lesson, we will show how you can display interesting repeating patterns on your OLED screen.  Our program will write a pattern into the framebuffer using a simple math equation.  The oled.show() will then update the pattern on the display.

## Math Functions

The modulo function is written ```%```.  It returns the integer remainder after a division.  So ```7 % 3``` is 1 and ```7 % 4``` is 3.
The Power function of X to the Y power is written in python as ```pow(x,y)```.  For example pow(7, 2) is seven squared = 49.

The bitwise and is written as ```x & y```

```py
for i in range(8):
    13 & i
```

|Function|Returns|
|---|---|
|13 & 0 | 0 |
|13 & 1 | 1 |
|13 & 2 | 0 |
|13 & 3 | 1 |
|13 & 4 | 4 |
|13 & 5 | 5 |
|13 & 6 | 4 |
|13 & 7 | 5 |
|13 & 8 | 8 |
|13 & 9 | 9 |
|13 & 10 | 8 |
|13 & 11 | 9 |
|13 & 12 | 12 |


## The Equations

(x ^ y) % 9
(x ^ y) % 5
(x ^ y) % 17
(x ^ y) % 33
(x * y) & 64
(x * y) & 24
(x * y) & 47
(x ^ y) < 77
(x ^ y) < 214
(x ^ y) < 120
(x * 2) % y
(x * 64) % y
(x * 31) % y
((x-128) * 64) % (y-128)
(x ^ y) & 32
(x ^ y) & 72
(x ^ y) & 23
((x * y) ** 4) % 7
((x * y) ** 5) % 99
((x * y) ** 9) % 3
(x % y) % 4
(y % x) % 20
40 % (x % y)
x & y
x % y
x & 9

## Combinations
(x & y)   &   (x ^ y) % 19
((x ^ y) & 32)   *   (x ^ y) % 9)
(x * 64) % y   *   ((x ^ y) < 77)


## Sample Image

## Sample Code

draw-patterns-ssd1306-spi.py
```py
import machine
import ssd1306

WIDTH = 128
HEIGHT = 64
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi=machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

oled.fill(0) # clear display
for x in range(WIDTH):
    for y in range(HEIGHT):
        if x % (y+1):
           oled.pixel(x,y,0)
        else:
            oled.pixel(x,y,1)
oled.show()

```

## Adding a List of Patterns

### The Eval Function
The eval() function takes any string and passes it to the python interpreter for evaluation within the current context of variables that are in scope.  We can use eval to pass an expression that should be evaluated to any function.

```py
list = ["x+y", "x-y", "x*y", "x % (y+1)"]

for i in range(0, 4):
    print(list[i], ': ', sep='', end='')
    for x in range(5):
      for y in range(5):
         print(eval(list[i]), '', end='')
    print('')
```

## The Command Design Pattern

## Reference

[Martin Kleppe Post on Twitter](https://twitter.com/aemkei/status/1378106731386040322)
