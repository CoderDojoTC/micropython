# How to Debug Micropython

## Listing the Modules

```py
help('modules')
```

Result:

```txt
__main__          gc                uasyncio/funcs    uos
_boot             machine           uasyncio/lock     urandom
_onewire          math              uasyncio/stream   ure
_rp2              micropython       ubinascii         uselect
_thread           onewire           ucollections      ustruct
_uasyncio         rp2               uctypes           usys
builtins          uasyncio/__init__ uhashlib          utime
ds18x20           uasyncio/core     uio               uzlib
framebuf          uasyncio/event    ujson
Plus any modules on the filesystem
```

## Micropython issues

https://github.com/micropython/micropython/issues