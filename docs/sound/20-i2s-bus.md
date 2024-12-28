# The I2S Bus

The **I2S (Inter-IC Sound)** bus on the Raspberry Pi Pico is a versatile and high-quality interface for digital audio. Here are some compelling reasons to use it:

### 1. **High-Quality Digital Audio**

-   I2S allows for precise, lossless transfer of digital audio between devices, ensuring superior sound quality compared to analog signals that are susceptible to noise and distortion.

### 2. **Low Pin Usage**

- I2S requires only a few pins to transmit high-quality audio data. This leaves other GPIO pins available for additional peripherals or projects.

### 3. **Stereo Audio Support**

- The I2S bus can handle stereo audio, making it ideal for projects requiring left and right channels, such as music players, audio recorders, or sound-based art installations.

### 4. **Ease of Integration with Digital Audio Components**

- Many digital audio devices, such as DACs (Digital-to-Analog Converters), ADCs (Analog-to-Digital Converters), and codecs, natively support I2S. This simplifies the integration of audio into your projects.

### 5. **Reduced Audio Interference**

- By keeping the audio in the digital domain until it reaches the final output stage (e.g., DAC), I2S reduces the risk of electromagnetic interference that analog signals might pick up.

### 6. **Support for Advanced Audio Formats**

-   I2S can transmit audio at various sample rates and bit depths (e.g., 16-bit, 24-bit), enabling support for high-fidelity audio formats used in modern applications.

### 7. Ideal for Audio Projects

The I2S interface is perfect for:
-   Building audio streaming devices.
-   Implementing DIY digital radios or podcast recording setups.
-   Creating smart speakers or voice assistants.

### 8. Integration with MicroPython

- The Raspberry Pi Pico's support for MicroPython and C/C++ makes it easy to work with I2S in a high-level programming environment, reducing development complexity.

### 9. Applications in Education and Prototyping

-   For educational purposes, I2S offers an opportunity to learn about digital audio processing and signal transmission. It also facilitates prototyping of commercial audio equipment.

### Example Applications

-   **DIY Digital Audio Player**: Combine an I2S DAC with an SD card reader to create a custom MP3 or FLAC player.
-   **Audio Signal Processing**: Capture audio with an I2S ADC for real-time signal analysis or effects processing.
-   **Voice Recognition Systems**: Use I2S microphones for clear audio input in speech-to-text or voice control projects.

The inclusion of I2S on the Raspberry Pi Pico opens up a world of opportunities for high-quality, efficient, and versatile audio processing in your projects.

## Robot Sounds Project

Here we describe a simple project that plays robot sound files on the Raspberry Pi Pico.

### Project: Robot Sound Player on Raspberry Pi Pico

This project will use the Raspberry Pi Pico with an I2S DAC to play pre-recorded robot sound files (e.g., "beeps," "boops," "affirmative," "error") stored on a microSD card. The sounds will be triggered using a button or slider switch.

### Components Needed

1.  **Raspberry Pi Pico** (with headers for easy wiring)
2.  **I2S DAC Module** (e.g., PCM5102)
3.  **MicroSD Card Module** (for storing sound files)
4.  **Speaker** (connected to the DAC)
5.  **Push Button** or **Slider Switch** (to trigger sound effects)
6.  **Wires** and **Breadboard**

### Steps to Build

#### 1. **Prepare the Sound Files**

-   Convert your robot sound files to a compatible format like 16-bit PCM WAV files at 44.1 kHz.
-   Store the WAV files on a microSD card with filenames like `robot1.wav`, `robot2.wav`.

#### 2. **Connect the Components**

##### MicroSD Module to Pico
-   `VCC` → Pico `3.3V`
-   `GND` → Pico `GND`
-   `MISO` → Pico `GP16`
-   `MOSI` → Pico `GP19`
-   `SCK` → Pico `GP18`
-   `CS` → Pico `GP17`
##### I2S DAC to Pico
-   `BCK` → Pico `GP10`
-   `LRCK` → Pico `GP11`
-   `DIN` → Pico `GP9`
-   `GND` → Pico `GND`
-   `VCC` → Pico `3.3V` or `5V` (depending on the module)
##### Speaker to DAC**:
    -   Connect the speaker output from the DAC module to your speaker terminals.
##### Button to Pico:**
    -   One side of the button → Pico `GP14`
    -   Other side of the button → `GND`
    -   Use a 10K pull-up resistor from `GP14` to `3.3V`.

#### 3. **Install the Required Software**

-   Install MicroPython on your Pico.
-   Upload libraries for:
    -   **I2S Audio Playback**: E.g., `i2s_audio.py`
    -   **SD Card Access**: `uos` or `os` module with MicroPython SD card libraries.
-   Format the microSD card as FAT32.

#### 4. **Write the Code**

Below is an example MicroPython code for playing sound files using a button trigger:

