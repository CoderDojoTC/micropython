# Minicom

## Installation

### Installation on a Mac

```sh
brew install minicom
```

### Installation on Linux (Raspberry Pi OS)

```sh
sudo apt install minicom
```

## Verification of Installation

```sh
which minicom
```

```
/usr/local/bin/minicom
```

```sh
minicom --version
```

```
minicom version 2.8 (compiled Jan  4 2021)
```

```sh
minicom --help
```

returns:
```
Usage: minicom [OPTION]... [configuration]
A terminal program for Linux and other unix-like systems.

  -b, --baudrate         : set baudrate (ignore the value from config)
  -D, --device           : set device name (ignore the value from config)
  -s, --setup            : enter setup mode
  -o, --noinit           : do not initialize modem & lockfiles at startup
  -m, --metakey          : use meta or alt key for commands
  -M, --metakey8         : use 8bit meta key for commands
  -l, --ansi             : literal; assume screen uses non IBM-PC character set
  -L, --iso              : don't assume screen uses ISO8859
  -w, --wrap             : Linewrap on
  -H, --displayhex       : display output in hex
  -z, --statline         : try to use terminal's status line
  -7, --7bit             : force 7bit mode
  -8, --8bit             : force 8bit mode
  -c, --color=on/off     : ANSI style color usage on or off
  -a, --attrib=on/off    : use reverse or highlight attributes on or off
  -t, --term=TERM        : override TERM environment variable
  -S, --script=SCRIPT    : run SCRIPT at startup
  -d, --dial=ENTRY       : dial ENTRY from the dialing directory
  -p, --ptty=TTYP        : connect to pseudo terminal
  -C, --capturefile=FILE : start capturing to FILE
  --capturefile-buffer-mode=MODE : set buffering mode of capture file
  -F, --statlinefmt      : format of status line
  -R, --remotecharset    : character set of communication partner
  -v, --version          : output version information and exit
  -h, --help             : show help
  configuration          : configuration file to use

These options can also be specified in the MINICOM environment variable.
This variable is currently unset.
The configuration directory for the access file and the configurations
is compiled to /usr/local/Cellar/minicom/2.8/etc.

Report bugs to <minicom-devel@lists.alioth.debian.org>.
```


## References

1. [](https://github.com/lilberick/MicroPython/tree/main/RPiPico)