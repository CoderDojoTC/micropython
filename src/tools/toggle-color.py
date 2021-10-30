b = bytearray(b'\x01\x02\x03\x04\x05')

bl=len(b)

for i in range(bl):
    m = 0x40 # mask the most significant in a an 8 bit byte
    print('\\b', end='')
    outstr = ''
    for bit in range(0,7): 
        x = b[i] & m # and with one bit mask
        if x != 0:
            print(0, end='')
            
        else:
            print(1, end='')
        m = m >> 1
    print('')