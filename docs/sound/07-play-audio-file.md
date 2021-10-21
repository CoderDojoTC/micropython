# Playing and Audio File

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


## References

[Daniel Perron](https://github.com/danjperron/PicoAudioPWM)