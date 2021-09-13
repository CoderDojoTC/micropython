# Getting Started

Your robot kit will have the following components:

1. A SmartCar Chassis
    1. Two 3 to 6-volt DC geared hobby motors
    1. Plexiglass (acrylic) main board
    1. Screws and nuts
    1. 4 AA battery pack
    1. Power switch
2. Cytron Maker Pi RP2040 kit
    1. Maker Pi RP2040 board
    1. 4x Grove to Female Header Cable
    2. Screwdriver
    3. Silicone Rubber Feet (Pack of 4)
3. Time of Flight distance sensor
    1. 3D printed mount
    2. 2 M2 6mm screws and nut

You will need to provide 4 AA batteries and a micro USB connector.

## Install the MicroPython Runtime Library

The **Maker Pi RP2040** comes with an incompatible Python run-time.  Our first step is to re-initialize the board with the Raspberry Pi [flash_nuke.uf2](https://www.raspberrypi.org/documentation/pico/getting-started/static/6f6f31460c258138bd33cc96ddd76b91/flash_nuke.uf2) runtime.  We can then load the latest MicroPython libraries.

To do this **hold down** the BOTSEL button on the main board while you turn on the board using the on-board power switch.  This will make the board look like a USB drive.  You can then just drag the flash-nuke file onto the drive and the board will be initialized.  Make sure to power the board off and back on.

You can now repeat this process with the [Raspberry Pi MicroPython Runtime](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2).  Just remember to press and hold down the BOTSEL **before** you turn on the board and reboot after the image has been copied to the microcontroller.

If you have never used MicroPython, the Raspberry Pi Foundation has a nice [Getting Started Guide](https://www.raspberrypi.org/documentation/microcontrollers/micropython.html) that can be helpful.

## Get Familiar with your IDE (Thonney) and the Basic Programs

There are many Integrated Development Environments (IDEs) that work with the Raspberry Pi RP2040 chip.  The one you chose just should support MicroPython and be able to upload and run new programs.  Once you turn on the board you should be able to configure Thonny to use the Raspberry Pi MicroPython interface.  When you press the Stop/Reset button you should see the MicroPython RPEL prompt.

![](../../img/thonny-micropython-pico.png)

## Assemble the SmartCar Chassis

1. Solder red and black motor wires to the motors.  I use the convention of connecting the red wires to the right connector when you view the motor from the back
2. There are many videos online how to assemble to motors to the chassis.  The trick is orienting the motors correctly and making sure the bolts don't get in the way of the wheels.
3. We prefer connecting the battery pack to the bottom of the chassis.  This leaves more room on the top for adding buttons and displays.
4. Connect the Maker Pi RP2040 board to the top with the USB connector facing the rear.
5. Connect the motors to the headers using the screwdriver.  Don't worry about getting the connections all correct.  They can be adjusted in your software.
6. Connect the black battery wire to the "-" on the black header
7. Connect the battery red through the switch and to the "+" on the black header.  You technically don't need the switch since the board has it's own power switch.

## Test the Motor Connections

Use the [Motor Connection Lab](07-motor-connection-lab.md)

## Getting Help

MicroPython on the RP2040 is the most powerful low-cost system on the market today.  With 264K of RAM, it will take a LOT of work to run out of memory.  But with all things new, there is a lock of good documentation, drivers and sample code.  To help you along, we suggest the following resources:

1. The [MicroPython Raspsberry Pi Forum](https://forum.micropython.org/viewforum.php?f=21&sid=73745cabd6bbdacfd3e78419d5064dfe).  Be sure use the search to check for prior questions.
2.  

