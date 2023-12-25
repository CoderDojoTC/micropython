# Play Test MIDI 
from machine import Pin, UART
import time
uart = UART(1, baudrate=31250, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=None, stop=1)
led=Pin("LED", Pin.OUT)
note = 24

while True:
    midimessage = bytearray([0x90, note, 64])
    uart.write(midimessage)
    led.toggle()
    # change third parameter to be 0
    midimessage = bytearray([0x90, note, 0])
    # pause 1/8 of a second
    time.sleep(0.125)
    note += 2
    if note > 64:
        note=24


