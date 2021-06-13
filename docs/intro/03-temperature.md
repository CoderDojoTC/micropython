# Using the Builtin Temperature Sensor

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

