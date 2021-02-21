"""
LCD1602/2002/2004 I2C adapter driver for Raspberry Pi or other devices

Copyright (C) 2019 SiYu Wu <wu.siyu@hotmail.com>. All Rights Reserved.

"""

__author__ = 'SiYu Wu <wu.siyu@hotmail.com>'

import smbus
import time

name = 'i2clcd'

# Note for developers
#
# I2C byte:   [H ------------------------ L]
#             [    data    ]  [  ctrl_bits ]
# PCA8574:    P7  P6  P5  P4  P3  P2  P1  P0
# LCD1602:    D7  D6  D5  D4  BT  E   R/W RS

# Define some device constants
LCD_DAT = 0x01  # Mode - Sending data
LCD_CMD = 0x00  # Mode - Sending command

# LINE_1 = 0x80   # LCD RAM address for the 1st line
# LINE_2 = 0xC0   # LCD RAM address for the 2nd line
# LINE_3 = 0x94   # LCD RAM address for the 3rd line
# LINE_4 = 0xD4   # LCD RAM address for the 4th line
LCD_LINES = (0x80, 0xC0, 0x94, 0xD4)

# Character code for custom characters in CGRAM
CGRAM_CHR = (b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07')


class i2clcd():
    def __init__(self, i2c_bus=1, i2c_addr=0x27, lcd_width=16):
        """
        initialize the connection with the LCD

        i2c_bus:    the smbus where the LCD connected to,
                    for Raspberry Pi, it should be 1 or 0 (depending on the model)
        i2c_addr:   I2C address of the adapter, usually 0x27, 0x20 or 0x3f
        lcd_width:  the width of the LCD, e.g. 16 for LCD1602, 20 for LCD2002/2004
        """
        self._bus = smbus.SMBus(i2c_bus)
        self._i2c_addr = i2c_addr
        self._lcd_width = lcd_width

        self._backlight = True
        self._last_data = 0x00

    def _i2c_write(self, data):
        """write one byte to I2C bus"""
        self._last_data = data
        self._bus.write_byte(self._i2c_addr, data)

    def _pluse_en(self):
        """proform a high level pulse to EN"""

        time.sleep(0)
        self._i2c_write(self._last_data | 0b00000100)
        time.sleep(0)
        self._i2c_write(self._last_data & ~0b00000100)
        time.sleep(0)

    def write_byte(self, data, mode):
        """write one byte to LCD"""

        data_H = (data & 0xF0) | self._backlight * 0x08 | mode
        data_L = ((data << 4) & 0xF0) | self._backlight * 0x08 | mode

        self._i2c_write(data_H)
        self._pluse_en()

        self._i2c_write(data_L)
        self._pluse_en()

        time.sleep(0.0001)

    def init(self):
        """
        Initialize the LCD
        """

        # setting LCD data interface to 4 bit
        self._i2c_write(0x30)
        self._pluse_en()
        time.sleep(0.0041)
        self._i2c_write(0x30)
        self._pluse_en()
        time.sleep(0.0001)
        self._i2c_write(0x30)
        self._pluse_en()
        time.sleep(0.0001)
        self._i2c_write(0x20)
        self._pluse_en()

        self.write_byte(0x28, LCD_CMD)    # 00101000 Function set: interface 4bit, 2 lines, 5x8 font
        self.write_byte(0x0C, LCD_CMD)    # 00001100 Display ON/OFF: display on, cursor off, cursor blink off
        self.write_byte(0x06, LCD_CMD)    # 00000110 Entry Mode set: cursor move right, display not shift
        self.clear()

    def clear(self):
        """
        Clear the display and reset the cursor position
        """
        self.write_byte(0x01, LCD_CMD)
        time.sleep(0.002)

    def set_backlight(self, on_off):
        """
        Set whether the LCD backlight is on or off
        """
        self._backlight = on_off
        i2c_data = (self._last_data & 0xF7) + self._backlight * 0x08
        self._i2c_write(i2c_data)

    def set_cursor(self, cursor_visible, cursor_blink):
        """
        Set whether the cursor is visible and whether it will blink
        """
        cmd = 0x0C + cursor_visible * 0x02 + cursor_blink * 0x01
        self.write_byte(cmd, LCD_CMD)

    def move_cursor(self, line, column):
        """
        Move the cursor to a new posotion

        line:   line number starts from 0
        column: column number starts from 0
        """
        cmd = LCD_LINES[line] + column
        self.write_byte(cmd, LCD_CMD)

    def shift(self, direction='RIGHT', move_display=False):
        """
        Move the cursor and display left or right

        direction:      could be 'RIGHT' (default) or 'LEFT'
        move_display:   move the entire display and cursor, or only move the cursor
        """
        direction = 0x04 if direction == 'RIGHT' else 0x00
        cmd = 0x10 + direction + move_display * 0x08
        self.write_byte(cmd, LCD_CMD)

    def return_home(self):
        """
        Reset cursor and display to the original position.
        """
        self.write_byte(0x02, LCD_CMD)
        time.sleep(0.002)

    def write_CGRAM(self, chr_data, CGRAM_solt=0):
        """
        Write a custom character to CGRAM

        chr_data:     a tuple that stores the character model data
        CGRAM_solt:   int from 0 to 7 to determine where the font data is written

        NOTICE: re-setting the cursor position after calling this method, e.g.

        lcd.write_CGRAM((0x10, 0x06, 0x09, 0x08, 0x08, 0x09, 0x06, 0x00), 2)
        lcd.move_cursor(1, 0)
        lcd.print(b'New char: ' + i2clcd.CGRAM_CHR[2])
        """
        cmd = 0x40 + CGRAM_solt * 8
        self.write_byte(cmd, LCD_CMD)

        for dat in chr_data:
            self.write_byte(dat, LCD_DAT)

    def print(self, text):
        """
        Print a string at the current cursor position

        text:   bytes or str object, str object will be encoded with ASCII
        """
        if isinstance(text, str):
            text = text.encode('ascii')

        for b in text:
            self.write_byte(b, LCD_DAT)

    def print_line(self, text, line, align='LEFT'):
        """
        Fill a whole line of the LCD with a string

        text:   bytes or str object, str object will be encoded with ASCII
        line:   line number starts from 0
        align:  could be 'LEFT' (default), 'RIGHT' or 'CENTER'
        """

        if isinstance(text, str):
            text = text.encode('ascii')

        text_length = len(text)
        if text_length < self._lcd_width:
            blank_space = self._lcd_width - text_length
            if align == 'LEFT':
                text = text + b' ' * blank_space
            elif align == 'RIGHT':
                text = b' ' * blank_space + text
            else:
                text = b' ' * (blank_space // 2) + text + b' ' * (blank_space - blank_space // 2)
        else:
            text = text[:self._lcd_width]

        self.write_byte(LCD_LINES[line], LCD_CMD)
        self.print(text)
