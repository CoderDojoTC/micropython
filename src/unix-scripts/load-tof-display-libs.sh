#!/bin/sh
# UNIX shell script to load drivers into /pico/lib filesystem
DRIVERS=~/Documents/ws/micropython/src/drivers
# create the /pico lib dir if it does not exist
rshell -p /dev/cu.usbmodem14101 mkdir /pico/lib
# Copy the driver files
# Copy the display driver
rshell -p /dev/cu.usbmodem14101 cp $DRIVERS/ssd1306.py /pico/lib
# Copy tne time of flight distance sensor
rshell -p /dev/cu.usbmodem14101 cp $DRIVERS/VL53L0X.py /pico/lib

