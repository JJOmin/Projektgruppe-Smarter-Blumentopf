import machine
import time

testPin = machine.Pin(32, machine.Pin.OUT)
running = True


while running:
    testPin.on()
    print("On")
    time.sleep(3)
    testPin.off()
    print("Off")
    time.sleep(3)