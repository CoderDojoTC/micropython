# https://github.com/wendlers/micropython-mfrc522/blob/master/examples/read.py
import mfrc522
from machine import Pin
from servo import Servo
import utime

s1 = Servo(0)
sck = 6
mosi = 7
miso = 4
cs = 5 #SDA pin
rst = 22

def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(angle * 1024 / 180))

def do_read():
    rdr = mfrc522.MFRC522(sck=sck, mosi=mosi, miso=miso, rst=rst, cs=cs)
    print("")
    print("Place card before reader to read from address 0x08")
    print("")
    
    try:
        while True:
            num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK: # Access code
                    print("New card detected")
                    print(" - tag type: 0x%02x" % tag_type)
                    print(" - uid : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            if rdr.read(8) == num:
                                for i in range(0,180,10):
                                    servo_Angle(i)
                                    utime.sleep(0.05)
                                    utime.sleep(1)
                                for i in range(180,0,-10):
                                    servo_Angle(i)
                                    utime.sleep(0.05)
                            else:
                                servo_Angle(0)
                                rdr.stop_crypto1()
                        else:
                            print("Authentication error") else:
                            print("Failed to select tag")
    except KeyboardInterrupt:
        print("Bye")

do_read() # Read success, return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]