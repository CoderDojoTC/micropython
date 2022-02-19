# servo
# Brown: GND
# Orange/Red : VCC
# Yellow: Signal
#
# Time for high level (Radio Shack Micro-servo @ 5V)
# 0.5 ms :   0 degree
# 1.0 ms :  45 degree
# 1.5 ms :  90 degree
# 2.0 ms : 135 degree
# 2.5 ms : 180 degree

from machine import Pin, PWM
from time import sleep

SERVO_PIN = 15
servoPin = PWM(Pin(SERVO_PIN))
servoPin.freq(50)

def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=8000 # duty*100
    minDuty=2000 # duty*100
    #maxDuty=2000 # test
    #minDuty=8000 # test
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))
        
while True:

  for degree in range(0,180,1):
    servo(degree)
    sleep(0.01)
    print("increasing -- "+str(degree))
    
  for degree in range(180, 0, -1):
    servo(degree)
    sleep(0.01)
    print("decreasing -- "+str(degree))