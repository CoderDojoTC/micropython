# Sample MicroPython program to test a ultrasonic ping sensor using the Maker Pi RP2040
# This is a polling (non interrupt) version of testing a Ultrasonic Ping sensor
# It is deliberately designed for beginning students to be able to understand
# See https://gist.githubusercontent.com/suadanwar/81ca2b83383310fa170a76bdf56771fb/raw/3ff9ae1cc226734c4d6db8756534fbe5df829c4a/UltrasonicPico.py

from machine import Pin, PWM
import utime

# We will pull the trigger down low for 2 microsends and then high for 10 microseconds  
# then low to start measurement
Trig = Pin(17, Pin.OUT)
# we will look for a 
Echo = Pin(16, Pin.IN, Pin.PULL_DOWN)
 
Buzzer = PWM(Pin(22))

# returns the distance to a obstacle in cm
def CheckDistance():
    SpeedOfSoundInCM = 0.034

    # begin the LOW/HIGH/LOW trigger output sequence
    Trig.low()
    utime.sleep_us(2)
    Trig.high()
    utime.sleep_us(10)
    Trig.low()
    exitLoop = False
    loopcount = 0 #used as a failsafe if the signal doesn't return
    # now we wait for the Echo pin to go high
    while Echo.value() == 0 and exitLoop == False:
        loopcount = loopcount + 1
        delay_time = utime.ticks_us()
        # give up after 3,000 tries
        if loopcount > 3000 : exitLoop == True
    
    # we now a high if we did not timeout
    while Echo.value() == 1 and exitLoop == False:
        loopcount = loopcount + 1
        receive_time = utime.ticks_us()
        # give up after 3,000 tries
        if loopcount > 3000 : exitLoop == True
 
    if exitLoop == True: #We failed somewhere
        return 0
    else:
        dela_time = receive_time - delay_time
        distance = dela_time * SpeedOfSoundInCM
        distance = int(distance / 2)
        return distance
 
while True:
    # why do they call CheckDistance() 3 times and not reference the distance variable?
    distance = CheckDistance()
    print(distance)
    # biz if we find something closer than 10 cm away
    if distance < 10:
        Buzzer.duty_u16(3000)
        Buzzer.freq(1700)
        utime.sleep(0.05)
        Buzzer.duty_u16(0)
        # sleep longer the further away the object is
        utime.sleep(distance/1000)