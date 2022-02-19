# distance-to-pitch-display.py
# As you move your hand closer and further away from a Time-of-Flight distance sensor
# you change the pitch of the sound on the speaker
from utime import sleep
from machine import Pin, PWM
from machine import I2C
import VL53L0X
import ssd1306

WIDTH = 128
HEIGHT = 64
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0,sck=clock, mosi=data)
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

SDA_PIN = 16
SCL_PIN = 17
SPEAKER_PIN = 18
MAX_DIST = 500 # max raw reading that is valid

sda=machine.Pin(SDA_PIN) # row one on our standard Pico breadboard
scl=machine.Pin(SCL_PIN) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
speaker = PWM(Pin(SPEAKER_PIN))
# speaker.duty_u16(1000) # 50% on and off

# Create a VL53L0X object and start reading
TOF_ZERO_VALUE = 20
tof = VL53L0X.VL53L0X(i2c)
# the minimum value for zero distance is about 50
tof.start()

def main():
    while True:
        # Start ranging
        distance = tof.read() - TOF_ZERO_VALUE
        if distance > MAX_DIST:
            print('No Signal')
            speaker.duty_u16(0)
            oled.fill(0)
            oled.text(str(distance), 0, 0, 1)
            oled.text("No Signal", 0, 10, 1)
            oled.show()

        else:
            # change these numbers to get different sounds
            freq = distance * 11
            if freq < 0:
                freq = 0
            print(distance, freq)
            sleep(.1)
            speaker.duty_u16(1000)
            speaker.freq(freq)
            oled.fill(0)
            oled.text(str(distance), 0, 0, 1)
            oled.text(str(freq), 0, 10, 1)
            oled.show()

try:
    main()
except KeyboardInterrupt:
    print("Keyboard Interrupt.  Shutting Down Speaker PWM")
finally:
    # Optional cleanup code
    print('turning off sound')
    speaker.duty_u16(0)
    tof.stop()