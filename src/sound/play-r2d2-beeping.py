import os as uos
from machine import Pin
from utime import sleep
from wavePlayer import wavePlayer
# this works when we send mono to pin 16 (lower right corner) leftPin=Pin(0),rightPin=Pin(16)
# this will not work) leftPin=Pin(0),rightPin=Pin(18)
# this will not work) leftPin=Pin(0),rightPin=Pin(19)
# this will work: wavePlayer(leftPin=Pin(14),rightPin=Pin(15))
# this will work: wavePlayer(leftPin=Pin(15),rightPin=Pin(14))
player = wavePlayer(leftPin=Pin(15),rightPin=Pin(14))

try:
    while True:
        player.play('/sounds/r2d2-beeping-8k.wav')
        sleep(1)

except KeyboardInterrupt:
    player.stop()
    print("wave player terminated")