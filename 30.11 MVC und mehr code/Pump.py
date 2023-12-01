from machine import Pin

class Pump:
    
    def __init__(self, pin):
        self.__pin = pin
        self.__pump = Pin(self.pin, Pin.OUT)

    def activatePump(self):
        self.pump.on()
        print("Pump activated!")
        
    def deactivatePump(self):
        self.pump.off()
        print("Pump deactivated!")
