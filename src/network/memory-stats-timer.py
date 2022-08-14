import gc
from machine import Timer

initial_free_memory = gc.mem_free()

myTimer1 = Timer()
myTimer2 = Timer()
myTimer3 = Timer()
myTimer4 = Timer()
myTimer5 = Timer()
myTimer6 = Timer()
myTimer7 = Timer()
myTimer8 = Timer()
myTimer9 = Timer()
myTimer10 = Timer()

diff = initial_free_memory - gc.mem_free()

print(initial_free_memory, diff, diff/10)

