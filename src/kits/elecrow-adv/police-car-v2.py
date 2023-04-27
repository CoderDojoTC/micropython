from utime import sleep
from machine import Pin,PWM

# Pins
RED_PIN = 13
BLUE_PIN = 14
BUZZER_PIN = 15

# pin objects
red_led = machine.Pin(RED_PIN, machine.Pin.OUT)
blue_led = machine.Pin(BLUE_PIN, machine.Pin.OUT)
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(1000)

def main():
    while True:
        buzzer.freq(750) # low frequence tone
        red_led.on()
        blue_led.off()
        sleep(.2)
        buzzer.freq(1200) # high frequence tone
        red_led.off()
        blue_led.on()
        sleep(.2)

try:
    main()
except KeyboardInterrupt:
    buzzer.duty_u16(0)
    print("sound off")