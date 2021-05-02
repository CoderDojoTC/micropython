# VL53L0X Time-of-Flight Laser Ranging Module IR Distance Sensor

![](../img/VL53L0X_GY-530.png)
Figure: VL53L0X in the GY-530 package.

The VL53L0X is a low-cost ($5) time-of-flight light-based distance sensor that is easy to use.  It comes packaged in a I2C board and gives precise distance measurements up to 1.5 meters away.  It measures the time that light pulses take to travel to an object and back to estimate distance.  Light travels about 1 foot every nanosecond, so the timing inside this little chip must be very accurate.

The VL53L0X integrates a  group of Single Photon Avalanche Diodes (SPAD) and embeds ST Electronic's second generation FlightSense™ patented technology.  The VL53L0X’s 940 nm  emitter Vertical Cavity Surface-Emitting Laser (VCSEL), is safe for kids and totally invisible to the human eye.  Coupled with internal physical infrared filters, the sensor enables longer ranging distance, higher immunity to ambient light, and better robustness to cover glass optical crosstalk.

## Circuit
Hook the VCC to the 3.3 out of the Pico, the GND of the sensor to andy of the GND pins of the Pico and then connect the Clock and Data to two pins such as GIPO pins 16 and 17.

## Scanner

We first run the I2C scanner program to verify that the sensor is connected correct and is responding to the I2C bus scan.

```py
import machine
sda=machine.Pin(0) # row one on our standard Pico breadboard
scl=machine.Pin(1) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("Device found at decimal", i2c.scan())
```

This should return a single decimal number.

## Download The VL53L0X Driver

If you are using Thonny, you can try to use the "Manage Packages" menu and search for the 

## Create a Test Program

```py
# Test program for VL53L0X

```

## Use the Thonny Plot

## Refernces Purchase links

1. [ST Microelectronics](https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html)
2. [User Manual](https://www.st.com/resource/en/user_manual/dm00279088-world-smallest-timeofflight-ranging-and-gesture-detection-sensor-application-programming-interface-stmicroelectronics.pdf)
3. [Ebay $4](https://www.ebay.com/itm/163960247303)
4. [Amazon $12](https://www.amazon.com/VL53L0X-Ranging-Distance-Measurement-Communication/dp/B07KDQ4XQ4)

