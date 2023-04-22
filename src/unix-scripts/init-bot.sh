#!/bih/sh
# UNIX shell script to initialize RP2040 files for bots
DRIVERS=~/Documents/ws/micropython/src/drivers
# create the lib directory
rshell -p /dev/cu.usbmodem14101 mkdir lib
# write the file to change the name to be /pico
rshell -p /dev/cu.usbmodem14101 echo 'name="pico"' > /pyboard/board.py
# restart here
# TBD
# copy the driver files
rshell -p /dev/cu.usbmodem14101 cp $DRIVERS/*.py /pico/lib