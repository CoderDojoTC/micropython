from machine import Pin, PWM, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

# pot init
POT_PIN_1 = 26
adc = machine.ADC(POT_PIN_1)

# Display init
SDA_PIN = 16
SCL_PIN = 17
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# motor stuff
HALF_POT = 32768
FORWARD_PIN = 9
REVERSE_PIN = 8
forward = PWM(Pin(FORWARD_PIN))
reverse = PWM(Pin(REVERSE_PIN))

counter = 0
scale = .25 # percent of total to give the motor for a demo that does not use too much battery power
def main():
    global counter, scale
    while True:
        pot_value = adc.read_u16()
        print(pot_value, pot_value >> 6)
        if pot_value > HALF_POT:
            # forward
            reverse.duty_u16(0)
            power = pot_value - HALF_POT
            scaled_power = int(power * scale)
            print('forward:', scaled_power)
            forward.duty_u16(scaled_power)
        else:
            forward.duty_u16(0)
            power = HALF_POT - pot_value
            scaled_power = int(power * scale)
            reverse.duty_u16(scaled_power)
            print('reverse:', scaled_power)
        
        # display code
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(str(pot_value >> 6))
        
        lcd.move_to(8, 0)
        lcd.putstr(str(power >> 6))
        
        lcd.move_to(0, 1)
        if pot_value > HALF_POT:
            lcd.putstr('forward')
        else:
            lcd.putstr('reverse')
        
        sleep(.1)
        counter += 1

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    forward.duty_u16(0)
    reverse.duty_u16(0)