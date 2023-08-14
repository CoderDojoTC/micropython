# MPU-9250 Accelerometer Gyroscope Compass

The MPU-9250 by InvenSense is a nine-axis motion tracking device.  It includes:

1. A MPU-6500, which contains a 3-axis accelerometer and a 3-axis gyroscope and 
2. A AK8963, the market leading 3-axis digital compass that senses magnetic fields

(Gyro + Accelerometer + Compass) MEMS MotionTracking™ Device

1PCS GY-91 10DOF Accelerometer Gyroscope Compass Temp/Pressure MPU-9250 BMP-280

* [Art of Circuits](https://artofcircuits.com/product/10dof-gy-91-4-in-1-mpu-9250-and-bmp280-multi-sensor-module)

## Pinouts

1. VIN: Voltage Supply Pin
1. 3V3: 3.3v Regulator output
1. GND: 0V Power Supply
1. SCL: I2C Clock / SPI Clock
1. SDA: I2C Data or SPI Data Input
1. SDO/SAO: SPI Data output / I2C Slave Address configuration pin
1. NCS: Chip Select for SPI mode only for MPU-9250
1. CSB: Chip Select for BMP280

You only need to hook the 3.3 to VIN, the GND to GND and the SCL and SDA.  The other connections are not needed.

## I2C Scanner Results

```py
import machine
sda=machine.Pin(16) # row one on our standard Pico breadboard
scl=machine.Pin(17) # row two on our standard Pico breadboard
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("Device found at decimal", i2c.scan())
```

Device found at decimal [104, 118]

## MPU9250 Drivers

[MicroPython Driver](https://github.com/tuupola/micropython-mpu9250)

```py
import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)
```

## LSM6DS3 Accelerometer and Gyroscope

The LSM6DS3 is a combined 3-axis accelerometer gyroscope with an 8kb FIFO buffer and an embedded processing interrupt function for the gyro sensor, specifically for the mobile phone market.
Specifications: 

1. 3-axis accelerometer
2. 6 parameter gyroscope
3. 8K FIFO for buffering reads
4. Embedded temperature sensor
5. 3.3 logic.  Any voltages above 3.3 will damage the board
6. Gyro read data speed: 6.7ks / s
7. Accelerometer read data speed: 1.7ks / s
8. Power consumption: 0.9 mA for standard rate, 1.25 mA for high-performance mode
9. Input supply voltage: 1.71V to 5V
10. Interfaces: IIC and SPI
11. Accelerometer Sensitivity Ranges: ±2/±4/±16/±8 g
12. Gyro Sensitivity Ranges: ± 125/245/500/1000/2000 degrees per second

With LSM6DS3 breakout, you will be able to detect the motion, impact, and tilt.

## Selecting the Accelerometer Sensitivity Range

The sensitivity ratings for an accelerometer specify the maximum measurable acceleration that the device can sense along its measurement axis (or axes). When an accelerometer states its sensitivity as ±2/±4/±16/±8 g, it usually means that the device can be set to different ranges or scales of measurement. Here's what each of those ratings mean:

### ±2g Sensitivity Setting

The accelerometer can measure accelerations between -2g and +2g. This is a lower range, so it can detect small changes in acceleration with high precision. This range would be ideal for applications that require precise measurements of small movements.  For example, the orientation of a screen as it is being tilted or rotated.

### ±4g Sensitivity Setting

In this setting, the accelerometer can measure accelerations between -4g and +4g. This provides a slightly larger range than the ±2g setting, making it suitable for applications that might experience slightly stronger forces or movements but still require a good amount of precision.

One example is wearable fitness trackers, like smartwatches and sport bands, often have built-in accelerometers to monitor and analyze user movement. For regular walking or jogging, a ±2g accelerometer might suffice. However, for more intense activities like plyometric exercises, sprinting, or aggressive directional changes in sports like basketball or soccer, the forces exerted on the tracker can exceed 2g. These activities involve rapid starts, stops, jumps, and changes in direction.

Why ±4g?: The accelerometer needs to capture both the subtleties of everyday motion and the higher-intensity bursts of activity without saturating or clipping the data. A ±4g range provides a good balance between sensitivity and maximum measurable acceleration, making it suitable for wearable devices intended for diverse and dynamic physical activities.

With this capability, fitness trackers can more accurately measure and analyze the user's movements across a wider range of activities, providing better data and feedback on their workouts and performance.

±16g: 
The accelerometer can measure accelerations between -16g and +16g. This is a much broader range and is less sensitive to small movements. It's ideal for applications that are exposed to stronger forces or rapid movements, such as crash detection or certain sports applications.

±8g: The accelerometer can measure accelerations between -8g and +8g. This provides a balance between sensitivity and range, suitable for applications that might experience moderate forces.

In practice, these settings allow the user (or designer) to choose the best range for their application. For applications where precision in detecting small accelerations is essential, a lower range (like ±2g) would be selected. In contrast, for applications where large accelerations may occur, a higher range (like ±16g) would be more appropriate to prevent the sensor from saturating or clipping the readings.

## Selecting Gyroscope Sensitivity Ranges

Gyroscopes measure the rate of angular change, often referred to as the angular velocity or angular rate. The unit for this rate of change is typically represented in degrees per second (DPS).

The sensitivity ranges for a gyroscope describe the maximum rate of rotation it can measure. When a gyroscope has sensitivity ranges listed as ±125/245/500/±1000/±2000 DPS, it means the device has multiple selectable scales or ranges of measurement. Let's break down each of these ranges:

±125 DPS: At this setting, the gyroscope can measure angular velocities between -125 and +125 degrees per second. This is a low range and would provide high precision for slow rotational movements.  For example, a slowly turning sailboat.

±245 DPS: The device can measure angular velocities between -245 and +245 degrees per second. This offers a slightly larger range than the ±125 DPS setting.

±500 DPS: This setting allows the gyroscope to measure between -500 and +500 degrees per second.

±1000 DPS: The device can measure angular velocities ranging between -1000 and +1000 degrees per second. This is suitable for applications that might experience moderately fast rotations.

±2000 DPS: At this maximum setting, the gyroscope can capture angular velocities between -2000 and +2000 degrees per second. It's best for very fast rotational movements.  For example, inside a rapidly spinning ball thown in the air.


## Gyroscope Sensitivity Ranges and Their Applications

Here are some examples of different applications that might be used in each of these ranges.

### ±125 DPS

* **Wearable Health Devices**: Devices like posture trackers which monitor the orientation of a user to ensure they are maintaining a healthy posture.
* **Human Movement Analysis**: In biomechanics or rehabilitation scenarios where slow and controlled movements are being assessed.
* **Precision Robotics**: Robots that need to make very slow, controlled, and precise rotations.

### ±245 DPS

* **Consumer Electronics**: Gadgets like virtual reality (VR) headsets or augmented reality (AR) devices that track head movements, where moderate but not very rapid turns are common.
* **Gaming Controllers**: For games where precise tracking of tilt and rotation is crucial for gameplay.

### ±500 DPS

* **Drones**: Hobby drones or quadcopters that don't perform aggressive maneuvers might fit into this range.
* **Camera Gimbal Systems**: Devices that stabilize cameras may need to compensate for moderate motions.

### ±1000 DPS

* **Advanced Drones**: Racing drones or those designed for aerial acrobatics that require swift and agile movements.
* **Sports Analysis**: Tracking rapid movements in sports training equipment, like baseball or golf swing analyzers.
* **Automotive Systems**: Stability control systems in vehicles that monitor and counteract skidding or rollovers.

### ±2000 DPS

* **High-performance Aircraft**: Certain maneuvers in aeronautical or aerospace applications might need this high range.
* **High-speed Robotics**: Robots designed for tasks that involve very rapid rotations.
* **Extreme Sports Equipment**: Equipment used in scenarios where extreme rotational velocities can occur, like certain types of motorsport or action sports.


Module size: 13 * 18mm

Package Include:
1 x GY-LSM6DS3 IIC/SPI Accelerometer Tilt Angle Gyro Sensor Breakout Transfer Module

##  Settings for Robot Tracking Orientation and Position

If we are Tracking Orientation and Position for a Small Robot we need the following:

## 1. **Accelerometer**:
   - **Sensitivity**: Given the maximum speed of 6 inches per second, the accelerometer's main role is to capture any rapid starts, stops, or changes in direction. A ±2g setting is likely sufficient for most small robot applications. If uncertain about specific accelerations or possible bumps or drops, consider a ±4g setting.
   - **Purpose**: Measures acceleration and helps detect the robot's orientation with respect to the Earth's gravitational field.

## 2. **Gyroscope**:
   - **Sensitivity**: For moderate speeds and non-rapid spins, a ±250 DPS setting might be adequate. For rapid turns, a higher setting might be needed.
   - **Purpose**: Measures the rate of angular change to help determine the robot's orientation.

## 3. **Magnetometer** (if included in IMU):
   - **Purpose**: Measures the Earth's magnetic field to determine the robot's heading relative to magnetic north.

## 4. **Sensor Fusion**:
   - Combine data from the accelerometer, gyroscope, and magnetometer (if available) for a comprehensive understanding of the robot's movement and orientation.

## 5. **Additional Considerations**:
   - **Wheel Encoders**: Useful for position tracking by measuring wheel rotation.
   - **External Sensors**: Consider infrared, ultrasonic sensors, or computer vision techniques for advanced navigation and localization.

Remember to test and calibrate in real-world scenarios for optimal performance.

## References

* [MEMS YouTube Video](https://www.youtube.com/watch?v=9X4frIQo7x0) The ingenious micro mechanisms inside your phone
* [LSM6DS3 IIC/SPI 3 Axis Accelerometer Gyroscope 6 Degrees Sensor Transfer Module](https://www.ebay.com/itm/285038122433) - on Ebay for $3 each - IIC and SPI
* [SparkFun LSM6DS3 Breakout Hookup Guide](https://learn.sparkfun.com/tutorials/lsm6ds3-breakout-hookup-guide/all)