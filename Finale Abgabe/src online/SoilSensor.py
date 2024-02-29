from stemma_soil_sensor import StemmaSoilSensor
import machine
from machine import SoftI2C

class SoilSensor():
    def __init__(self, soilData):
        self.i2c = SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq = 400000)
        self.s = StemmaSoilSensor(self.i2c)
        
    def readSoilSensor(self):
        soilData = self.s.get_moisture()
        tempData = self.s.get_temp()
        return soilData
            

