import tm1637
from machine import Pin
from utime import sleep

DATA_PIN = 0
CLOCK_PIN = 1

tm = tm1637.TM1637(clk=Pin(CLOCK_PIN), dio=Pin(DATA_PIN))

RoA_Pin = 0
RoB_Pin = 1
Btn_Pin = 2
globalCounter = 0
flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

# CLK # DT # SW
# counter value
# Whether the rotation flag occurs
# DT state # CLK state
clk_RoA = Pin(RoA_Pin, Pin.IN)
dt_RoB = Pin(RoB_Pin, Pin.IN)
sw_BtN = Pin(Btn_Pin, Pin.IN, Pin.PULL_UP)

# Initialize the interrupt function, when the SW pin is 0, the interrupt is enabled
sw_BtN.irq(trigger=Pin.IRQ_FALLING, handler=btnISR)
    
# Rotation code direction bit judgment function
def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter

    Last_RoB_Status = dt_RoB.value()

    # Judging the level change of the CLK pin to distinguish the direction
    while(not clk_RoA.value()):
        Current_RoB_Status = dt_RoB.value()

        flag = 1
    if flag == 1:
        flag = 0
        # Rotation mark occurs
        # The flag bit is 1 and a rotation has occurred
        # Reset flag bit
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter = globalCounter + 1 # counterclockwise, positive
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter = globalCounter - 1 # Clockwise, negative

# Interrupt function, when the SW pin is 0, the interrupt is enabled
def btnISR(chn):
    global globalCounter
    globalCounter = 0
    print ('globalCounter = %d' %globalCounter)

tmp = 0

while True:
    rotaryDeal()
    if tmp != globalCounter:
        print('globalCounter = %d' % globalCounter)
        tmp = globalCounter
        tm.number(globalCounter)

    if globalCounter == 0:
        break


