#lightsensor

import machine
import math, time
from machine import SoftI2C, Pin
#from Controller import Controller

class LightSensor:
    def __init__(self, lightData):
        self.scl = Pin(lightData['scl'], Pin.OUT)
        self.sda = Pin(lightData['sda'], Pin.OUT)
        self.scl_pin = machine.Pin(self.scl)
        self.sda_pin = machine.Pin(self.sda)
        self.i2c = SoftI2C(scl=Pin(self.scl), sda=Pin(self.sda))
        
        
    def readValues(self):# Convert raw data to make it readible for esp
        data = self.sda_pin.readfrom(0x23, 2)
        light_level = (data[0] << 8 | data[1]) / 1.2 #data vom sensor
        #time.sleep_ms(1000)
        return light_level
    
        
    def readLightSensor(self):
        analog_value = self.readValues
        voltage = analog_value / 1024 * 5
        resistance = 2000.0 * voltage / (1 - voltage / 5)
        lux = (50.0 * 1e3 * pow(10.0, 0.7) / resistance) ** (1.0 / 0.7) #standard umrechnung lt 

        print(analog_value, lux)

        if math.isfinite(lux):
            return("The brightness is {:.2f} lx".format(lux))
        else:
            return("Too bright to measure")

        time.sleep_ms(1000)