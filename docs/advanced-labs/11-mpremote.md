# MicroPython Remote

MicroPython now has a standard format for all remote access.  The program
is called [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)

The full list of supported commands are:

1. connect
1. disconnect
1. resume
1. soft_reset
1. repl
1. eval
1. exec
1. run
1. fs - file system commands like copy, move, rename
1. df
1. edit
1. mip
1. mount
1. unmount
1. rtc
1. sleep
1. reset
1. bootloader

## Installing

The first time:

```sh
pip install --user mpremote
```

```sh
pip install --upgrade --user mpremote
```

### Install Log

I use conda and you can see that it found the mpremote package version 1.20.0

```txt
Requirement already satisfied: mpremote in /Users/dan/opt/miniconda3/envs/mkdocs/lib/python3.6/site-packages (1.20.0)
Requirement already satisfied: pyserial>=3.3 in /Users/dan/opt/miniconda3/envs/mkdocs/lib/python3.6/site-packages (from mpremote) (3.5)
Requirement already satisfied: importlib-metadata>=1.4 in /Users/dan/opt/miniconda3/envs/mkdocs/lib/python3.6/site-packages (from mpremote) (4.8.3)
Requirement already satisfied: zipp>=0.5 in /Users/dan/opt/miniconda3/envs/mkdocs/lib/python3.6/site-packages (from importlib-metadata>=1.4->mpremote) (3.4.0)
Requirement already satisfied: typing-extensions>=3.6.4 in /Users/dan/opt/miniconda3/envs/mkdocs/lib/python3.6/site-packages (from importlib-metadata>=1.4->mpremote) (3.7.4.3)
```

## Testing the Version

The version of mpremote is not yet working, but eventually, it will be used like this:

```sh
$ mpremote --version
```

```
mpremote 0.0.0-unknown
```

## Getting Help

```sh
$ mpremote --help
```

### Help Results

```txt
mpremote -- MicroPython remote control
See https://docs.micropython.org/en/latest/reference/mpremote.html

List of commands:
  connect     connect to given device
  disconnect  disconnect current device
  edit        edit files on the device
  eval        evaluate and print the string
  exec        execute the string
  fs          execute filesystem commands on the device
  help        print help and exit
  mip         install packages from micropython-lib or third-party sources
  mount       mount local directory on device
  repl        connect to given device
  resume      resume a previous mpremote session (will not auto soft-reset)
  run         run the given local script
  soft-reset  perform a soft-reset of the device
  umount      unmount the local directory
  version     print version and exit

List of shortcuts:
  --help      
  --version   
  a0          connect to serial port "/dev/ttyACM0"
  a1          connect to serial port "/dev/ttyACM1"
  a2          connect to serial port "/dev/ttyACM2"
  a3          connect to serial port "/dev/ttyACM3"
  bootloader  make the device enter its bootloader
  c0          connect to serial port "COM0"
  c1          connect to serial port "COM1"
  c2          connect to serial port "COM2"
  c3          connect to serial port "COM3"
  cat         
  cp          
  devs        list available serial ports
  df          
  ls          
  mkdir       
  reset       reset the device after delay
  rm          
  rmdir       
  setrtc      
  touch       
  u0          connect to serial port "/dev/ttyUSB0"
  u1          connect to serial port "/dev/ttyUSB1"
  u2          connect to serial port "/dev/ttyUSB2"
  u3          connect to serial port "/dev/ttyUSB3"```
```

## Examples of File System Commands

Here is the syntax of the copy file command:

```sh
mpremote fs cp main.py :main.py
```

This copies the local file "main.py" to your pico.  The colon ":" is the root of the pico.

### Setting Up a UNIX Alias

If you get tired of typing "mpremote fs cp" you can create an command-line alias called "pcp" for Pico Copy:

```sh
alias pcp='mpremote fs cp'
```

The copy command the becomes simply:

```sh
pcp main.py :main.py
```

If you place this line in your .bashrc or similar shell startup it saves you a lot of typing.

File systems examples include:

1. ```cat <file..>``` to show the contents of a file or files on the device
2. ```ls``` to list the current directory
3. ```ls <dirs...>``` to list the given directories
4. ```cp [-r] <src...> <dest>``` to copy files
5. ```rm <src...>``` to remove files on the device
6. ```mkdir <dirs...>``` to create directories on the device
7. ```rmdir <dirs...>``` to remove directories on the device
8. ```touch <file..>``` to create the files (if they don’t already exist)

## Creating Deployment Scripts

For large classrooms that teach MicroPython using kits, we recommend that you arrange
all the ```mkdir``` and copy (```cp```) file shell commands in a single UNIX shell script for consistency.

Here are the steps:

1. Update the Pico with a new image
2. Rename the image to be a file system such as '/pico' by copying the 
3. Make a /lib directory
4. Copy all the drivers for your projects to /lib directory
5. Copy the default startup program to the /main.py
6. Have a sequence of "labs" that start with numbers such as 01_blink.py, 02_button.py etc.

If you follow these steps, then when the students connect to the Pico using Thonny they will see all the labs in the right order from simple to the most complex.