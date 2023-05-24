#!/bin/sh
# UNIX shell script to initialize RP2040 files for bots
CMD=rshell -p /dev/cu.usbmodem14101 --buffer-size 512
rshell -p /dev/cu.usbmodem14101 --buffer-size 512 cp /Documents/ws/micropython/src/kits/maker-pi-rp2040-robots/tof-display-bot/i2c-scanner.py /pico
SOURCE_FILES=~/Documents/ws/micropython/src/kits/maker-pi-rp2040-robots/tof-display-bot
# write the files to the /pico
rshell -p /dev/cu.usbmodem14101 --buffer-size 512 cp $SOURCE_FILES/i2c-scanner.py /pico
rshell -p /dev/cu.usbmodem14101 --buffer-size 512 cp $SOURCE_FILES/motor-connection-test.py /pico
rshell -p /dev/cu.usbmodem14101 --buffer-size 512 cp $SOURCE_FILES/tof-display-test.py /pico
rshell -p /dev/cu.usbmodem14101 --buffer-size 512 cp $SOURCE_FILES/collision-avoidance-tof.py /pico
rshell -p /dev/cu.usbmodem14101 --buffer-size 512 cp $SOURCE_FILES/collision-avoidance-tof-eyes.py /pico
