import time
from machine import Pin

p10 = Pin(10, Pin.OUT)
p10.off()

x = 0

while x < 10:
    x += 1
    print(x)
    p10.on()
    time.sleep(1)
    p10.off()
    time.sleep(1)

