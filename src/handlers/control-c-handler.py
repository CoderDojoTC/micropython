import time

def myMain():
    while True:
        print('in myMain')
        time.sleep(.5)
        
try:
    myMain()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('cleaning up')