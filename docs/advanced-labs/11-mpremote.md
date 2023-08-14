# MicroPython Remote

MicroPython now has a standard format for all remote access.  The program
is called [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html).  There is
ample documentation on the site, and there is a higher chance it will include the latest features.

## Why Use MicroPython Remote

There are three main reasons to use **mpremote**:

1. Setting up a new device with many device drivers, data files and code.
2. Automatically updating software to get new versions and fix bugs such as security patches.
3. Moving data back and forth from your Pico to and from your host computer or a cloud server on the internet,


## List of Commands

A partial list of the most frequently used commands are:

1. **connect** - connect to a remote device
2. **disconnect** - disconnect from a remote device
3. **resume** - maintain existing interpreter state for subsequent commands.  Useful for multiple REPL commands without soft resets between the commands.
4. **soft_reset** - perform a soft-reset of the device which will clear out the Python heap and restart the interpreter. 
5. **repl** - enter the line-at-time REPL Python interpreter loop on the connected device.
6. **eval** - evaluate a string you give as a parameter on the pico using the MicroPython interpreter.
7. **exec** - execute a string and potentially run it in the background.
8. **run** - run a script from the local filesystem on the Pico
9.  **fs** - file system commands like copy, move, rename.  Examples below.
10. **df** - print size/used/free statistics for teach of the device filesystems
11. **edit** - edit a file locally.  This will copy the file to your local file systems, launch your ```$EDITOR``` program and then copy the file back to the Pico.
12. **mip** - intaller.  Like pip but it runs on the pico.  It install packages from micropython-lib (or GitHub) using the mip tool.  This can be useful if you want to automatically upgrade your software and restart the device.  If you have a wireless Pico "W" you can get new software directly from the Internet without ever needing a hardline to the Pico.
13. **mount** - mount the local directory on your PC onto the remote device (the Pico).  This will allow you to use local files directly from your MicroPython code.
14. **unmount** - unmount a local directory.  This happens automatically when mpremote terminates.
15. **rtc** - get or set the real-time clock - useful if you want to keep clocks in sync
16. **sleep** - (delay) n seconds before executing the next command
17. **reset** - hard reset the device.  It will then rerun the main.py if it finds it.
18. **bootloader** - This will make the device enter its bootloader mode so it can get an new uf2 file.  Useful if you need to upgrade to a new version of MicroPython.

Note that you can only be connected to one remote device at a time to use many commands.

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
2. Make a /lib directory using the ```mkdir```
3. Copy all the drivers for your projects to /lib directory.  The drivers you use will be dependent on the hardware you use.  For example if your kit has a display you might need to load the ssd1306.py display driver into the /lib directory.
4. Copy the default startup program to the /main.py
5. Have a sequence of "labs" that start with numbers such as 01_blink.py, 02_button.py etc.

If you follow these steps, then when the students connect to the Pico using Thonny they will see all the labs in the right order from simple to the most complex.