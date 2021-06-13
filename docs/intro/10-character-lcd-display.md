# Character LCD Display

## Address Scanner

### Scanner Code
```py
import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
print(i2c.scan())
```
### Scanner Result

```sh
>>> %Run -c $EDITOR_CONTENT
[39]
>>>
```

## Hello To The LCD 

```py
import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000) i2c.writeto(114, '\x7C')
i2c.writeto(114, '\x2D') i2c.writeto(114, "hello world")
```

## 1602 LCD

[MicroPython Forum on 1602 LCDs](https://forum.micropython.org/viewtopic.php?t=2858)

```py
import i2clcd

lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
lcd.init()

# fill a line by the text
lcd.print_line('hello', line=0)
lcd.print_line('world!', line=1, align='RIGHT')

# print text at the current cursor position
lcd.move_cursor(1, 0)
lcd.print('the')

# custom character
char_celsius = (0x10, 0x06, 0x09, 0x08, 0x08, 0x09, 0x06, 0x00)
lcd.write_CGRAM(char_celsius, 0)
lcd.move_cursor(0, 6)
lcd.print(b'CGRAM: ' + i2clcd.CGRAM_CHR[0])
```

## ssd1306 module


[SSD1306 Library](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py) - click the RAW button and then right click to do a "Save As"

### HD44780 Drivers
[Dave Hylands HD44780 Drivers in Python](https://github.com/dhylands/python_lcd)

## References

[MFitzp article on OLED displays](https://www.mfitzp.com/article/oled-displays-i2c-micropython/)

[Adafruit SSD1306 Driver](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/blob/master/examples/ssd1306_stats.py)

[Adafruit LCD Guide](https://learn.adafruit.com/character-lcds)