```python
from machine import Pin, I2S, SPI
import uos

# Initialize I2S for DAC
audio_out = I2S(
    0,
    sck=Pin(10),   # Bit clock
    ws=Pin(11),    # Word select
    sd=Pin(9),     # Serial data
    mode=I2S.TX,
    bits=16,
    format=I2S.MONO,
    rate=44100
)

# Initialize SD Card
spi = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
sd_cs = Pin(17, Pin.OUT)
uos.mount(SDCard(spi, sd_cs), "/sd")

# Button Input
button = Pin(14, Pin.IN, Pin.PULL_UP)

def play_sound(file_path):
    with open(file_path, "rb") as wav:
        wav.seek(44)  # Skip WAV header
        while True:
            buf = wav.read(2048)
            if not buf:
                break
            audio_out.write(buf)

print("Ready to play robot sounds!")
while True:
    if not button.value():  # Button pressed
        print("Playing sound!")
        play_sound("/sd/robot1.wav")
```

#### 5. Test the Setup

-   Power up the Pico.
-   Press the button to trigger playback of `robot1.wav`.
-   Swap out files or add more buttons to trigger additional sounds.

### Extensions

1.  **Multiple Buttons**: Add more buttons to trigger different sound effects.
2.  **Random Playback**: Use the `random` module to pick a random sound from the SD card.
3.  **Interactive Robot**: Connect the sound system to sensors (e.g., distance or light sensors) to play sounds based on environmental triggers.

This project is an engaging way to learn about I2S, digital audio, and MicroPython, while creating a fun and interactive robot sound player!

##### Storing the Sounds on the Pico's Flash Memory

We can store the sound files on the Raspberry Pi Pico's internal flash memory instead of using an external microSD card. However, there are a few considerations and limitations to keep in mind:

### Considerations for Storing Sounds in Flash Memory

#### **Limited Flash Storage Space**

-   The Raspberry Pi Pico has 2 MB of onboard flash memory, which is shared with the MicroPython firmware and your code.
-   Sound files (e.g., WAV) can be quite large, so you'll need to ensure the files fit within the available space.
-   Use compressed or low-bitrate audio formats if possible (e.g., 8-bit, mono, low sample rate).

#### File Size and Format

-   A typical PCM WAV file at 16-bit, 44.1 kHz uses ~88 KB per second of audio. Consider using a lower sample rate (e.g., 8 kHz) to save space.
-   Mono sound files consume less space than stereo.

#### Loading Files into Flash**

-   Store the audio files in the Pico's filesystem (accessible via MicroPython) by uploading them using a file transfer tool like **Thonny** or a command-line tool like `ampy`.

#### Playback Speed

- Flash memory access is slower than an I2S DAC with buffered SD card reading. For short sound clips, this isn't usually an issue.

### Steps to Store and Play Sounds from Flash

#### 1.Prepare the Sound Files

-   Convert your sound files to a smaller format:
    -   Mono, 8-bit PCM WAV
    -   Sample rate: 8 kHz or 16 kHz
-   Example tools for conversion:
    -   [Audacity](https://www.audacityteam.org/)
    -   `ffmpeg` command-line tool:

```bash
ffmpeg -i input.wav -ar 16000 -ac 1 -b:a 8k output.wav
```

#### 2. Upload Files to Pico

-   Open the Thonny IDE.
-   Connect your Pico.
-   In the **File Explorer**, upload your WAV file(s) to the Pico's flash memory.

#### 3. **MicroPython Code for Playback**

-  Below is an example code to play a short WAV file stored in the Pico's flash memory:

```python
from machine import I2S, Pin

# Initialize I2S for DAC
audio_out = I2S(
    0,
    sck=Pin(10),   # Bit clock
    ws=Pin(11),    # Word select
    sd=Pin(9),     # Serial data
    mode=I2S.TX,
    bits=16,
    format=I2S.MONO,
    rate=16000  # Match the WAV file's sample rate
)

def play_sound(file_path):
    try:
        with open(file_path, "rb") as wav:
            wav.seek(44)  # Skip WAV header
            while True:
                buf = wav.read(2048)
                if not buf:
                    break
                audio_out.write(buf)
    except Exception as e:
        print(f"Error playing sound: {e}")

# Play the sound file stored on the Pico
print("Playing robot sound...")
play_sound("robot1.wav")
```

#### 4. **Optimize and Test**

-   Use `uos.listdir()` to list files stored in flash memory.
-   Ensure the file format matches the I2S configuration (e.g., 8-bit or 16-bit, mono or stereo).
-   Test playback and confirm there are no buffer underruns.

### Advantages

-   Eliminates the need for external storage hardware (microSD card module).
-   Simpler wiring and lower cost.
-   Suitable for small, self-contained projects where a few short sound clips are needed.

### Limitations

-   Limited storage for audio files.
-   Requires careful management of the flash memory to avoid overwriting important files or the firmware.

For projects with just a few short robot sound effects, storing the sounds on the Pico's flash memory is a practical and convenient option.