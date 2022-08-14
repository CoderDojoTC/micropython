import sys

x = 'a'
# returns 50 bytes - 48 + null + 1 char
print(sys.getsizeof(x))

y = 'ab'
# returns 51 bytes
print(sys.getsizeof(y))