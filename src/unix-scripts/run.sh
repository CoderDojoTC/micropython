#!/bin/sh
echo 'running init'
./init-pico.sh
echo 'running load libraries'
./load-libs.sh
echo 'running programs'
./load-tof-display.py
