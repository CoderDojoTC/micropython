# Converting MP3 to WAV formats

Our micropython library is limited to 8K sound files

This is done on your host PC, not the microcontroller. This

## Method 1: Use the ffmpeg Command Line Tool

```sh
ffmpeg -i r2d2-beeping.mp3 -ar 8000 r2d2-beeping-8k.wav
```

## Bulk Conversions

We can use unix shell commands to do a batch conversion.  The following is an example of using awk and sed to convert all the .mp3 files in a directory and convert them to 8K WAV files and put them in a sibling directory.

```sh
ls -1 | awk '{print "ffmpeg -i " $1 " -ar 8000 ../wav-8k/"$1}' | sed s/mp3$/wav/ | sh
```

## Inspect the Files Using the UNIX file command:

```sh
file *
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

Note that these are WAVE audio, Pulse-code Modulated (PCM), 16 bit and mono at 8K.


## Method 2: Install Conda and the Python libraries

```sh
conda create -n mp3-to-wav python=3
conda activate mp3-to-wav
pip install pydub ffprobe ffmpeg
```

```sh
pip freeze
```

returns:

```
ffmpeg==1.4
ffprobe==0.5
pydub==0.25.1
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
