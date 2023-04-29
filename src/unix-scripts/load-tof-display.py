#!/bin/sh
# UNIX shell script to initialize RP2040 files for bots
SOURCE_FILES=~/Documents/ws/micropython/src/kits/maker-pi-rp2040-rotobs/tof-display-bot
# write the files to the /pico
rshell -p /dev/cu.usbmodem14101 cp $SOURCE_FILES/* /pico
