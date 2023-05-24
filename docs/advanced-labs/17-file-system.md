# MicroPython File Systems

Unlike older Arduino systems, MicroPython has full support for a "virtual file system" (VFS) that we use to store and retrieve programs and data.  The way we access the file systems in MicroPython
is similar to the way we access files in standard Python.

## Blocks and Fragments

First, we need to define two key terms: blocks and fragments.

The block size refers to the size of the fundamental unit of storage on the file system. All files and directories occupy an integral number of blocks, with the size of each file and directory being a multiple of the block size. The block size is typically a power of 2, and can vary depending on the file system and the size of the storage medium.

The fragment size, on the other hand, refers to the smallest unit of space that can be allocated for a file or directory. Files and directories may occupy a number of fragments that is not necessarily an integer multiple of the fragment size. Fragmentation occurs when the file system is unable to allocate a contiguous block of storage for a file or directory, resulting in the file or directory being spread out over multiple fragments. The fragment size is typically smaller than the block size, and may also vary depending on the file system and the size of the storage medium.

## File Systems Statistics

In MicroPython, the [os.statvfs('/')](https://docs.micropython.org/en/latest/library/os.html?highlight=os#os.statvfs) function provides information about the root file system. Among the information it provides is the block size and fragment size of the file system.

In the ```os.statvfs('/')``` function, the block size and fragment size are reported as the first and second elements of the tuple returned by the function, respectively. Specifically, stats[0] contains the block size, and stats[1] contains the fragment size. These values can be used to calculate various file system statistics, such as the total size of the file system, the total number of blocks and fragments, and the amount of free space available.

You can also mount file systems on other flash drives.  You can get the stats of these file systems by using the new mount point with the ```os.statvfs()``` function.

## Using Statvfs

```py
"""
Print the statistics from the virtual file system (vfs)

https://docs.micropython.org/en/latest/library/os.html?highlight=os#os.statvfs

0 f_bsize – file system block size
1 f_frsize – fragment size
2 f_blocks – size of fs in f_frsize units
3 f_bfree – number of free blocks
4 f_bavail – number of free blocks for unprivileged users
5 f_files – number of inodes
6 f_ffree – number of free inodes
7 f_favail – number of free inodes for unprivileged users
8 f_flag – mount flags
9 f_namemax – maximum filename length
"""

import os

stats = os.statvfs("/")
print(stats)

block_size = stats[0]
fragment_size = stats[1]
total_blocks = stats[2]

free_blocks = stats[3]
available_blocks = stats[4]

mount_flags = stats[8]
max_filename_length = stats[9]

# byte calculations
total_bytes = total_blocks * fragment_size
free_bytes = free_blocks * fragment_size
available_bytes = available_blocks * fragment_size

print("File system block size: {:,} bytes".format(block_size))
print("Fragement size: {:,} bytes".format(fragment_size))
print("Size of entire file system in fragement blocks: {:,}".format(total_blocks))
print("Size of entire file system in bytes: {:,}".format(total_bytes))

print("Total free blocks for system and users: {:,}".format(free_blocks))
print("Number of free blocks for unprivileged users: {:,} bytes".format(available_blocks))

print("Free size for system and users: {:,} bytes".format(free_bytes))
print("Free size for users: {:,} bytes".format(available_bytes))
print("Mount flags: {:,}".format(mount_flags))
print("Max filename length: {:,}".format(max_filename_length))
```