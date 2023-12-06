from machine import Pin,PWM
import utime

SERVO_PIN=0

SERVO_MIN =  500000
SERVO_MAX = 1500000

POT_PIN = 26

POT_MIN = 272
POT_MAX = 65263

servo_per_pot = (SERVO_MAX-SERVO_MIN)/(POT_MAX-POT_MIN)

analog_value = machine.ADC(POT_PIN)

led = Pin(25,Pin.OUT)

servo = PWM(Pin(SERVO_PIN))
servo.freq(50)

while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    servo.duty_ns(SERVO_MIN+int(reading*servo_per_pot ) )
    utime.sleep(0.2)


# graveyard
servo.duty_ns(SERVO_MID)

while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    servo.duty_ns(SERVO_MIN)
    led.value(0)
    utime.sleep(1)
    servo.duty_ns(SERVO_MID)
    led.value(1)
    utime.sleep(0.2)
    servo.duty_ns(SERVO_MAX)
    utime.sleep(1)
