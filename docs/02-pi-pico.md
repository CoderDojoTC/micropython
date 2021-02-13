# Getting Started with the Raspberry Pi Pico
The Raspberry Pi Pico is a custom silicon microcontroller built by the [Raspberry Pi Foundation](glossary#raspberry-pi-foundation) with a retail list prices of $4.  With 264K SRAM, it has around 100 times the RAM of an Arduino Uno (2K).  It is ideal for projects that need more RAM such as project that require drawing to an OLED display.

## Specs

* RP2040 microcontroller chip designed by Raspberry Pi in the United Kingdom
* Dual-core Arm Cortex M0+ processor, flexible clock running up to 133 MHz
* 264KB of SRAM, and 2MB of on-board Flash memory
* Castellated module allows soldering direct to carrier boards
* USB 1.1 with device and host support
* Low-power sleep and dormant modes
* Drag-and-drop programming using mass storage over USB
* 26 × multi-function GPIO pins
* 2 × SPI, 2 × I2C, 2 × UART, 3 × 12-bit ADC, 16 × controllable PWM channels
* Accurate clock and timer on-chip
* Temperature sensor
* Accelerated floating-point libraries on-chip
* 8 × Programmable I/O (PIO) state machines for custom peripheral support

## Pico Pinout
The pinout diagram for the Raspberry Pi.

It features: 
* 26 × multi-function GPIO pins
* 2 × SPI, 2 × I2C, 2 × UART, 3 × 12-bit ADC, 16 × controllable PWM 
![](img/pi-pico-pinout.png)
* [Pinout PDF](https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf)

Pins are numbered 0-29, and 26-29 have ADC capabilities
Pin IO modes are: Pin.IN, Pin.OUT, Pin.ALT
Pin pull modes are: Pin.PULL_UP, Pin.PULL_DOWN

## Steps To Get Micropython Running on the Mac

1. Download the MicroPython UF2 file.
2. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is connected.
It will mount as a Mass Storage Device called RPI-RP2.
3. Drag and drop the MicroPython UF2 file onto the RPI-RP2 volume. Your  Pico will reboot. You are now running MicroPython.

## Using Thonny
Thonny is a free lightweight Python development tool.

1. Download the Thonny Application
2. Download the Thonny Pico driver
3. Configure Thonny to use the Pico interpreter
4. Test using the help() function
5. Test by running a blink application

```py
from machine import Pin
import utime

# right uppermost pin with USB on the left
led = Pin(16, Pin.OUT)
led.low()
while True:
   led.toggle()
   utime.sleep(1)
```
Press the Play Button

## References
### Getting Started Guide
[Raspberry Pi Getting Started](https://www.raspberrypi.org/documentation/pico/getting-started/)

### Book PDF
[](https://hackspace.raspberrypi.org/downloads/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBaThSIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--d43ee613629bddf78bc41c1479c2acb2ec6ef34e/RPi_PiPico_Digital_v10.pdf)
Commons Attribution-NonCommercial-ShareAlike 3.0 Unported
(CC BY-NC-SA 3.0)
