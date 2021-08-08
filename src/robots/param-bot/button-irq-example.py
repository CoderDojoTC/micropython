import machine, utime

# the lower right coner has a wire that goes throuh
count_input = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
presses = 0

def count_handler(pin):
    global presses
    # disable the IRQ during our debounce check
    count_input.irq(handler=None)
    presses +=1
    # debounce time - we ignore any activity diring this period 
    utime.sleep_ms(200)
    # reenable the IRQ
    count_input.irq(trigger=machine.Pin.IRQ_FALLING, handler = count_handler)

count_input.irq(trigger=machine.Pin.IRQ_FALLING, handler = count_handler)

old_presses = 0
while True:
    # only print on change
    if presses != old_presses:
        if presses > old_presses + 1:
            print('double counting in irq.  Fixing...')
            presses = old_presses + 1
        print(presses)
        old_presses = presses