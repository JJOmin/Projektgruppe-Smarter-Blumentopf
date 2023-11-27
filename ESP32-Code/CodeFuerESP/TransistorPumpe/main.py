import time
from machine import Pin

# Programmdurchläufe pro Sekunde
frameRate = 60

# LED und Button Pins zum Testen
btnPin = 17
ledPin = 4

# Pin zur Steuerung der Pumpe
# kann irgendein Pin sein, der digital High/Low geschaltet werden kann
transPin = 0

# Initialisieren von Pins
btn = Pin(btnPin, Pin.IN)
led = Pin(ledPin, Pin.OUT)
trans = Pin(transPin, Pin.OUT)

running = True
# Program Loop
while running:
    if btn.value():
        led.on()
        trans.on()
    else:
        led.off()
        trans.off()
    print(btn.value())
    time.sleep(1/frameRate)