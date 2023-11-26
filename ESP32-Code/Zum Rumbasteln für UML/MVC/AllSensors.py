from SoilSensor import SoilSensor
from TemperatureSensor import TemperatureSensor



class AllSensors: #Class that holds instances of every sensor to get measurments
    def __init__(self, soilData, tempData):
        self.soilData = soilData
        self.tempData = tempData
        
        self.soilSensor = SoilSensor(soilData)
        self.temperatureSensor = TemperatureSensor(tempData)
        
        
        self.soilSensorValue = 'no data'
        self.lightSensorValue = 'no data'
        self.temperaturSensorValue = 'no data'
        
    def readSoilSensor(self):
        self.soilSensorValue = self.soilSensor.readMoisture()
        
    def readTemperature(self):
        self.temperaturSensorValue = self.temperatureSensor.readTemperature()