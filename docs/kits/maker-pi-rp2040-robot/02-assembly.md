# Assembling Your Maker Pi RP2040 Robot

This kit is a $25 robot kit that we will use in our CoderDojo robotics classes.  This kit includes:

1. A SmartCar Chassis
    1. Two 3 to 6-volt DC geared hobby motors and wheels
    2. Plexiglass (acrylic) main board
    3. Screws and nuts
    4. 4 AA battery pack
    5. Power switch
2. Cytron Maker Pi RP2040 kit
    1. Maker Pi RP2040 board
    2. 4x Grove to female header cables
    3. Screwdriver
    4. Silicone rubber feet (pack of 4)
3. Ultrasonce sensor
    1. mounting braket
    2. 2 M2 6mm screws and nuts

You will need to provide 4 AA batteries and a Micro USB connector that works with your PC or Mac.

## Assemble the SmartCar Chassis

In this version of the kit the wires are pre-soldered onto the motors.

Here is the robot kit in all the packaging:
![](../../img/IMG_0146.jpg)

Your first task is to remove the protective backing from the acrylic body.
![](../../img/IMG_0151.jpg)

Here are all the parts removed from the packaging:
![](../../img/IMG_0153.jpg)

We mount the motors with the wires on the inside and the heads of the bolts on the outside.
![](../../img/IMG_0162.jpg)
This photo shows cable ties I have added so that the wires don't get pulled out by our students.  These cable ties are optional.

Next, we position the battery pack on the BOTTOM so that we have more room on the top for our circuit board, sensors and add-on displays.

![](../../img/IMG_0163.jpg)

I used a 1/8th inch drill bit to put holes where the battery pack should be mounted.
![](../../img/IMG_0164.jpg)

Next, I put the flat head screws in the battery pack.  We want to make sure the top of the screw is all the way in so that it does not get in the way of the battery.
![](../../img/IMG_0166.jpg)

Next we mount the rubber feat on the bottom of the Maker Pi RP2040 circuit board so that we have some space between the PC board and the main chassis.  I use the space next to the four corners to mount the feet.  Note that we must put the drag wheel on before we put the PC board on top of the chassis.
![](../../img/IMG_0167.jpg)

Next, we put the four screws and spacers in the four holes at the bottom rear of the robot directly behind the battery pack.
![](../../img/IMG_0172.jpg)

We then add the four screws to mount the drag wheel.
![](../../img/IMG_0173.jpg)

Now is a good time to check the spacing of the battery pack and the read drag wheel.  The rear drag wheel must be able to spin freely in a full circle without bumping into the battery.  If it bumps you might need to remount the battery pack before you proceed to the next step.
![](../../img/IMG_0174.jpg)

This figure has the switch that comes with the battery pack.  For our work, we will not need this switch since the Maker Pi RP2040 circuit board has an no-board power switch.  Most of our students put the switch in if they ever need to change circuit boards that don't have a built-in power switch.  If you do this, you can solder the switch between the red power of the battery and the positive terminal of VIN.
![](../../img/IMG_0175.jpg)

Next, line up the printed circuit board with the USB connector facing the rear.  Note where the holes are in the board and drill two 1/8" holes to mount the board.
![](../../img/IMG_0169.jpg)

This photo shows the holes drilled with the screws in them.
![](../../img/IMG_0170.jpg)

This is the side-view from the rear of the screws holding on the circuit board.
![](../../img/IMG_0176.jpg)

Next use two 6 mm M3 screws to mount the ultrasonic distance sensor on top front of the robot.
![](../../img/IMG_0180.jpg)
Some of our students like to mount the ultrasonic sensor under the chassis and point the sensor up a little so the sensor does not reflect off the floor.  You can use a heat gun to soften the plastic mount to change the angle.

Next I added a drop of hot-glue under the front screws that mount the pc board.  I did this because the battery pack and motor mounts get in the way of adding a nut under the board.
![](../../img/IMG_0182.jpg)

Next, I used a small rubber coated twist tie to keep the wires under the robot away from the wheels and battery.  We don't want them to drag on the floor.
![](../../img/IMG_0185.jpg)

![](../../img/maker-pi-rp2040-robot-bottom.jpg)

Next, we connect the motors up to the screw headers on the printed circuit board.  There is a screwdriver that comes with the Cytron Maker Pi RP2040 that is handy for tightening the screws.
![](../../img/IMG_0178.jpg)
Don't worry about getting the connections all correct.  They can be adjusted in your software.

Press the wheels on the motors.
![](../../img/IMG_0181.jpg)

Lastly we connect the battery to the VIN jumper, making sure to connect the red wire to the "+" terminal and the black wire to the "-" terminal.
![](../../img/IMG_0186.jpg)

Connect the Maker Pi RP2040 board to the top with the USB connector facing the rear.

 ![Maker Pi RP2040 Motor Connections](../img/maker-pi-rp2040-motor-connections.jpg)

Here is a short video of the assembly of a SmartCar Chassis.  Note that this video puts the battery on the top, where we put it on the bottom.
<iframe width="560" height="315" src="https://www.youtube.com/embed/lgCERugoVL4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


![](../../img/maker-pi-rp2040-robot-bottom.jpg)
There are many videos online how to assemble to motors to the chassis.  The trick is orienting the motors correctly and making sure the bolts don't get in the way of the wheels.


   ![Maker Pi RP2040 Motor Connections](../img/maker-pi-rp2040-motor-connections.jpg)


