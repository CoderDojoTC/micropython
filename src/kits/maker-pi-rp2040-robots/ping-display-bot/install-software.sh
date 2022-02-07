#!/bin/sh
# Shell script to install all the relevent micropython libraries on an RP2040 chip
# this script required RSHELL to be installed
# You much shut down Thonny and any other IDEs that use the port before you run this
# use "which rshell" to find the path

echo "Installing all the relevent micropython libraries on you RP2040"
echo "Using" $RSHELL_PATH "and" $RP2040_PORT
# TODO - create a UNIX shell-scripc test to see if rshell is working
rshell -p $RP2040_PORT

# Step 1: Setup the HOST Variables
RSHELL_PATH=/Users/dan/opt/miniconda3/envs/mkdocs/bin/rshell
# use "ls -d /dev/cu*" on a Mac to find the port that is being used
RP2040_PORT=/dev/cu.usbmodem14101
HOST_MICRYPYTHON_LIB_DIR=~/Documents/ws/micropython/src/drivers
HOST_SOUNDS_DIR=~/Documents/ws/robot-media/

# Step 2 name the board "pico" and create the lib and sounds directories
# rshell -p /dev/cu.usbmodem14101 echo 'name="pico"' > /pyboard/board.py
# restart rshell
# rshell -p /dev/cu.usbmodem14101 mkdir /pico/lib
# rshell -p /dev/cu.usbmodem14101 mkdir /pico/sounds
# check that  lib/     sounds/  board.py all exists

# Step 3
# copy the libraries
# cp ~/Documents/ws/micropython/src/drivers/*.py /pico/lib
# rshell -p /dev/cu.usbmodem14101 cp ~/Documents/ws/micropython/src/drivers/*.py /pico/lib

# Step 4: Copy the media files

rshell -p $RP2040_PORT cp ~/Documents/ws/robot-media/wav-8k/*.wav /pico/sounds
rshell -p $RP2040_PORT cp ~/Documents/ws/robot-media/img/bytearrays/*py /pico/img