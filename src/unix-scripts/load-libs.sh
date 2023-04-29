#!/bin/sh
# UNIX shell script to load drivers into /pico/lib filesystem
DRIVERS=~/Documents/ws/micropython/src/drivers
# copy the driver files
rshell -p /dev/cu.usbmodem14101 mkdir /pico/lib
rshell -p /dev/cu.usbmodem14101 cp $DRIVERS/*.py /pico/lib
