# Memory Management in MicroPython

In the recent past, memory management has been a challenge for embedded systems.  Before 2020 microcontrollers like the Arduino usually only came with a few kilobytes of RAM, and careful attention needed to be paid to each byte using clever memory management trickery.  The memory management system in recent years has become much easier.  Even a low-cost $4 Raspberry Pi Pico now comes with 264K RAM! This is an almost 100-fold increase over the older Arduino Uno which only had 2K of RAM.  That being said, there are always developers that push their hardware to the limit, and knowing the basics of memory management is important to understand how embedded systems work.

MicroPython is very clever about how memory is allocated.  It is very stingy about memory use and will only allocate memory for what is needed.  This is very different from the standard Python that allocates memory for everything that is needed up-front assuming that most laptops, desktops and servers have gigabytes of RAM and virtual memory support.  This is an important difference, and it is important to understand if you want to push the limits of your microcontroller.

This lab will cover the basics of memory management, and how to use the memory management system in MicroPython.
We will cover the following topics:

1. Memory Management Concepts: The Heap, Stack, and Garbage Collection
2. Functions to show the amount of free and used memory and current memory usage
3. Functions to manually allocate and free memory
4. Functions to debug memory allocation

## Memory Management Concepts

![Memory Heap Stack](../img/memory-heap-stack.png)

The **memory management system** is responsible for allocating and freeing memory.  The memory management system must allocate memory for data variables, and for freeing this memory when a variable is no longer needed.  The system is also responsible for allocating memory for the parameters used by functions, and for freeing memory when a function is no longer needed.  You can read more about memory management on the [MicroPython Memory Management Docs](https://docs.micropython.org/en/latest/develop/memorymgt.html) website.

The **heap** is the area of memory that is used to store general data.  In MicroPython the heap is located in the lower memory and it grows upwards in memory address space.  The exception is memory used as parameters to functions, which is stored in the stack.

The **stack** is the area of memory that is used to store all the parameters to function calls.  In MicroPython the stack is located in the upper memory and it grows downwards in memory address space.  If you are calling highly recursive functions, the stack will get a lot of use.

The **garbage collector** is a process to reuse memory that is no longer in use.  The garbage collector is automatically run when the heap is full, but you can also run it manually to reclaim unused memory to get finer-grain control over memory usage and to avoid memory fragmentation.

In MicroPython most of these operations are done automatically for you.  You don't really need to worry about how memory works unless you are reaching the limits of what your microcontroller can do.

One other key concept is **continuous memory**.  If you are allocating a large amount of memory in an array or a long string, we need to allocate all this memory in one large chunk.  As programs run for a long time memory becomes **fragmented** (many small free sections) and can't be used for storing large arrays.

You can read more about how MicroPython is clever about memory usage by reading the [MicroPython Optimizations Docs](https://docs.micropython.org/en/latest/develop/optimizations.html) website.

## Functions to show free and used memory

We will be using the "gc" module to show the amount of free and used memory.  "gc" orignally stood for "garbage collection", but the model has been generalized to perform other memory management tasks.

Here are the key functions to show the amount of free and used memory and current memory usage on a Raspberry Pi Pico with an RP2040 microcontroller: ```gc.mem_free()``` and ```gc.mem_alloc()```:

```python
import gc
import micropython

print('Memory Free:', "{:,}".format(gc.mem_free()), 'bytes')
print('Memory Allocated:', "{:,}".format(gc.mem_alloc()), 'bytes')
```

results for RP2040:

```
Memory Free: 187,232 bytes
Memory Allocated: 4,864 bytes
```

You can see that although the RP2040 chip has a specification of 264K of RAM, it only has 187,232 bytes of RAM available for program use.  The other RAM us used to store the MicroPython interpreter software.  You can also see that the heap is currently using 4,864 bytes of RAM.  This is typical of the additional overhead that MicroPython requires to run a program.

### Viewing Memory Layout

You can use the ```micropython.mem_info(1)``` function to view the memory layout of the MicroPython interpreter.  This function returns a list of tuples, each tuple containing the address, size and type of each memory block.  The address on the left of each row is the memory address of the start of the block within the heap.  In MicroPython, memory blocks are each typically 16 bytes.

```python

```python
import micropython
print(micropython.mem_info(1))
```

results:
```
stack: 532 out of 7936
GC: total: 192064, used: 4896, free: 187168
 No. of 1-blocks: 52, 2-blocks: 13, max blk sz: 64, max free sz: 11650
GC memory layout; from 200084a0:
00000: h=MhhhBDhhBTTBDhTBDBBBh===DBDh====B=BBBBBBTB=BTB=BBBTB=TBTB=Bh==
00400: =BB=h===========TB=h=h===================h=====h==h=============
00800: ====h===========================================================
00c00: ====h===========================================================
01000: ====h=hBhh=ShhS..h=.........Sh=.................................
01400: ....Shh=======h========h====h=====..............................
       (181 lines all free)
2ec00: ....................................
None
```

This shows that the garbage collector is responsible for managing a total of 192,064 bytes of memory.  The other numbers give you an indication of how fragmented you heap is.

* The number of 1-blocks is 52
* The number of 2-block spaces is 13
* The maximum block size is 64
* The maximum free size is 11,650
* The heap starts at memory location: 2000 84a0

Each of the letters represents the type of memory at that position on the heap:

| Letter | Description |
|_|_|
|.|Free memory|
|h|head of a block of memory|
|=|tail of a block of memory|
|T|Tuple|
|L|List|
|D|Dictionary|
|S|String|
|A|Array or Byte Array|
|F|Float|
|B|Function BC|
|M|Module|

If the heap is 192,064 bytes and each block is 16 bytes then there should be 12,004 blocks on the heap.  If each row in the report displays 62 characters then there are 12,004/62=193 rows in the report.  To keep the report short, the function will only show the rows that are not free.  The report indicates that there are 181 lines all free blocks, so it will only show the non-free lines which in the example above is about six non-free rows in lower heap memory.

## Functions to manually allocate and free memory

You can manually run the garbage collector using the ```gc.collect()``` functions.  This function is used to force garbage collection exactly when you want to, not when the heap is full.  This may occur at a time that is inconvenient for the program when it must be sending data at a specific speed.

!!! Note
    Still under development.
    
```python
import gc
import micropython

def show_memory():
    print('Memory Free:', "{:,}".format(gc.mem_free()), 'bytes')
    print('Memory Allocated:', "{:,}".format(gc.mem_alloc()), 'bytes')

show_memory()
# allocate a block of memory
print('Allocating a block of memory')
myBigBlockOfMemory = matrix[100][100]
show_memory()
print('Freeing the block of memory')
# free the block of memory
gc.mem_free(ptr)
show_memory()
```
## References

* [Code that Prints Memory Block Types](https://github.com/micropython/micropython/blob/fabaa6143745cf09928dfc13367ddc91e0eb9ad2/py/gc.c#L837-L856)