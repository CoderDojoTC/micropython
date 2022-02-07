#!/bih/sh
# UNIX shell script to initialize RP2040 files for bots
DRIVERS=~/Documents/ws/micropython/src/drivers
rshell -p /dev/cu.usbmodem14101 mkdir lib
rshell -p /dev/cu.usbmodem14101 echo 'name="pico"' > /pyboard/board.py

rshell -p /dev/cu.usbmodem14101 cp $DRIVERS/*.py /pico/lib