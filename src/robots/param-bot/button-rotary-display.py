# This program will print a sequence of numbers in the shell if a button is pressed
# Each momentary button must be connected to the 3.3 volt power rail
# The rotory encoder will only display A or B values
from machine import Pin, Timer
import ssd1306
import time

# display setup
WIDTH = 128
HEIGHT = 64
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0, sck=clock, mosi=data)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

led = Pin(15, Pin.OUT)

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(22, Pin.IN, Pin.PULL_DOWN)
rotaryA = Pin(16, Pin.IN, Pin.PULL_DOWN)
rotaryB = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:

    if button1.value():
        print('Button 1 ', end='')
        oled.fill(0)
        oled.text('Button 1', 0, 0, 1)
        oled.show()
    if button2.value():
        print('2 ', end='')
        oled.fill(0)
        oled.text('Button 2', 0, 10, 1)
        oled.show()
    if button3.value():
        print('3 ', end='')
        oled.fill(0)
        oled.text('Button 3', 0, 20, 1)
        oled.show()
    if rotaryA.value():
        print('A ', end='')
        oled.fill(0)
        oled.text('Rot A', 0, 30, 1)
        oled.show()
    if rotaryB.value():
        print('B ', end='')
        oled.fill(0)
        oled.text('Rot B', 0, 40, 1)
        oled.show()
    time.sleep(0.1)