from math import sqrt

def fill_circle_array(r):
    r_sq = r**2 + 1
    print('CIRCLE_', r, ' = [', sep='')
    # scan through all pixels and only turn on pixels within r of the center
    for y in range(-r, r+1):
        print('[', end='')
        for x in range(-r, r+1):
            if x**2 + y**2 <= r_sq:
                print('1', end='')
            else:
                print('0', end='')
            if x < r:
                print(',', end='')
        print(']', end='')
        if y < r:
            print(',', end='')
        print('')
    print(']')

for i in range(0, 20):
    fill_circle_array(i)
