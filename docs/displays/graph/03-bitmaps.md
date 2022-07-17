# Drawing Bitmaps with MicroPython

## Framebuffers

A [Framebuffer](../../misc/glossary.md#framebuffer) is the core data structure we use when drawing bitmaps. 

## Block Image Transfers (blit)
The basic function we use to draw a rectangular region of the screen is called the ```blit()``` function:

```py
display.blit(frame_buffer, x, y)
```

This function moves all the data within any frame buffer to the given (x,y) position of the display.  The function will check the dimensions of the frame buffer to know how much data to move to the display.  You just need to tell the function where to start drawing.

## Blit Functions Are Efficient

Blit operations can be much more efficient then the ```display.show()``` function when you are just updating a small region of the screen.  This is because the ```display.show()``` function transfers the entire screen image each time it is called.  Using ```blit``` functions can be written to only update the area of the screen that changes.

For example, if you are writing a video game that has a ball moving across the screen, you only need to update the pixels around the ball, not the entire screen image.  The exact performance difference between ```show()``` and ```blit()``` operations will depend on the size of the screen, the size of the blit update and the speed of the transfer of data from the framebuffer to the display device.

The key disadvantage of using ```blit()``` functions is that you must consider what other artifacts there are on the screen that you might overwrite.  Keeping track of the differences requires more computation by the microcontroller.  The more powerful your microcontroller is relative to the communication speed, the more difference computations you can do.

Not all display drivers will let you write directly from the microcontroller resident image directly to a region of the display.  Sometimes you must follow your blit() operations with a show() to transfer the entire framebuffer to the display.

## Working with ByteArrays

MicroPython blit operations use a data representation format for images called a ByteArray.  These are sequences of the bytes that will be sent in a blit operation.  They are coded using the following notation:

```py
my_bytearray = (b"\xFF\xFF\xFF\xBF\xDF\xEF\xF7\xFF\xFB\xFF\xFD")
```

Note that the letter ```b``` begins the parameter to show the Python interpreter that the all the characters between the double quotes are byte array values.  The characters ```\x``` indicate that there are hexadecimals useds to encode the bit values.

## Image Encoding Options

There are several alternate methods to encode the bits of an image into a byte array.  The bits can be coded left to right or top to bottom.  You can also put the bits in most-significant bit first or least-significant bit first.  All these options and controlled when you interface with a framebuffer.

### Vertical Least Significant Bit Layout
framebuf.MONO_VLSB
Monochrome (1-bit) color format This defines a mapping where the bits in a byte are vertically mapped with bit 0 being nearest the top of the screen. Consequently each byte occupies 8 vertical pixels. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered at locations starting at the leftmost edge, 8 pixels lower.

## References

[MicroPython Bitmap Tool Video](https://www.youtube.com/watch?v=a7MzPA0T_MM) - this video created by Lucky Resistor
is a good overview of the image formats used by MicroPython.