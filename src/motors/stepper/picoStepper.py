#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Date: Dec 27th, 2021
# Version: 1.0
# https://peppe8o.com

from machine import Pin
from time import sleep

# define variables
motor_GP = [0,1,2,3] # RPI Pico ports, ordered according to IN1, IN2, IN3 and IN4 of ULN2003
seq_pointer=[0,1,2,3,4,5,6,7] # Pointer to keep current sequence position
stepper_obj = [] # array including the 4 Pins connected yo 

# sequence map
arrSeq = [[0,0,0,1],\
          [0,0,1,1],\
          [0,0,1,0],\
          [0,1,1,0],\
          [0,1,0,0],\
          [1,1,0,0],\
          [1,0,0,0],\
          [1,0,0,1]]


# Set all pins as output
print("Setup pins...")
for gp in motor_GP: stepper_obj.append(Pin(gp, Pin.OUT))

def stepper_move(direction): # direction must be +1 or -1
    global seq_pointer
    seq_pointer=seq_pointer[direction:]+seq_pointer[:direction]
    for a in range(4): stepper_obj[a].value(arrSeq[seq_pointer[0]][a])
    sleep(0.001)

while True:
    stepper_move(1)

  