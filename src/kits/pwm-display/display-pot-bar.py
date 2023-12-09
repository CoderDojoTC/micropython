# Display a PWM waveform on a 128x64 OLED Display

from machine import Pin, ADC, SPI
from utime import sleep
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)

WIDTH = 128
HEIGHT = 64
HALF_HEIGHT = HEIGHT // 2
clock=Pin(2)
data=Pin(3)
RES = Pin(4)
DC = Pin(5)
CS = Pin(6)

spi=SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

POT_PIN = ADC(26)
POT_MAX = 65536

# map a value from one rante into another range
# checks for divide by zero
def map(value, istart, istop, ostart, ostop):
  # check ff (istop - istart)
  if (istop - istart) == 0:
      return ostop
  else:
      return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

# draw a horizontal bar
def draw_hbar(inval, yPos, barHeight):
    oled.fill_rect(0, yPos, inval, barHeight, 1) # fill with 1s

def update_display(xPos):
    oled.fill(0)
    oled.text('Display Pot', 0, 0)
    # draw a hbar at the top yPos, height
    draw_hbar(xPos, 10, 2)
    oled.text("X Pos: " + str(xPos), 0, 56)
    oled.show()

counter = 0
# repeat forever
while True:
    potVal = int(POT_PIN.read_u16())
    xPos = map(potVal, 0, POT_MAX, 0, WIDTH)
    update_display(xPos)
    led.toggle()
    sleep(.1)
    counter += 1