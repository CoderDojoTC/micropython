import machine
import time

# lower right corner
motor_pin = machine.Pin(16, machine.Pin.OUT)
# allocate a PWM object for controlling the motor speed
#motor_pwm = machine.PWM(motor_pin)
#motor_pwm.freq(50) # 50 hertz
#motor_pwm.duty(51)

while True:
    print('on')
    motor_pin.high()
    time.sleep(3)
    
    print('off')
    motor_pin.low()
    time.sleep(3)