# Displaying Images on your OLED

We will use the ```framebuffer``` function to load a binary image into the OLED.

```python
buffer = bytearray(b"\x00\x00\x00\x00...

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

oled.fill(0)
oled.blit(fb, 50, 20) # copy the framebuffer to x=50 and y=20
oled.show()
```

## Drawing the Raspberry Pi Logo:

```py
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

WIDTH  = 128
HEIGHT = 64

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
print("I2C Address: "+hex(i2c.scan()[0]).upper()) # Display device address
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

oled.fill(0)
# Blit the image from the framebuffer to the oled display
oled.blit(fb, 50, 20)
oled.show()
```

But how do we convert a logo into a bytearray?
```

## References

1. [Cytron Example](https://github.com/CytronTechnologies/MAKER-PI-RP2040/blob/main/Examples/MicroPython/OLED/oled_ssd1306.py)
2. [Image to C ByteArray](http://javl.github.io/image2cpp/)
2. [Image to OLED Converter](http://www.majer.ch/lcd/adf_bitmap.php)

