# MIDI with MicroPython

!!! Warnining
    I am not an expert on MIDI and I don't have any MIDI gear.  This is
    mostly a collection of material I have for students that want
    to use MicroPython to generate music.



## Sample Code

### Ascending Notes

```py
# Play Test MIDI Ascending Notes
from machine import Pin, UART
import time
uart = UART(1, baudrate=31250, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=None, stop=1)
led=Pin("LED", Pin.OUT)
note = 24

while True:
    midimessage = bytearray([0x90, note, 64])
    uart.write(midimessage)
    led.toggle()
    # change third parameter to be 0
    midimessage = bytearray([0x90, note, 0])
    # pause 1/8 of a second
    time.sleep(0.125)
    note += 2
    if note > 64:
        note=24
```

## References

[Raspberry Pi Pico MIDI Development Board Midimuso](https://www.ebay.com/itm/134794678425?hash=item1f62639099:g:WbcAAOSwvMxk0qof) for $20 US.  This board has all the MIDI connectors on it.

[Simple DIY electromusic Project](https://diyelectromusic.wordpress.com/)

[DIY Electro Music SDEMP MicroPython Code on GitHub](https://github.com/diyelectromusic/sdemp/tree/main/src/SDEMP/Micropython)

[Pico MIDI by Barb Arach](https://barbarach.com/pico-midi-external-switches/)

[PicoMIDI manual v1.0](https://docs.google.com/viewer?url=https%3A%2F%2Fmidimuso.co.uk%2Fwp-content%2Fuploads%2F2023%2F07%2FpicoMIDI_manual-2.pdf)