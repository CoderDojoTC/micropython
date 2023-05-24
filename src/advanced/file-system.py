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
# these return null
total_inodes = stats[5]
free_inodes = stats[6]
available_inodes = stats[7]
mount_flags = stats[8]
# this seems valid
max_filename_length = stats[9]

total_size = total_blocks * fragment_size
free_size = free_blocks * fragment_size
available_size = available_blocks * fragment_size

print("File system block size: {:,} bytes".format(block_size))
print("Fragment size: {:,} bytes".format(fragment_size))
print("Size of entire file system in fragment size units: {:,}".format(total_blocks))
print("Free blocks: {:,}".format(free_blocks))
print("Available blocks: {:,}".format(available_blocks))
print("Total size: {:,} bytes".format(total_size))
print("Number of free blocks for unprivileged users: {:,} bytes".format(available_size))
print("Total inodes: {:,}".format(total_inodes))
print("Free inodes: {:,}".format(free_inodes))
print("Available inodes: {:,}".format(available_inodes))
print("Mount flags: {:,}".format(mount_flags))
print("Max filename length: {:,}".format(max_filename_length))

"""
Pico Output:

(4096, 4096, 352, 348, 348, 0, 0, 0, 0, 255)
File system block size: 4,096 bytes
Fragment size: 4,096 bytes
Size of entire file system in fragment units: 352
Free blocks: 348
Available blocks: 348
Total size: 1,441,792 bytes
Free size: 1,425,408 bytes
Number of free blocks for unprivileged users: 1,425,408 bytes
Total inodes: 0
Free inodes: 0
Available inodes: 0
Mount flags: 0
Max filename length: 255
"""