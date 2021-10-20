# Using the Builtin Temperature Sensor

The Raspberry Pi Pico has an internal temperature sensor that can be access using ```machine.ADC(4)```.  This might be useful to see if your RP2040 CPY is running "hot" and might benefit from a cooling fan.

## Reading the temperature
```py
import machine
import utime
sensor_temp = machine.ADC(4)
while True:
   reading = sensor_temp.read_u16() * conversion_factor
   temperature = 27 - (reading - 0.706)/0.001721
   print(temperature)
   print('\n')
```

## Logging the Temperature
```py
import machine
import utime
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)
file = open("temps.txt", "w")
while True:
   reading = sensor_temp.read_u16() * conversion_factor
   temperature = 27 - (reading - 0.706)/0.001721
   file.write(str(temperature))
   file.flush()
   utime.sleep(10)
```

