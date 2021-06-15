import machine
import time
photo_pin = machine.ADC(26)

while True:
    val = photo_pin.read_u16()
    print(val)
    time.sleep(.2)