import os

stat = os.statvfs("/")
size = stat[1] * stat[2]
free = stat[0] * stat[3]
used = size - free

KB = 1024
MB = 1024 * 1024

print("Size : {:,} bytes, {:,} KB, {} MB".format(size, size / KB, size / MB))
print("Used : {:,} bytes, {:,} KB, {} MB".format(used, used / KB, used / MB))
print("Free : {:,} bytes, {:,} KB, {} MB".format(free, free / KB, free / MB))

if   size > 8 * MB : board, flash = "Unknown", 16 * MB
elif size > 4 * MB : board, flash = "Unknown",  8 * MB
elif size > 2 * MB : board, flash = "Unknown",  4 * MB
elif size > 1 * MB : board, flash = "Pico",     2 * MB
else               : board, flash = "Pico W",   2 * MB
print("{} board with {} MB Flash".format(board, flash // MB))