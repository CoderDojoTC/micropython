from machine import Pin,PWM ADC
light_sensor_pin = 0
PIR_pin = 1
Led_R_pin = 2
Led_G_Pin = 3
Led_B_pin = 4
# ADC0 multiplexing pin is GP26

light_sensor_ADC = ADC(light_sensor_pin) PIR = Pin(PIR_pin, Pin.IN, Pin.PULL_DOWN) Led_R = PWM(Pin(Led_R_pin))
Led_G = PWM(Pin(Led_G_Pin))
Led_B = PWM(Pin(Led_B_pin)) Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)

while True:
    print('light_sensor Value: ', light_sensor_ADC.read_u16())
    print('PIR Value: ',PIR.value())
    if PIR.value() == 1 and light_sensor_ADC.read_u16() > 35000:
        Led_R.duty_u16(65535)
        Led_G.duty_u16(65535)
        Led_B.duty_u16(65535)
    else:
        Led_R.duty_u16(0)
        Led_G.duty_u16(0)
        Led_B.duty_u16(0)


loop()