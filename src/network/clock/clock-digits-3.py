# clock digits
import machine
import utime
import ssd1306
from utime import sleep, localtime
led = machine.Pin(25, machine.Pin.OUT)

SCL=machine.Pin(2) # SPI CLock
SDA=machine.Pin(3) # SPI Data
spi=machine.SPI(0, sck=SCL, mosi=SDA, baudrate=100000)

RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

segmentMapping = [
  #a, b, c, d, e, f, g
  [1, 1, 1, 1, 1, 1, 0], # 0
  [0, 1, 1, 0, 0, 0, 0], # 1
  [1, 1, 0, 1, 1, 0, 1], # 2
  [1, 1, 1, 1, 0, 0, 1], # 3
  [0, 1, 1, 0, 0, 1, 1], # 4
  [1, 0, 1, 1, 0, 1, 1], # 5
  [1, 0, 1, 1, 1, 1, 1], # 6
  [1, 1, 1, 0, 0, 0, 0], # 7
  [1, 1, 1, 1, 1, 1, 1], # 8
  [1, 1, 1, 1, 0, 1, 1]  # 9
];


# x and y are the center of the digit, size is the center to edge
def drawDigit(digit, x, y, size):

  segmentOn = segmentMapping[digit];
  
  # Horizontal segments
  for i in [0, 3, 6]:
    if (segmentOn[i]):
      if (i==0): yOffset = 0 # top
      if (i==3): yOffset = size*2 # bottom element
      if (i==6): yOffset = size # middle
      oled.line(x - size, y+yOffset-size, x + size, y+yOffset-size, 1);

  # Vertical segments
  for i in [1, 2, 4, 5]:
    if (segmentOn[i]) :
      if (i==1 or i==5):
          startY = y-size
          endY = y
      if (i==2 or i==4):
          startY = y
          endY = y + size
      if (i==4 or i==5): xOffset = -size
      if (i==1 or i==2): xOffset = +size
      xpos = x + xOffset
      oled.line(xpos, startY, xpos, endY, 1);

def update_screen(digit_val):
    oled.fill(0)
    oled.text('Clock Digit Lab', 0, 0, 1)
    dr = 10 # digit radius
    dch = 26 # digit center hight
    lm = 10 # left margin for all 4-digits
    dw = 24 # digit width (2*dr + spacing between digits
    cm = 8 # colon left margin
    
    # draw the hour digits
    hour = localtime()[3]
    if hour > 12:
        hour = hour - 12
        am_pm = 'pm'
    else:
        am_pm = 'am'
    if hour < 10:
        # just draw the second digit
        drawDigit(hour, lm+dw, dch, dr)
    else:
        # we have 10, 11 or 12 so the first digit is 1
        drawDigit(1, lm, dch, dr)
        # subtract 10 from the second digit
        drawDigit(hour-10, lm+dw, dch, dr)
       
    # draw the colon
    if localtime()[5] % 2:
        draw_colon(lm+dw*2+cm-16,dch-5)
    
    # draw the minutes
    minutes = localtime()[4]
    # value, x, y, size
    # left minute digit after the colon
    drawDigit(minutes // 10, lm+dw*2+cm, dch, dr)
    # right minute digit
    drawDigit(minutes % 10, lm+dw*3+cm+2, dch, dr)
    
    # draw the AM/PM
    oled.text(am_pm, lm+dw*4+cm-8, dch+3, 1)
    
    #oled.text(timeStrFmt(), 0, 46, 1)
    oled.text(str(localtime()[5]), 0, 54)
    #oled.text(str(digit_val), 0, 54, 1)

    oled.show()

def draw_colon(x,y):
    oled.fill_rect(x, y, 2, 2,1)
    oled.fill_rect(x, y+8, 2, 2,1)

def timeStrFmt():
    hour = localtime()[3]
    if hour > 12:
        hour = hour - 12
        am_pm = ' pm'
    else: am_pm = ' am'
    # format minutes and seconds with leading zeros
    minutes = "{:02d}".format(localtime()[4])
    return str(hour) + ':' + minutes + am_pm

counter = 0
while True:
    update_screen(counter)
    sleep(1)
    counter += 1
    if counter > 9:
        counter = 0

