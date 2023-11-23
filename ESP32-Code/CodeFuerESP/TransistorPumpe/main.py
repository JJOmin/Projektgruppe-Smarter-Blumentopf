import time
from machine import Pin

frameRate = 60

btnPin = 17
ledPin = 4
transPin = 0

btn = Pin(btnPin, Pin.IN)
led = Pin(ledPin, Pin.OUT)
trans = Pin(transPin, Pin.OUT)

running = True

while running:
    if btn.value():
        led.on()
        trans.on()
    else:
        led.off()
        trans.off()
    print(btn.value())
    time.sleep(1/frameRate)