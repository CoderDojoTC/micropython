# Playing and Audio File

Note: This is a work in progress.  There is a bug in the .wav file player on my test system.

Although we can play tones of various pitches using the PMW to generate square waves, the quality of this sound is not close to high-fidelity sound like you would expect in a personal MP3 audio player.

In this lesson we will demonstrate how to play a high-quality audio file that is stored on the non-volatile static memory of the Pico.  According to the specification of the [](https://www.raspberrypi.com/products/raspberry-pi-pico/specifications/), the system comes with 2MB on-board QSPI Flash that we can use to store sound files.  By combining our Pico with an SD card reader we can play many sounds and even full-length songs and albums.

## Connections
GPIO pin 14 and 15 are the output.  We will need to use an amplifier or head phone with a 1K resistor in series on the pins.

The myPWM subclass set the maximum count to 255(8 bits)  or 1023(10bits)  at a frequency 
around 122.5KHz.

The PWM is now on 10 bits (0..1023)

The myDMA class allows to use direct memory access to transfer each frame at the current sample rate

You need to install the wave.py and chunk.py from
     https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio

Don't forget to increase the SPI clock up to 3Mhz.


How it works,

   1 - We set the PWM to a range of 255 at 122Khz
   2 - We read the wave file using the class wave which will set the 
       sample rate and read the audio data by chunk
   3 - Each chunk are converted to 16 bit signed to unsigned char 
       with the middle at 128, (512 for 10 bits)
   4 - Wait for the DMA to be completed.  On first it will be 
       anyway.
   5 - The converted chunk is then pass to the DMA to be transfer at 
       the sample rate using one of build in timer
   6 - Go on step 2 until is done.
   
P.S. to transfer wave file use rshell.

## Steps to test playing a wav file

### Clone the Pico Audio PWM GitHub Repository
```sh
git clone https://github.com/danjperron/PicoAudioPWM
cd PicoAudioPWM
```

## Download some test robot wav files

## Converting .MP3 to .WAV files

This software only currently support playing .wav files since it is easy to convert these files into a format that can be played. WAV files store uncompressed audio, so they are larger than MP3 files.  Wav files are simple ways to store sound patterns.  MP3 files are much more complex and require complex algorithms to convert into sound outputs.

 The usual bitstream encoding is the linear pulse-code modulation (LPCM) format.

You can use the following web-site to convert MP3 files into wave files:

[Cloud Convert Service that Converts MP3 to WAV files](https://cloudconvert.com/mp3-to-wav)

## Copy Sound Files to the Pico

Your pico has 2MB of static memory.  You can copy many sound effect files to the pico file system and play them.  Some IDEs may allow you to do this.

Here is an example of using the [rshell](../advanced-labs/11-rshell.md) program to copy a directory of wav files to the pico.  Lines that start with pc$ are commands that you type into your PC or MAC's terminal.  Lines that start with rs$ are commands that you type into the rshell.

```sh
# list the devices (only works on Mac and UNIX)
pc$ ls /dev/cu.modem*
# start the rshell
pc$ rshell -p /dev/cu.modem*
# change the name of the device to be "pico"
rs$ echo 'name="pico"' > /pyboard/board.py
# exit from rshell - can also use exit
CONTROL-C
# reconnect with the rshell
$pc rshell -p /dev/cu.modem*
# go into the /pico file systems
$rs cd /pico
# create a directory for all our sound files
mkdir sounds
# copy files from hour PC's home ~/tmp/sounds dir to the pico
rs$ cp ~/tmp/sounds/*.wav /pico/sounds
rs$ ls /pico/sounds
```

## Listing the Wave Files

After you have a list of Wave files loaded you can verify them by using the os listdir() function.

```py
import os

waveFolder= "/sounds"
wavelist = []

# get a list of .wav files
for i in os.listdir(waveFolder):
    if i.find(".wav")>=0:
        wavelist.append(waveFolder+"/"+i)
    elif i.find(".WAV")>=0:
        wavelist.append(waveFolder+"/"+i)
            
if not wavelist :
    print("Warning NO '.wav' files")
else:
    for i in wavelist:
        print(i)
```

Sample console output

```
/sounds/cylon-attention.wav
/sounds/cylon-by-your-command.wav
/sounds/cylon-excellent.wav
/sounds/cylon-eye-scanner.wav
/sounds/cylon-see-that-the-humans.wav
/sounds/cylon-those-are-not-the-sounds.wav
```

## Checking the WAV File Format

There is a standard Python module called ```wave.py`` that reads the .wav files and shows the metadata for the file.  Wave files come in many formats, single channel, stereo and different bit rates.  The wave player can show us all this data that describes the wave file.

The report shows you how to use fixed-width formatting since the file names and data should fit in columns to make it easier to read.

```py
import os
import wave

waveFolder= "/sounds"
wavelist = []

# get a list of .wav files
for i in os.listdir(waveFolder):
    if i.find(".wav")>=0:
        wavelist.append(waveFolder+"/"+i)
    elif i.find(".WAV")>=0:
        wavelist.append(waveFolder+"/"+i)
            
if not wavelist :
    print("Warning NO '.wav' files")
else:
    print("{0:<45}".format('File Path'), 'Frame Rate  Width Chans Frames')
    for filename in wavelist:
        f = wave.open(filename,'rb')
        # the format string "{0:<50}" says print left justified from chars 0 to 50 in a fixed with string
        print("{0:<50}".format(filename),
              "{0:>5}".format(f.getframerate()),
              "{0:>5}".format(f.getsampwidth()),
              "{0:>6}".format(f.getnchannels()),
              "{0:>6}".format(f.getnframes())
              )
```

Sample Response

```
File Path                                     Frame Rate  Width Chans Frames
/sounds/cylon-attention.wav                         8000     1      1   6399
/sounds/cylon-by-your-command.wav                  11025     1      1  12583
/sounds/cylon-excellent.wav                        22050     1      1  48736
/sounds/cylon-eye-scanner.wav                      16000     2      2  24768
/sounds/cylon-see-that-the-humans.wav              11025     1      1  30743
/sounds/cylon-those-are-not-the-sounds.wav         22050     1      1  64137
```

## Playing the Same Sound Repeatedly

```py
import os as uos
from wavePlayer import wavePlayer
player = wavePlayer()

try:
    while True:
        player.play('/sounds/cylon-eye-scanner.wav')
except KeyboardInterrupt:
    player.stop()
    print("wave player terminated")
```

## Downloading the Audio Libraries

Both the wave.py and the chunck.py files are here:

https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio

## References

1. [Daniel Perron](https://github.com/danjperron/PicoAudioPWM)
2. [Wikipedia Wave File](

)