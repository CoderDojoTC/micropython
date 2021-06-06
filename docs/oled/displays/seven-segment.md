# Sample Seven Segment Display Lab

## 4 Digit Seven Segment Display

![](../img/4-digit-7-segment-colon.png)

Make sure to put a current limiting resistor in series with each LED.  A 330 ohm resistor is a generally safe value for 5 volt circuits and you can use a 220 ohm resistor for 3.3 volt circuits.

This code was provided by Jaison Miller from his [GitHub Repo](https://github.com/zimchaa/pico_examples/blob/main/4by7segmentdisplay.py).

```py
from machine import Pin, PWM, Timer
import utime

# Constants - where the pins are currently plugged into, etc.
number_bitmaps = { 0: 0b00111111, 1: 0b00000110, 2: 0b01011011, 3: 0b01001111, 4: 0b01100110, 5: 0b01101101, 6: 0b01111101, 7: 0b00000111, 8: 0b01111111, 9: 0b01100111 }
segment_masks = { 'a': 0b00000001, 'b': 0b00000010, 'c': 0b00000100, 'd': 0b00001000, 'e': 0b00010000, 'f': 0b00100000, 'g': 0b01000000 }
pin_segments = { 'a': 10, 'b': 11, 'c': 12, 'd': 17, 'e': 16, 'f': 13, 'g': 14}
pin_others = { 'decimal': 22, 'colon': 6, 'dash': 8 }
pin_digits = { 1: 18, 2: 19, 3: 20, 4: 21 }
pin_control_others = { 'colon': 27, 'dash': 7 }

# initial setup of the pins, alternatives include using PWM to set the brightness
# if not using PWM then make sure to use appropriate resistors to avoid blowing the LEDs in the display (like I have)

segment_maps = {}

for segment, pin in pin_segments.items():
    segment_maps[segment] = Pin(pin, Pin.OUT)
    
other_pin_maps = {}

for feature, pin in pin_others.items():
    other_pin_maps[feature] = Pin(pin, Pin.OUT)

digit_maps = {}

for digit, pin in pin_digits.items():
    digit_maps[digit] = Pin(pin, Pin.OUT)
    
other_maps = {}

for feature, pin in pin_control_others.items():
    other_maps[feature] = Pin(pin, Pin.OUT)
    

def render_digit_display(show_digit=1, number=8, decimal=False):
    
    # turn everything off
    for segment, mask in segment_masks.items():
        segment_maps[segment].value(1)
        
    other_pin_maps['decimal'].value(1)

    # turn on the digit required to be displayed
    for digit, digit_pin in digit_maps.items():
        if show_digit == digit:
            digit_pin.value(1)
            # print("\n\nDigit: {} - Pin: {} - Number: {}\n".format(digit, pin, number))
        else:
            digit_pin.value(0)
            
    utime.sleep(0.001)

    display_number_bitmap = number_bitmaps[number]
    
    # check every 
    for segment, mask in segment_masks.items():
        # print("segment: {}\nmask: {}".format(segment, mask))
            
        if display_number_bitmap & mask == mask:
            # print("segment OFF: {}".format(segment))
            segment_maps[segment].value(0)
        else:
            segment_maps[segment].value(1)
    
    # show decimal
    if decimal:
        other_pin_maps['decimal'].value(0)
    else:
        other_pin_maps['decimal'].value(1)
        
    utime.sleep(0.001)

    
def render_feature_display(show_colon=False, show_dash=False):
    if show_colon:
        other_pin_maps['colon'].value(0)
        other_maps['colon'].value(1)
    else:
        other_pin_maps['colon'].value(0)
        other_maps['colon'].value(0)
        
    if show_dash:
        other_pin_maps['dash'].value(0)
        other_maps['dash'].value(1)
    else:
        other_pin_maps['dash'].value(0)
        other_maps['dash'].value(0)
 
while True:
    
    lt_year, lt_month, lt_mday, lt_hour, lt_minute, lt_second, lt_weekday, lt_yearday = utime.localtime()
    
    # testing out all the features of the display
    digit_1_decimal = (lt_second % 4 == 0)
    digit_2_decimal = (lt_second % 4 == 1)
    digit_3_decimal = (lt_second % 4 == 2)
    digit_4_decimal = (lt_second % 4 == 3)

    render_digit_display(1, lt_minute // 10, digit_1_decimal)
    render_digit_display(2, lt_minute % 10, digit_2_decimal)
    render_digit_display(3, lt_second // 10, digit_3_decimal)
    render_digit_display(4, lt_second % 10, digit_4_decimal)
    
    if (lt_second % 2 == 0):
        render_feature_display(True, False)
    else:
        render_feature_display(False, True)
    
     ```
