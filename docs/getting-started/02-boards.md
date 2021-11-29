# Micropython Boards

Technically, any computer that has at least 16K of RAM can run MicroPython as long as someone has ported the MicroPython runtime to use that instruction set.  

## Raspberry Pi Pico
Most of these lessons use a low-cost ($4 retail list price) [Raspberry Pi Pico]()(../glossary.md#pico).  The microcontroller was designed by the Raspberry Pi Foundation specifically to provide a low-cost way for student to learn how to program MicroPython.  The Raspberry Pi Foundation has also worked with the [Thonny](misc/glossary.md@thonny) developers to create a simple clean kid-friendly interface that is ideal for beginning students.

## ESP32
The [ESP32](../misc/glossary.md#ESP32) is similar to the Raspberry Pi Pico but ESP32 also has both WiFi and bluetooth.

## Cables
You will need a USB cable to program your microcontroller.  These cables are frequently sold at high margin rates at retail stores.  If you plan ahead, you can usually find these cables on eBay for about 50% less.  Classroom purchases make this a good option.


## Getting Machine Statistics

```
import machine
help(machine)
```