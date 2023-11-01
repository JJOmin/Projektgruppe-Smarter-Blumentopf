import time
from machine import Pin

ledRed = Pin(10, Pin.OUT)
ledYellow = Pin(11, Pin.OUT)
ledGreen = Pin(12, Pin.OUT)
leds = [ledRed, ledYellow, ledGreen]

btnRed = Pin(35, Pin.IN)
btnYellow = Pin(36, Pin.IN)
btnGreen = Pin(37, Pin.IN)

def toggleLed(led):
    if led.value():
        led.off()
    else:
        led.on()
    time.sleep(0.5)

running = True
while running:
    status = [btnRed.value(), btnYellow.value(), btnGreen.value()]
    for i in range(3):
        if status[i]:
            toggleLed(leds[i])