# https://docs.micropython.org/en/latest/library/os.html
import os
uname = os.uname()
print(uname)

# (sysname='rp2', nodename='rp2', release='1.19.1', version='v1.19.1-88-g74e33e714 on 2022-06-30 (GNU 11.2.0 MinSizeRel)', machine='Raspberry Pi Pico W with RP2040')