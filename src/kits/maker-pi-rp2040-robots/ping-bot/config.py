# VCC, GND Clock and Data are on Grove Port 2
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)

# servo signal pins
CS = machine.Pin(13) # can also be wired to +
DC = machine.Pin(14)
RES = machine.Pin(15)
oled = SSD1306_SPI(128, 64, spi, DC, RES, CS)

# pins used on the Grove 4 connector
Trig = Pin(17, Pin.OUT)
Echo = Pin(16, Pin.IN, Pin.PULL_DOWN)

NEOPIXEL_PIN = 18
SPEAKER_PIN = 22

MOTOR_RIGHT_FORWARD = 11
MOTOR_RIGHT_BACKWARD = 10
MOTOR_LEFT_FORWARD = 8
MOTOR_LEFT_REVERSE = 9