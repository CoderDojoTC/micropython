# Button

In this lesson we will hook a single momentary push button up to our Raspberry Pi Nano.  We will use it to toggle the built-in LED.  We will start out with simply polling the button 10 times a second to check it's state.  Then we will show how to use an interrupt handler function to monitor events from the button.

![Momentary Button Press](../img/button-press.gif)

In the example above, we are connecting the button on the left to the lower-left corner pin of the Raspberry Pi Pico.  This is GPIO Pin 15 and is in row number 20 of our [breadboard](#02_breadboard).

## Momentary Switch Buttons

![Momentary Switch](../img/momentary-switch-button.png)

We use ["B3F" tactile switch buttons](getting-started/03-suggested-parts/#momentary-press-buttons) that can be mounted directly on our breadboards.  When the button is pressed, it connects a wire that joins two pins on one side to the two pins on the other side.  The buttons can be mounted directly over the trough in the center of the breadboard.  They typically cost under $2 for 10 buttons or about 20 cents per button.

![Momentary Switch Connection Diagram](../img/button-connection-digram.png)

## Sample Button Polling Code
```py
from machine import Pin
import time

# GPIO is the internal built-in LED
led = Pin(25, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN) # input with pull down resistor

while True:
    if button.value(): # if the value changes
	    led.toggle()
        time.sleep(0.1) # wait 1/10th of a second
```

## Interrupt Handler Version

Although the polling version is simple, it does take a lot of resources.  The button.value() is checked 10 times a second, even though the button might only be pressed once a day!

A more efficient version uses a strategy called a interrupt handler.  This is a function that is "registered" by micropython to handel external events such as a button press.

```py
# Use an interrupt function count the number of times a button has been pressed
from machine import Pin
import micropython
import time

# global value
button_pressed_count = 0

# Interrupt Service Routine for Button Pressed Events - with no debounce
def button1_pressed(change):
    global button_pressed_count
    button_pressed_count += 1

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button1.irq(handler=button1_pressed, trigger=Pin.IRQ_FALLING)

button_pressed_count_old = 0
while True:
    if button_pressed_count_old != button_pressed_count:
       print('Button 1 value:', button_pressed_count)
       button_pressed_count_old = button_pressed_count
```

## References

1. [Raspberry Pi Pico Getting Started Guide Lab 6](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6)
1. [YouTube Video](https://www.youtube.com/watch?v=nPMU10mfFbs)
2. [Switchs with trough pins](https://www.ebay.com/itm/381924159238)
3. [Sample B3F Button on eBay](https://www.ebay.com/itm/402898405046) 10 pieces for $1.50