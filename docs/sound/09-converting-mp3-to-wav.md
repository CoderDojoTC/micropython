# Converting MP3 to WAV formats

In last lab we will learned how to play an audio file stored on the flash memory or SD card.  We are used an early version of a program that plays .WAV files in a fixed format: 8,000 samples per second using 16-bit encoding.  Because there are hundreds of different formats of audio files, we need a consistent way to convert all of these formats to 8K samples/second 16-bit .WAV formats.

The audio data file conversions are done on your host PC, not the microcontroller. This allows us to use a rich library of tools that don't need to run on our microcontroller.

## Method 1: Use the ffmpeg Command Line Tool

One of the easiest ways to get started is to go to the web site [ffmpeg.org](https://www.ffmpeg.org/download.html) and download the program that does the conversion using a command line.  Note that on a Mac you will need to go into your System Preferences and indicate that the following programs are trusted:

Here are the direct links for MacOS

1. [ffmpeg (mac)](https://evermeet.cx/ffmpeg/ffmpeg-104676-g5593f5cf24.zip)
2. [ffprobe (mac)](https://evermeet.cx/ffmpeg/ffprobe-104676-g5593f5cf24.zip)
3. [ffplay (mac)](https://evermeet.cx/ffmpeg/ffplay-104454-gd92fdc7144.zip)

This will download a zip file which you will need to unzip and place in a location such as ```~/bin```.  After you do this make sure you add ```~/bin`` to your path by adding the following file to your .bash_profile:

```PATH=$PATH:~/bin```

After you source your .bash_profile type in the following:

```which ffmpeg```

This should return the location that it finds the ffmpeg shell script.  You can then see the many file-format MPEG options:

```ffmpeg --help```

## Converting MP3 to 8K 16 bit WAV Files

To get the format we need for the MicroPython wave player class we just specific ```-i``` for the input file and use the ```-ar 8000``` to specify the output bit rate of 8K samples per second.  The final parameter is a file name that must in ```.wav``` so the command knows to use WAV PCM encoding.  The default value is 16 gits per sample.

```sh
ffmpeg -i r2d2-beeping.mp3 -ar 8000 r2d2-beeping-8k.wav
```

## Bulk Conversions

We can use unix shell commands to do a batch conversion of all the .  The following is an example of using awk and sed to convert all the .mp3 files in a directory and convert them to 8K Hz WAV files and put them in a sibling directory.

```sh
ls -1 *.mp3 | awk '{print "ffmpeg -i " $1 " -ar 8000 ../wav-8k/"$1}' | sed s/mp3$/wav/ | sh
```

## Inspect the Files Using the UNIX file command:

```sh
cd ../wav-8k
file *.wav
```

returns
```
r2d2-another-beep.wav:          RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-beeping-2.wav:             RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-beeping-4.wav:             RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-beeping-8k.wav:            RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-beeping-like-an-alarm.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-beeping.wav:               RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-cheerful.wav:              RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-determined.wav:            RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-excited.wav:               RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-laughing.wav:              RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-more-chatter.wav:          RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-processing.wav:            RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-sad.wav:                   RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-shocked.wav:               RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-surprised.wav:             RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-taking-to-himself.wav:     RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
r2d2-unsure.wav:                RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
```

Note that these are WAVE audio, Pulse-code Modulated (PCM), 16 bit and mono at 8K Hz.

## Method 2: Use the pydub Python Module

!!! Note
    This section is only for experienced Python developers.

### Install Conda and the Python libraries

```sh
conda create -n mp3-to-wav python=3
conda activate mp3-to-wav
pip install pydub ffprobe ffmpeg
```

Check your versions:

```sh
pip freeze
```

returns:

```
ffmpeg==1.4
ffprobe==0.5
pydub==0.25.1
```

### Running pydub

```py
from pydub import AudioSegment

sound = AudioSegment.from_mp3("r2d2-beeping.mp3")
sound.export("r2d2-beeping.wav", format="wav", tags={'Robot name': 'R2D2'})
```

## Transferring the Files with Rshell

```sh
cd ../wav-8k
rshell -p /dev/cu.usbmodem14101
cp *.wav /pico/sounds
```

## References

1. [PyDub Documentation](http://pydub.com/)
2. [File Formats for Audio from MPEG](http://www.ffmpeg.org/general.html#Audio-Codecs)
3. [File Formats for motion picture experts group Python Library](http://www.ffmpeg.org/general.html#File-Formats)
