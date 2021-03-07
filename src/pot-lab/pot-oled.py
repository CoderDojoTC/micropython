import machine
import utime
import sh1106

sda=machine.Pin(0)
scl=machine.Pin(1)
pot_pin = machine.ADC(26)

i2c=machine.I2C(0,sda=sda, scl=scl)
# Screen size
width=128
height=64
half_height = int(height / 2)
# oled = SSD1306_I2C(width, height, i2c)
oled = sh1106.SH1106_I2C(width, height, i2c, machine.Pin(4), 0x3c)

oled.fill(0) # clear to black

# note that OLEDs have problems with screen burn it - don't leave this on too long!
def border(width, height):
    oled.hline(0, 0, width - 1, 1) # top edge
    oled.hline(0, height - 2, width - 1, 1) # bottom edge
    oled.vline(0, 0, height - 1, 1) # left edge
    oled.vline(width - 1, 0, height - 1, 1) # right edge

# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def valmap(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

# draw a horizontal bar
def draw_hbar(inval, height, state):
    oled.fill(0) # clear screen
    border(width, height) # draw a border
    oled.fill_rect(0, 1, inval, height, 1) # fill with 1
    utime.sleep(.1) # wait a bit
    
# continiuous update
while True:
    pot_val = int(pot_pin.read_u16())
    # the max value of the input is a 2^16 or 65536
    pot_scaled = valmap(pot_val, 0, 65536, 0, 127)
    print(pot_val, pot_scaled)
    draw_hbar(pot_scaled, half_height, 1)
    
    oled.text('raw:', 0, half_height + 5, 1)
    oled.text(str(pot_val), 30, half_height + 5, 1)
    
    oled.text('scaled:', 0, half_height + 15, 1)
    oled.text(str(pot_scaled), 60, half_height + 15, 1)
    oled.show()  