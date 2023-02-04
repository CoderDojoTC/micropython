from math import sqrt

def fill_circle_array(r):
    diameter = r*2
    upper_left_x = -r
    upper_left_y = -r
    print('CIRCLE_', r, ' [', sep='')
    # scan through all pixels and only turn on pixels within r of the center
    for i in range(upper_left_x, upper_left_x + diameter):
        print('[', end='')
        for j in range(upper_left_y, upper_left_y + diameter):
            # distance of the current point (i, j) from the center (cx, cy)
            d = sqrt( (i) ** 2 + (j) ** 2 )
            if d < r:
                print('1,', end='')
            else:
                print('0,', end='')
        print(']')
    print(']')

fill_circle_array(10)