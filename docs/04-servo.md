# Micropython Servo Lab

```py
import machine
import pyb

# The pyboard has four simple servo connections
servo = pyb.Servo(1)

servo.angle(90, 5000)
```
