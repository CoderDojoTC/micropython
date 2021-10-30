# Using rshell on the Raspberry Pi Pico

Using an IDE such as Thonny you can copy one file at a time to the Raspberry Pi Pico by creating a new file and doing a copy/paste of the code into that new file.  However, this process becomes slow and tedious if you want to copy a large number of files.  To do this we will use the "remote shell" program from the command line.  In our classes we often want to copy a dozen or more files to a new robot for student to try out.

Rshell was written by David Hyland.  The source code and installations are documented on Dave's GitHub repository here: [https://github.com/dhylands/rshell](https://github.com/dhylands/rshell).  Dave added support for the Raspberry Pi Pico in release [0.0.30](https://github.com/dhylands/rshell/releases/tag/v0.0.30) in March of 2021.

Rshell's primary use is to to get filesystem information on the pico (ls), and to copy files to and from MicroPython's filesystem.  It can also be used as a terminal to run interactive RPEL commands.


## Conda Setup

If you are new to Python and you don't have any previous virtual environments set up you can skip this step.  Experienced Python developers have many different environments that they want to keep separated due to library incompatibility issues.  Here is how to create a new Python Conda environment that keeps your rshell libraries separated.

```sh
conda create -n pico python=3
conda deactivate
conda activate pico
```

Your prompt should now indicate you are in the pico environment.

## Install rshell in your pico environment
We will now use the standard pip installer tool to install the rshell command.

```sh
python -m pip install rshell
```

You can check that rshell has been correctly installed in your command PATH by running the UNIX ```which``` command.

```sh
which rshell
```

## Running shell

Rshell communicates with the Pico through the USB port.  When you plug in the Pico you should see a new file created in the UNIX /dev directory.  It typically begins with the letters ```/dev/cu.modem```.  One way to test this is to unlpug the pico and run the following command:

```sh
ls /dev/cu.usbmodem*
```
With the pico unplugged, there should be no files that match the ls wildcard pattern.  However, after you plug in the pico the following should be returned:

```
/dev/cu.usbmodem14101
```

This is the port you will use to connect to the pico.  We will use the ```-p``` for port option to startup rshell.

```sh
rshell -p /dev/cu.usbmodem14101
```

```
Using buffer-size of 128
Connecting to /dev/cu.usbmodem14101 (buffer-size 128)...
Trying to connect to REPL  connected
Retrieving sysname ... rp2
Testing if ubinascii.unhexlify exists ... Y
Retrieving root directories ... /LCD_SPI.py/ /lcd-spi-test.py/ /lcd-test.py/ /lcd.py/
Setting time ... Oct 28, 2021 20:30:56
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 1970
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
```

## Boards

The boards command will list the boards rshell is connected to:

boards
pyboard @ /dev/cu.usbmodem14101 connected Epoch: 1970 Dirs: /pyboard/hello.py /pyboard/main.py

## Listing Files

We can see that the board is called "pyboard" and you can use that as a path to list the files on the board.

```sh
ls /pyboard
hello.py      main.py
```

## Giving Your Board a Name

rshell will look for a program called board.py when it connects to the board.  If this file contains a board name it will use that as the board name the next time it connects to the board.  You can use the "echo" command to generate the file.  In the example below, we will call our board "pico"

```sh
echo 'name="pico"' > /pyboard/board.py
```

After you use the CONTROL-C and reconnect you will see the following:

```
pico @ /dev/cu.usbmodem14101 connected Epoch: 1970 Dirs: /pico/hello.py /pico/main.py
```

Remember you must disconnect from rshell and reconnect before the boards.py function is used.

For the remainder of this lesson we will assume you have renamed your board "pico".

You can then type ```cd /pico``` followed by a ```ls``` to see the files on your pico.

## Entering REPL
You can enter the REPL loop using the ```repl``` command and use the same commands that you used in the Thonny shell.

```
repl
print('Hello World!')
```

returns

```
Hello World!
```

## Getting Help on rshell commands

You can type the ```help``` command to see all the rshell commands:

```
help

Documented commands (type help <topic>):
========================================
args    cat  connect  date  edit  filesize  help  mkdir  rm     shell
boards  cd   cp       echo  exit  filetype  ls    repl   rsync

Use Control-D (or the exit command) to exit rshell.
```

## Running Backup

If you want to copy all the python files from the pico to a backup directory you can use the following command:

```
cd /pico
cp *.py /Users/dan/backup
```

You will need to create the /Users/dan/backup directory before you do this.  You can also use the tilde ```~``` character to stand in for your home directory like this:

```sh
cp *.py /Users/dan/backup
```

Copying '/pico/hello.py' to '/Users/dan/backup/hello.py' ...
Copying '/pico/main.py' to '/Users/dan/backup/main.py' ...

## Installing files

If you have a directory called ```~/build``` that contains many files you want to install on the pico file system you can use the following command:

```sh
cp ~/build/* /pico
```

If you have done a clone to the CoderDojoTC micropython repository and put it in your home directory under ~/micropython then following command will copy the python files from the Maker Pi RP2040 kit to your pico:

```sh
mkdir /pico/lib
cp ~/micropython/src/drivers/*.py /pico/lib
cp ~/micropython/src/kits/maker-pi-rp2040/*.py /pico
cp ~Documents/ws/micropython/src/kits/maker-pi-rp2040-robots/*.py /pico/lib
```

Note that the drivers will be placed in the /lob directory.

## Direct Command Execution

You do not need to use an interactive session to run a command with rshell.  You can just add the command you would like to run to the end of the rshell command like this:

```sh
rshell -p /dev/cu.usbmodem14101 ls /pico
```

returns:

```
hello.py      main.py
```

