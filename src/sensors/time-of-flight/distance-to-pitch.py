from utime import sleep
from machine import Pin, PWM
from machine import I2C
import VL53L0X

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
tof = VL53L0X.VL53L0X(i2c)
# the minimum value for zero distance is about 50
tof.start()

def main():
    while True:
        # Start ranging
        distance = tof.read()
        if distance > MAX_DIST:
            print('No Signal')
            speaker.duty_u16(0)
        else:
            # change these numbers to get different sounds
            freq = distance * 9 - 250
            print(distance, freq)
            sleep(.1)
            speaker.duty_u16(1000)
            speaker.freq(freq)

try:
    main()
except KeyboardInterrupt:
    print("Keyboard Interrupt.  Shutting Down Speaker PWM")
finally:
    # Optional cleanup code
    print('turning off sound')
    speaker.duty_u16(0)
    tof.stop()