import time
from machine import Pin

rotaryA = Pin(16, Pin.IN, Pin.PULL_DOWN)
rotaryB = Pin(17, Pin.IN, Pin.PULL_DOWN)

val = 0
# we set the old value to zero for both bits being off
old_combined = 0
while True:
    A_val = rotaryA.value()
    B_val = rotaryB.value()
    # a sifts by one bit and then is ORed with the B calue
    new_combined = (A_val << 1) | B_val
    if new_combined != old_combined:
            #print(A_val, end='')
            #print(B_val)
            old_combined = new_combined
            print(val)
    if A_val == 0 and B_val == 1:
        val += 1
    elif A_val == 1 and B_val == 0:
        val -= 1
    
    time.sleep(.05)