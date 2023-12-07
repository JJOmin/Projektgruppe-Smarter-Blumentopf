import machine
import time
from bh1750 import BH1750

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))

#class LightSensor:
    #def __init__(self):
        #self.i2c = i2c
        #self.running = False
    
   #def readLightSensor(self):
       # time = utime.ticks_ms()
        #test = print(i2c.scan())#kontrolle ob i2c erkannt wird -> 35 = jep
       # return test
    
print(i2c.scan())
s = BH1750(i2c)

while True :
    #time.sleep_ms(500)
    lightData=s.luminance(BH1750.CONT_LOWRES)
    
    print(lightData," lx")
    


