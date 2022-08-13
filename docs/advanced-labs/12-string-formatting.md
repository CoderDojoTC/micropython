# MicroPython String Formatting

The normal Python has advanced string formatting functions using "%" and .format methods documented at the [PyFormat](https://pyformat.info/) website.

Although most of these functions work, there are some exceptions when using date formats.

The following % formats do **not** work under MicroPython:

1. %Y - year
1. %m - month
1. %d - day of month
1. %H - hour of day
1. %M - minute

## Padding Example

The following example prints a floating point number with two decimals of precision in a field of six characters with leading zeros.

```python
print('{:06.2f}'.format(3.141592653589793))
```

returns:

```
003.14
```