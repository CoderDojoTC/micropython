# Timing Functions

We often need to calculate how much time has elapsed since an event occurred.  To to this we can use the ```ticks``` functions in the MicroPython utime library.

## Microsecond Timer

There are one million microseconds in a single second.  The ```utime``` library allows us to count the number of microseconds that have elapsed since the processor was powered up.

The following example times the sleep function and measures the difference in the number of clock ticks in microseconds between the two events.

```py
import machine, utime

start_time = utime.ticks_us()
# sleep for 1 second
utime.sleep(1)
end_time = utime.ticks_us()

while True:
    print("Start Time:", start_time)
    print("End Time:", end_time)
    print("Delta Time:", end_time - start_time)
    print("")
```

results:

```
Start Time: 403122147
End Time: 404122241
Delta Time: 1000094

Start Time: 403122147
End Time: 404122241
Delta Time: 1000096
```

You will note that the difference between the start and end time should be one million microseconds.  However, the run-time libraries on the pico have some variability, so you will see the actual time vary by a few microseconds.  Most of the time you can use milliseconds to compare time intervals.

## Millisecond Timer

```py
import machine, utime

start_time = utime.ticks_ms()
utime.sleep(1)
end_time = utime.ticks_ms()

while True:
    print("Start Time:", start_time)
    print("End Time:", end_time)
    print("Delta Time:", end_time - start_time)
    print("")
```

results:

```
Start Time: 855845
End Time: 856845
Delta Time: 1000

Start Time: 858031
End Time: 859032
Delta Time: 1001
```

These results are almost always 1000 with an occasional 1001 value.