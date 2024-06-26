# Microcontrollers

![Microcontrollers](../img/microcontrollers.jpg)
Left to right: Raspberry Pi Pico, Cytron Maker Pi Nano, Cytron Maker Pi 2040, Cytron Maker Pi Pico, ESP-32, ESP TTGO

This lesson is an overview of microcontrollers and their role in teaching [physical computing](https://en.wikipedia.org/wiki/Physical_computing).

A [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) is a small low-cost computer used to control physical devices such as LED, servos and motors.  Microcontroller boards typically cost around $4 to $6 and are an ideal way to learn about computer science because you can use them to build fun projects.  For example you can control a row of LEDs, move a robot and sense the world around us with a variety of light, sound and motion sensors.

## Types of Microcontroller Boards Used in These Labs

We use a variety of microcontroller boards that are based on either the Raspberry Pi RP2040 chip or the ESP32.  The boards we use are all low-cost (under $10) but have a variety of on-board devices such as buttons, LEDs, speakers and motor controllers.  Which board you use depends on how many of these components you need in your projects.  The RP2040 has 264K RAM and the ESP32 has 520K RAM.

Some of the boards are mounted on breadboards and others use Grove connectors to connect sensors and actuators.

### Raspberry Pi Pico

This microcontroller is low cost (retail list price is $4) and can be mounted directly on a breadboard.  The Pico has just a single LED and no buttons.

In the past, microcontrollers were difficult for younger students to program.  They were also too expensive for every student to purchase and take home.  A typical Arduino kit could easily cost over $20 and required you to learn C to program it.

Today, microcontrollers such as the [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/) and the [ESP32](https://en.wikipedia.org/wiki/ESP32) cost as little as four dollars.  And these devices are designed to be programmed in Python, the most popular programming language for students.

## What is Physical Computing?
[Physical Computing](https://en.wikipedia.org/wiki/Physical_computing) is a field of study that can sense and respond to the world around us.  Unlike programming a cell phone or a laptop computer, our focus is reading sensor values and quickly responding to changes.  Physical Computing is widely used to teach principals of computer science because students can create their own projects and express creativity such a controlling the patterns of lights or creating complex sounds.

## How Microcontrollers are Used
Microcontrollers do three things:

1. They read sensor values of the world around them
2. They transform this data into useful representations
3. They send outputs to devices that control the world such as LEDs and motors as well as displays

Here is a general diagram to think about when you are designing microcontroller systems:
![Microcontroller Architecture](../img/microcontroller-arch.png)

Here is a specific example instance of what inputs and outputs might do.
![Microcontroller Architecture Example](../img/microcontroller-arch-example.png)

## Programming a Microcontroller

In this class, we will use the MicroPython to program our Microcontroller.  

Our programs will usually have the following structure:

1. **Imports**: Specify the Python libraries used in the code (*More Information on Python libraries are available [here](https://docs.python.org/3/tutorial/modules.html)*)
2. **Setup**: Setup/ Initialize variables and sensors 
3. **Main loop**: Continuously monitor sensor inputs and take actions

The following is an example code in Micropython:

```python
# Import Section
import machine
import time

# Setup Section
led = machine.Pin(16, machine.Pin.OUT)

# Main Loop
while True:
    led.high()
    time.sleep(0.5)
    led.low()
    time.sleep(0.5)
```

Almost all our programs will start with the `import machine` line.  This tells the system that we need to gather all the libraries that understand our physical machine.

If you couldn't understand the example program - don't worry! We will be going through it in detail as we work on our labs.

## References

* [Listing of RP2040-based Boards on the Raspberry Pi Foundation Website](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#rp2040-based-boards)
