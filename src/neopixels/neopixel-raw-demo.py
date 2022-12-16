import time
from neopixel import NeoPixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 8
np = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def demo(np, delay):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(delay)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (255, 255, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 255)
        else:
            np[n - 1 - (i % n)] = (0, 255, 0)
        np.write()
        time.sleep_ms(delay*2)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        time.sleep_ms(delay)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

delay = 100 # 100 millseconds between draws
counter = 0
print('Number of NeoPixels', np.n)
print('Pin Number:', np.pin)
print('Buffer Lenght:', len(np.buf))
print('Buffer:', np.buf)
for i in range(0, np.n):
    j = i * 3
    np.buf[j] = 0 # green byte
    np.buf[j+1] = 255 # red byte
    np.buf[j+2] = 0 #blue
np.write()
time.sleep(2)
print('Buffer:', np.buf)
while True:
    print('running demo', counter)
    demo(np, delay)
    counter += 1