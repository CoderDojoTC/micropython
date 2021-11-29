from machine import Pin, PWM
pwm = PWM(Pin(14))
pwm.deinit()
pwm = PWM(Pin(15))
pwm.deinit()
