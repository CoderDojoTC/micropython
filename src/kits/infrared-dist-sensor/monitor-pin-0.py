from machine import Pin, PWM
from utime import sleep

SENSOR_PIN = 0
sensor = machine.Pin(SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)

led = Pin(25, Pin.OUT)

# corner of the lower right
SPEAKER_PIN = 16
speaker = PWM(Pin(SPEAKER_PIN))

counter = 0

def play_sound1():
    # create a Pulse Width Modulation Object on this pin
    speaker.duty_u16(1000)
    speaker.freq(300) # 1 Kilohertz
    sleep(.1) # wait a 1/4 second
    speaker.duty_u16(0)


def play_sound2():
    speaker.duty_u16(1000)
    speaker.freq(800)
    sleep(.1)
    speaker.duty_u16(0)

    
# turn off the PWM 
speaker.duty_u16(0)

counter = 0
def main():
    global counter
    while True:
        # toggle the on-board LED every 20th time
        if not counter % 10:
            led.toggle()
        myVal = sensor.value()
        print(myVal)
        if myVal:
            play_sound1()
        else:
            # play_sound2()
            sleep(0)
        sleep(.05)
        # increment counter
        counter += 1

try:
    main()
except KeyboardInterrupt:
    speaker.duty_u16(0)
    print("Sound terminated")