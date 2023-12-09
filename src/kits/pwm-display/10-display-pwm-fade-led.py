# Display a PWM waveform on a 128x64 OLED Display

from machine import ADC, Pin, PWM
from utime import sleep
import ssd1306

# this is the built-in LED on the Pico
led = Pin('LED', Pin.OUT)
EXTERNAL_LED_PIN = 18
pwm = PWM(Pin(EXTERNAL_LED_PIN))
# 50% duty cycle
pwm.freq(50)

WIDTH = 128
HEIGHT = 64
HALF_HEIGHT = HEIGHT // 2
clock=Pin(2)
data=Pin(3)
RES = machine.Pin(4)
DC = machine.Pin(5)
CS = machine.Pin(6)

spi=machine.SPI(0, sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

POT_PIN = machine.ADC(26)
POT_MAX = 65536

# map a value from one rante into another range
# checks for divide by zero
def map(value, istart, istop, ostart, ostop):
  # check ff (istop - istart)
  if (istop - istart) == 0:
      return ostop
  else:
      return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

# draw a horizontal bar
def draw_hbar(inval, yPos, barHeight):
    oled.fill_rect(0, yPos, inval, barHeight, 1) # fill with 1s

# draw a square wave
def draw_pulse_wave(dutyCycle, yOffset):
    pulses = 5
    square_wave_height = 20
    sq_wave_period = WIDTH // pulses
    high_length = int(dutyCycle * sq_wave_period / 100)
    # half the square wave period
    hswp = sq_wave_period // 2
    
    
    for i in range(0,pulses+1):
        # top bar
        oled.hline(i*sq_wave_period, yOffset-square_wave_height, high_length, 1)
        # down line
        oled.vline(i*sq_wave_period + high_length, yOffset-square_wave_height, square_wave_height, 1)
        # up line
        oled.vline(i*sq_wave_period + yOffset-square_wave_height-2, yOffset-square_wave_height+1, square_wave_height, 1)
        # bottem bar 
        oled.hline(i*sq_wave_period - (sq_wave_period - high_length), yOffset, sq_wave_period-high_length, 1)
    
    # oled.text(str(high_length), 64, 56)

def update_display(counter, xPos, dutyCycle):
    oled.fill(0)
    oled.text('Pulse Width Modu', 0, 0)
    # draw a hbar at the top yPos, height
    draw_hbar(xPos, 10, 2)
    draw_pulse_wave(dutyCycle, HALF_HEIGHT+15)
    # oled.hline(0, HALF_HEIGHT+15, WIDTH, 1)
    oled.text("Duty Cycle: " + str(round(dutyCycle)), 0, 56)
    oled.show()

counter = 0
# repeat forever
while True:
    potVal = POT_PIN.read_u16()
    # set the duty cycle on the LED for brightness
    pwm.duty_u16(potVal)
    xPos = map(potVal, 0, POT_MAX, 0, WIDTH)
    # duty cycle is a float
    dutyCycle = int(xPos / WIDTH * 100)
    update_display(counter, xPos, dutyCycle)
    led.toggle()
    sleep(.1)
    counter += 1