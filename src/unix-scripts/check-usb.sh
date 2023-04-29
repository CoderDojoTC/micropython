#!/bin/sh

# check if the character file exists
if [ -c /dev/cu.usbmodem14101 ]; then
   echo /dev/cu.usbmodem14101 exists
else
   echo file /dev/cu.usbmodem14101 does not exist
fi
