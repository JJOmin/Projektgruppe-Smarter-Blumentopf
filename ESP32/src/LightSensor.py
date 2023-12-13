#from utime import sleep_ms
from BH1750 import BH1750
import machine
from machine import SoftI2C

class LightSensor():
    def __init__(self, lightData):
        self.i2c = SoftI2C(scl=machine.Pin(lightData['scl']), sda=machine.Pin(lightData['sda']))
        self.s = BH1750(self.i2c)
    
    """Micropython BH1750 ambient light sensor driver."""
    
    def readLightSensor(self, mode):
       # time = utime.ticks_ms()
        #print(i2c.scan())
        lightData = self.s.luminance(mode)
            #time.sleep_ms(500)
        #print(lightData," lx")
        return lightData

