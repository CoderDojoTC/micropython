from utime import time, gmtime, localtime, sleep

print('time() in seconds since 1/1/1970:', time())
print('gmtime():', gmtime())
print('localtime():', localtime())

print('Year:', localtime()[0])
print('Month:', localtime()[1])
print('Day:', localtime()[2])
print('Hour 24:', localtime()[3])
# print('Hour:', hour, am_pm)
print('Minute:', localtime()[4])
print('Seconds:', localtime()[5])

while True:
    hour24 = localtime()[3]
    if hour24 > 12:
        hour = hour24 - 12
        am_pm = 'pm'
    else:
        hour = hour24
        am_pm = 'am'
    # pad minutes and seconds with leading zeros
    minutes = '{:02d}'.format(localtime()[4])
    seconds = '{:02d}'.format(localtime()[5])
    print(localtime()[2], '-', localtime()[1], '-', localtime()[0], ' ', hour, ':', minutes, ':', seconds, ' ', am_pm, sep='')
    sleep(1)
