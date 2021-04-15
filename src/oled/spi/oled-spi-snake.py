from machine import Pin, SPI, ADC
import ssd1306
import time
import random
 
def showPixelList(pixelList):
    for xy in pixelList:
        x, y = xy
        oled.pixel(x, y, 1)
        
def appleBit(appleList, snakeList):
    hit = 0
    snakeX1, snakeY1 = snakeList[0]
    snakeX2, snakeY2 = snakeList[1]
    
    # Did the snake bite the apple?
    for appleXY in appleList:
        appleX, appleY = appleXY
        if (snakeX1 == appleX and snakeY1 == appleY) or (snakeX1 == appleX and snakeY2 == appleY) or (snakeX2 == appleX and snakeY1 == appleY) or (snakeX2 == appleX and snakeY2 == appleY):
            hit = 1
            break
        
    # Yes, so clear the apple and make a new one
    if hit == 1:
        for appleXY in appleList:
            appleX, appleY = appleXY
            oled.pixel(appleX, appleY, 0)
        appleList.clear()
        appleX = random.randint(1, 125)
        appleY = random.randint(11, 61)
        for i in range(2):
            appleList.append((appleX + i, appleY))
            appleList.append((appleX + i, appleY + 1))
        showPixelList(appleList)
    return hit
 
def snakeBit(snakeList):
    hit = 0
    x, y = snakeList[0]
    length = len(snakeList)
    i = 10
 
    while i < length:
        snakeX, snakeY = snakeList[i]
        if x == snakeX and y == snakeY:
            hit = 1
            break
        i += 1
    return hit
    
# Define the pins for SPI Clock and Transmit
spi_sck = Pin(2)
spi_tx = Pin(3)
spi = SPI(0, baudrate=100000, sck=spi_sck, mosi=spi_tx)
 
# Define the pins for Chip Select, DC (Command), and Reset
CS = Pin(1)
DC = Pin(4)
RES = Pin(5)
 
# Setup the oled display
oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)
 
# Define the pins for the buttons
leftButton = Pin(10, Pin.IN, Pin.PULL_UP)
rightButton = Pin(11, Pin.IN, Pin.PULL_UP)
upButton = Pin(12, Pin.IN, Pin.PULL_UP)
downButton = Pin(13, Pin.IN, Pin.PULL_UP)
 
# Turn all pixels off
oled.fill(0)
 
# Provide info to user
oled.text('Eat the apples', 0, 0, 1)
oled.text('Hit any button', 0, 20, 1)
oled.text(' to start the', 0, 30, 1)
oled.text('    game', 0, 40, 1)
oled.show()
 
 
# Wait unti the user hits a button to clear the screen and start drawing
while leftButton.value() and rightButton.value() and upButton.value() and downButton.value():
    time.sleep(.25)
 
# Turn all pixels off
oled.fill(0)
 
# Create the initial appleList
x = random.randint(101, 121)
y = random.randint(41, 61)
appleList = []
for i in range(2):
    appleList.append((x + i, y))
    appleList.append((x + i, y + 1))
showPixelList(appleList)
    
# Create initial snakeList
x = random.randint(20, 100)
y = random.randint(20, 40)
snakeList = []
for i in range(10):
    snakeList.append((x + i,y))
    snakeList.append((x + i,y + 1))
showPixelList(snakeList)
    
# Add the wall around the "garden"
oled.rect(0, 10, 128, 54, 1)
 
# Show the number of apples eaten
appleHits = 0
oled.text('Apples: ' + str(appleHits), 0, 0, 1)
oled.show()
 
xDir = 0
yDir = 0
delay = .05
 
# Loop forever
while True:
    
    # Get the head of the snakeList (Top left)
    x, y = snakeList[0]
    
    # Figure out the new direction of the snakeList if a button has been pushed
    if leftButton.value() != 1 and xDir == 0:
        xDir = -1
        yDir = 0
    if rightButton.value() != 1 and xDir == 0:
        xDir = 1
        yDir = 0
    if upButton.value() != 1 and yDir == 0:
        xDir = 0
        yDir = -1
    if downButton.value() != 1 and yDir == 0:
        xDir = 0
        yDir = 1
    
    # Move
    x = x + xDir
    y = y + yDir
    
    if yDir == 0:
        snakeList.insert(0, (x , y + 1))
        oled.pixel(x, y + 1, 1)
    else:
        snakeList.insert(0, (x + 1, y))
        oled.pixel(x + 1, y, 1)
    snakeList.insert(0, (x , y))
    oled.pixel(x, y, 1)
    
    # Check for a bite on the apple
    if appleBit(appleList, snakeList) == 1:
        oled.text('Apples: ' + str(appleHits), 0, 0, 0)
        appleHits += 1
        oled.text('Apples: ' + str(appleHits), 0, 0, 1)
        delay = delay * 0.9
    else:
        snakeX, snakeY = snakeList.pop()
        oled.pixel(snakeX, snakeY, 0)
        snakeX, snakeY = snakeList.pop()
        oled.pixel(snakeX, snakeY, 0)
        
    oled.show()
 
    # Check for running into the wall
    if x <= 1 or x >= 126 or y <= 11 or y >= 62:
        break
    
    # Did the snake run into itself?
    if snakeBit(snakeList) == 1:
        break
    
    time.sleep(delay)
 
oled.text('Game Over', 30, 30, 0)
oled.text('Game Over', 30, 30, 1)
oled.show()