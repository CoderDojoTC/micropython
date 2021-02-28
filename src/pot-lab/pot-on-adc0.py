import machine
import utime
pot = machine.ADC(26)
min = 65535
max = 0
pot_val = 0
while True:
    pot_val = pot.read_u16()
    if pot_val < min:
        min = pot_val
    if pot_val > max:
        max = pot_val
    percent = (pot_val - min)/max * 100
    print(pot_val, min, max, round(percent,1))
    utime.sleep(.2)