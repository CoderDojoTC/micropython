from machine import Pin, PWM
from utime import sleep

SENSOR_PIN = 0
sensor = machine.Pin(SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)

led = Pin(25, Pin.OUT)
external_led = Pin(15, Pin.OUT)

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

external_led_state = 0
def toggle_light():
    global external_led_state
    external_led.toggle()
    if external_led_state == 0:
        external_led_state = 1
        external_led.on()
    else:
        external_led_state = 0
        external_led.off()
    
# turn off the PWM 
speaker.duty_u16(0)

counter = 0

prior_value = 0
def main():
    global counter, prior_value
    while True:
        # toggle the on-board LED every 20th time
        if not counter % 10:
            led.toggle()
        myVal = sensor.value()
        print(myVal)
        if myVal != prior_value:
            if myVal == 1:
                play_sound1()
                toggle_light()
            else:
                play_sound2()
            prior_value = myVal
        sleep(.05)
        # increment counter
        counter += 1

try:
    main()
except KeyboardInterrupt:
    speaker.duty_u16(0)
    print("Sound terminated")