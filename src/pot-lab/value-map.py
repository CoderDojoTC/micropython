# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
def valmap(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

print('Map a number from 0 to 100 to the range of 1 to 10')
print('%-8s %-6s' % ('Input', 'Output'))
for x in range(0, 100):
    print('%8.3f %6.1f' % (x, valmap(x, 0, 100.0, 1, 10.0)))