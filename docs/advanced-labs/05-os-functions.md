# Raspberry Pi Pico OS Functions

In the Thonny tool, open the Terminal.  At the REPL prompt type:

```help()```

which returns

```py
help()
```

returns

```
Welcome to MicroPython!

For online help please visit https://micropython.org/help/.

For access to the hardware use the 'machine' module.  RP2 specific commands
are in the 'rp2' module.

Quick overview of some objects:
  machine.Pin(pin) -- get a pin, eg machine.Pin(0)
  machine.Pin(pin, m, [p]) -- get a pin and configure it for IO mode m, pull mode p
    methods: init(..), value([v]), high(), low(), irq(handler)
  machine.ADC(pin) -- make an analog object from a pin
    methods: read_u16()
  machine.PWM(pin) -- make a PWM object from a pin
    methods: deinit(), freq([f]), duty_u16([d]), duty_ns([d])
  machine.I2C(id) -- create an I2C object (id=0,1)
    methods: readfrom(addr, buf, stop=True), writeto(addr, buf, stop=True)
             readfrom_mem(addr, memaddr, arg), writeto_mem(addr, memaddr, arg)
  machine.SPI(id, baudrate=1000000) -- create an SPI object (id=0,1)
    methods: read(nbytes, write=0x00), write(buf), write_readinto(wr_buf, rd_buf)
  machine.Timer(freq, callback) -- create a software timer object
    eg: machine.Timer(freq=1, callback=lambda t:print(t))

Pins are numbered 0-29, and 26-29 have ADC capabilities
Pin IO modes are: Pin.IN, Pin.OUT, Pin.ALT
Pin pull modes are: Pin.PULL_UP, Pin.PULL_DOWN

Useful control commands:
  CTRL-C -- interrupt a running program
  CTRL-D -- on a blank line, do a soft reset of the board
  CTRL-E -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
```

followed by

help(modules)

```py
help('modules')
__main__          gc                uasyncio/funcs    uos
_boot             machine           uasyncio/lock     urandom
_onewire          math              uasyncio/stream   ure
_rp2              micropython       ubinascii         uselect
_thread           onewire           ucollections      ustruct
_uasyncio         rp2               uctypes           usys
builtins          uarray            uerrno            utime
cmath             uasyncio/__init__ uhashlib          uzlib
ds18x20           uasyncio/core     uio
framebuf          uasyncio/event    ujson
```

## OS Functions

```py
import os
print(dir(os))
```

returns

```
['__class__', '__name__', 'remove', 'VfsFat', 'VfsLfs2', 'chdir', 'getcwd', 'ilistdir', 'listdir', 'mkdir', 'mount', 'rename', 'rmdir', 'stat', 'statvfs', 'umount', 'uname', 'urandom']
```

## Real Time Clock

```py
from machine import RTC

rtc = RTC()
rtc.datetime((2017, 8, 23, 2, 12, 48, 0, 0)) # set a specific date and time
rtc.datetime() # get date and time
```

See [MicroPython Real Time Clock](https://docs.micropython.org/en/latest/rp2/quickref.html#real-time-clock-rtc)